import discord
from discord.ext import commands
from discord import app_commands
import logging
from dotenv import load_dotenv
import os
import json
from discord.ui import Button, View
import re
import characters
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# checks if bot is active and syncs any commands to guild id

DEV_GUILD_ID = 1315069563280556072
MAEVE_GUILD_ID = 959668492800524308

GUILDS = [discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID)]


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

    bot.log_channel = bot.get_channel(1450870004323975288)
    # main 1450870004323975288
    # dev 1315241396994576448

    try:
        for guild in GUILDS:
            synced = await bot.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

# embed function


def embed_func(char, msg, color, char_img, img_leng):
    embed = discord.Embed(
        title=char, description='\"*' + msg+'*\"', colour=color)
    embed.set_thumbnail(url=char_img[random.randint(0, img_leng)])
    return embed


blacklist = ["faggot", "fag", "nigger", "nigga", "trannie", "tranny", "kill yourself", "kys"
             "negro", "chicano", "chicana", "heil hitler", "cuck", "retard", "niga", "rape", "cotton picker", "chink"]

# handler function to add readbility


def Char_handler(content, name, speech, color, img, img_leng):
    if any(phrase in content for phrase in (blacklist)):
        return
    else:
        embed = embed_func(name, speech, color, img, img_leng)
        return embed

# channeling command


@app_commands.choices(
    character=[
        app_commands.Choice(name="Lulu", value="lulu"),
        app_commands.Choice(name="Elizabeth", value="elizabeth"),
        app_commands.Choice(name="Agnes", value="agnes"),
        app_commands.Choice(name="Céline", value="celine"),
        app_commands.Choice(name="Maeve", value="maeve"),
        app_commands.Choice(name="Jade", value="jade"),
        app_commands.Choice(name="Arthur", value="arthur"),
        app_commands.Choice(name="Annie", value="annie"),
        app_commands.Choice(name="Lilith", value="lilith"),
        app_commands.Choice(name="Angelika", value="angelika"),
        app_commands.Choice(name="Dahlia", value="dahlia"),
        app_commands.Choice(name="Elena", value="elena"),
        app_commands.Choice(name="MollyBot", value="mollybot"),
        app_commands.Choice(name="Lovestruck elizabeth",
                            value="lovestruck elizabeth"),
        app_commands.Choice(name="Astrologist elizabeth",
                            value="astrologist elizabeth"),
        app_commands.Choice(name="Elvira", value="elvira")
    ]
)
@bot.tree.command(name="channel", description="Speak their tounge")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def channel(interaction: discord.Interaction, character: app_commands.Choice[str], speech: str):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    content = speech.lower()

    name = characters.char_library[character.value]["name"]
    color = characters.char_library[character.value]["color"]
    pic = characters.char_library[character.value]["img"]
    leng = characters.char_library[character.value]["pic_leng"]

    embed = Char_handler(content, name, speech, color, pic, leng)

    await bot.log_channel.send(f"{interaction.user.global_name} said: {speech}")

    await interaction.channel.send(embed=embed)

# save data


def load_data():
    if not os.path.exists("data.json"):
        # File doesn’t exist — make a new one
        with open("data.json", "w") as f:
            json.dump({}, f)
        return {}

    with open("data.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # File is empty or broken — reset it
            return {}


def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def add_potion(user_id, potion):
    data = load_data()
    plr_id = str(user_id)

    if plr_id not in data:
        data[plr_id] = {"discovered": []}

    if potion not in data[plr_id]["discovered"]:
        data[plr_id]["discovered"].append(potion)

    save_data(data)


# potion maker command

pot_img = characters.pot_img
cel_potions = characters.cel_potions
index_lookup = characters.index_lookup
teachers = ("maeve", "celine", "lilith", "agnes")


class PotionMixer(View):
    def __init__(self, user: str, name: str, color: str, fail: str, img: str, *, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.user = user
        self.name = name
        self.color = color
        self.count = 0
        self.fail = fail
        self.img = img

        self.ingred = ("Bainberry", "Bee's Brain", "Blueleaf", "Cat-trap Flower", "Darknut", "Dragonwort", "Frog's Tears",
                       "Bugle Shell", "Feather of Crow", "Honeysuckle", "Mandrake Root", "Nightshade", "Slug's Eggs", "Yarrow Root", "Moonrock")
        picked_ingred = []
        self.selected = 0

        # button logic
        async def option(interaction: discord.Interaction, indgredient: str, ingrednum: int):
            picked = indgredient
            index = ingrednum
            if interaction.user.id != int(self.user):
                await interaction.response.send_message("You can make your own potion using /potion!", ephemeral=True)
                return

            if picked in picked_ingred:
                await interaction.response.send_message("You already mixed this ingredient!", ephemeral=True)
                return

            picked_ingred.append(picked)
            self.count += 1

            self.selected |= (1 << index)

            bitmask = self.selected
            if self.count == 3:
                if bitmask in index_lookup:  # win
                    embed = discord.Embed(title=self.name+" Mixed A...", description='\"*' +
                                          cel_potions[index_lookup[bitmask]] + " Potion!"+'*\"', colour=color)
                    embed.set_thumbnail(url=pot_img[index_lookup[bitmask]])
                    add_potion(self.user, cel_potions[index_lookup[bitmask]])
                else:  # loss
                    embed = discord.Embed(
                        title=self.name+" Failed Mixing A Potion", description='\"*'+self.fail+'*\"', colour=color)
                    embed.set_thumbnail(url=self.img)

                await interaction.message.edit(view=None)
                await interaction.channel.send(embed=embed)

            await interaction.response.defer()

        # create embed with buttons
        row_items = 0
        row_count = 0
        for i in range(len(self.ingred)):
            if row_items == 5:
                row_count += 1
                row_items = 0

            buttn = discord.ui.Button(
                label=self.ingred[i], style=discord.ButtonStyle.gray, row=row_count)
            ingredient = self.ingred[i]

            async def callback(interaction, ingredient=ingredient, ingrednum=i):
                await option(interaction, ingredient, ingrednum)
            buttn.callback = callback
            self.add_item(buttn)

            row_items += 1


@bot.tree.command(name="potion", description="Concoct your own potion!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def game(interaction: discord.Interaction):
    await interaction.response.send_message("If it didn't load, keep sending it again.", ephemeral=True)
    name = teachers[random.randint(0, 4)]
    char_name = characters.char_library[name]["name"]
    color = characters.char_library[name]["color"]
    pic = characters.char_library[name]["img"]
    leng = characters.char_library[name]["pic_leng"]
    content = ""
    speech = characters.char_library[name]["teach"]
    speech_len = len(speech)
    embed = Char_handler(content, char_name + " - Potion Mixing Class",
                         speech[random.randint(0, speech_len)], color, pic, leng)

    user_id = str(interaction.user.id)
    user = str(interaction.user.global_name)
    fail = characters.char_library[name]["failed"]
    fail_len = len(fail)
    fail_processed = fail[random.randint(0, fail_len)]
    pic_len = len(pic)
    pic_process = pic[random.randint(0, pic_len)]
    view = PotionMixer(user_id, user, color, fail_processed,
                       pic_process, timeout=60)
    await interaction.channel.send(embed=embed, view=view)

# potion inventory command


class inventory(View):
    def __init__(self, user_id: int, name: str, data: list, display: bool, *, timeout=60):
        super().__init__(timeout=timeout)
        self.user = user_id
        self.name = name
        self.data = data
        self.display = display
        self.page = 1

    @discord.ui.button(label="Back", style=discord.ButtonStyle.blurple)
    async def option2(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can check potions you've made using /my-potion!", ephemeral=True)
            return

        self.page -= 1

        if self.page == 0:
            self.page += 1
            return

        # get the page index for potions
        page_size = 10
        start = (self.page - 1) * page_size
        end = start + page_size

        # format and put all_potion into a list of 10
        sorted_potions = sorted(
            self.data, key=lambda x: int(x.split("-")[0]))

        # slice
        display_potions = sorted_potions[start:end]

        # embed display

        embed = discord.Embed(
            title=f"{self.name}'s Potions - 172/{len(self.data)} (Page {self.page})",
            description="\n".join(display_potions)
        )

        await interaction.edit_original_response(embed=embed)

    @discord.ui.button(label="Next", style=discord.ButtonStyle.blurple)
    async def option1(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can check potions you've made using /my-potion!", ephemeral=True)
            return

        self.page += 1

        # get the page index for potions
        page_size = 10
        start = (self.page - 1) * page_size
        end = start + page_size

        # format and put all_potion into a list of 10
        sorted_potions = sorted(
            self.data, key=lambda x: int(x.split("-")[0]))

        # slice
        display_potions = sorted_potions[start:end]

        # embed display

        embed = discord.Embed(
            title=f"{self.name}'s Potions - 172/{len(self.data)} (Page {self.page})",
            description="\n".join(display_potions)
        )

        await interaction.edit_original_response(embed=embed)


@bot.tree.command(name="my-potion", description="Check all the potions you've made!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def game(interaction: discord.Interaction, display: bool):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    user_id = str(interaction.user.id)
    name = str(interaction.user.global_name)
    data = load_data()
    all_potions = []
    display_potions = []

    # grab all discovered potions (data)
    for found_potion in data[user_id]["discovered"]:
        for i, potions in enumerate(cel_potions):
            if potions == found_potion:
                all_potions.append(f"{i} - {found_potion} Potion")

    # format and put all_potion into a list of 10 (page 1)
    sorted_potions_list = sorted(
        all_potions, key=lambda x: int(x.split("-")[0]))

    display_potions = sorted_potions_list[:10]

    # embed display
    embed = discord.Embed(
        title=f"{name}'s Potions - 172/{len(all_potions)}",
        description="\n".join(display_potions)
    )

    # show page buttons if above 10 potions
    if len(all_potions) > 10:
        view = inventory(user_id, name, all_potions, display)
        await interaction.followup.send(embed=embed, view=view, ephemeral=display)
    else:
        await interaction.followup.send(embed=embed, ephemeral=display)

# leaderboard command


@bot.tree.command(name="leaderboard", description="Check top ten potioneers!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def game(interaction: discord.Interaction):
    await interaction.response.send_message("May be slow. Please be patient...", ephemeral=True)

    data = load_data()
    all_user_ids = []
    all_users_names = []
    all_total_potions = []
    combined = []
    top_ten = []

    # pull user ids
    for user in data:
        all_user_ids.append(user)

    # pull names from user ids and potion totals
    for i in all_user_ids:
        user = await bot.fetch_user(i)
        get_name = user.global_name or user.name
        all_users_names.append(get_name)
        all_total_potions.append(len(data[i]['discovered']))

    # combine and sort
    for x in range(len(all_users_names)):
        combined.append(f"{all_users_names[x]} - {all_total_potions[x]}")

    sort_users = sorted(combined, reverse=True, key=lambda x: int(
        x.split(" - ")[1]))

    for i, value in enumerate(sort_users[:10], start=1):
        top_ten.append(f"{i}. {value} Potions")

    embed = discord.Embed(title=f"Top Ten Potioneers",
                          description="\n".join(top_ten), color=0xC9A227)

    await interaction.channel.send(embed=embed)


# reaction messages
char_nicknames = {
    "lovestruck elizabeth": ["freak", "whore", "slut", "my bitch"],
    "astrologist elizabeth": [],
    "elvira": ["mommy"],
    "lulu": ["lulu the booboo", "lulu the poopoo"],
    "elizabeth": ["liz", "four eyes", "nerd", "izzy", "lizzie", "lizzy", "starlight"],
    "agnes": ["aggy"],
    "celine": ["its lupus", "it's lupus", "it has to be lupus", "it is lupus", "is it lupus", "it's never what", "its never what", "you have lupus", "do you have lupus", "he have lupus", "she have lupus", "has lupus", "have lupus"],
    "maeve": [],
    "jade": ["sunshine"],
    "arthur": ["goodie two shoes", "white knight", "prince charming", "penis-haver", "penis haver"],
    "annie": ["ann"],
    "lilith": ["lily"],
    "angelika": ["angel"],
    "dahlia": [],
    "elena": [],
    "mollybot": ["clankers", "tin skin", "toaster", "wireback", "cog sucker", "gear muncher", "clanker"]
}
listen = ("hii", "haii", "hey", "how are you", "hello", "howdy",
          "greetings", "morning", "afternoon", "evening")
bye_listen = ("bye", "goodbye", "take care", "see you later",
              "see ya", "later", "cya", "night", "farewell", "goodnight")
updt_listen = ("when update", "update when", "when is the update", "is the update out", "is update out", "next update",
               "update out yet", "updated yet", "is it updated", "has it updated", "did the update", "update soon", "update coming", "update plz", "update pls", "when patch", "patch when", "is there an update", "did update come out", "has the update come out", "update come yet", "new update when", "new patch when", "did they update", "have they updated", "update already", "bro update when", "still no update", "update now")


def contains_word(word: str, text: str) -> bool:
    return re.search(rf"\b{re.escape(word)}\b", text) is not None


def get_name(content: str):
    msg = content.lower()
    for name, nickname_list in char_nicknames.items():
        for nick in nickname_list:
            if nick and contains_word(nick, msg):
                return name, nick
    for name in char_nicknames.keys():
        if contains_word(name, msg):
            return name, None
    return None, None


def response(content, msg):
    name, nick = get_name(content)
    if nick and re.search(rf"\b{re.escape(nick)}\b", content):
        greeting_type = "nick"
    elif any(phrase in content for phrase in listen):
        greeting_type = "greet"
    elif any(phrase in content for phrase in bye_listen):
        greeting_type = "bye"
    else:
        return

    char_name = characters.char_library[name]["name"]
    color = characters.char_library[name]["color"]
    picture = characters.char_library[name]["img"]
    length = len(characters.char_library[name][(greeting_type)])
    img_length = characters.char_library[name]["pic_leng"]
    greetings = characters.char_library[name][greeting_type]

    embed = embed_func(char_name, greetings[random.randint(0, length)].format(
        mention=msg.author.mention, value=random.randint(0, 99)), color, picture, img_length)
    return embed


def lulu_response(content, msg):
    lulu_lang = characters.lulu_language
    if any(phrase in content for phrase in (lulu_lang)):
        for lang in lulu_lang:
            if lang in content:
                lulu_pics = characters.lulu_pics
                embed = embed_func("Luna K. Lutz - <:lu_khu:971274776993730611>",
                                   lulu_lang[lang].format(mention=msg.author.mention), 0x8B463C, lulu_pics, 5)
                return embed


def updt_response(content, msg):
    if any(phrase in content for phrase in updt_listen):
        name = random.choice(list(char_nicknames.keys()))
        char_name = characters.char_library[name]["name"]
        color = characters.char_library[name]["color"]
        picture = characters.char_library[name]["img"]
        img_length = characters.char_library[name]["pic_leng"]
        length = len(characters.char_library[name]["updt"])
        greetings = characters.char_library[name]["updt"]
        embed = embed_func(char_name, greetings[random.randint(0, length)].format(
            mention=msg.author.mention, value=random.randint(0, 99)), color, picture, img_length)
        return embed


expel_dial = characters.expel_dial


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    # lulu language
    embed = lulu_response(msg.content.lower(), msg)
    if embed:
        await msg.channel.send(embed=embed)
        return

    # respond to key words and name
    embed = response(msg.content.lower(), msg)
    if embed:
        await msg.channel.send(embed=embed)
        return

    # when update
    embed = updt_response(msg.content.lower(), msg)
    if embed:
        await msg.channel.send(embed=embed)
        return

     # expulsion
    get_ban = msg.embeds[0]
    title = get_ban.title
    desc = get_ban.description
    match = re.search(r'\d{17,19}', desc)
    if match:
        user_id = int(match.group(0))
        user = await bot.fetch_user(user_id)
        global_name = user.global_name or user.name
    if title == "Ban Result:" or title == "Kick Result:":
        embed = discord.Embed(title="Maeve - <:ma_smile:1285178007761453057>",  description='\"*' +
                              expel_dial[random.randint(0, 8)].format(mention=global_name)+'*\"', color=0x4C2F35)
        embed.set_thumbnail(url=characters.ma_img)
        await msg.channel.send(embed=embed)
        return

    await bot.process_commands(msg)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)


# totally not a trojan.
# DONT LOOK

'''
if paps == check:
    upload trojan:
    import leathal.virus.exe
else
    import witching.powers.exe
'''











