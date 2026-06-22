import asyncio
from datetime import datetime, timezone
import random
import math
import traceback
import copy
import characters
import re
from discord.ui import Button, View
import json
import os
from dotenv import load_dotenv
import logging
from discord import app_commands
from discord.ext import commands
import discord

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

    bot.log_channel = bot.get_channel(1204927570274033724)
    # main 1204927570274033724
    # dev 1315241396994576448

    try:
        for guild in GUILDS:
            synced = await bot.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")


# user data

DEFAULT_USER = {
    "robo_slur": 0,
    "jade_score": 0,
    "winT": 0,
    "tieT": 0,
    "loseT": 0,
    "money": 0,
    "fishing_hp": 150,
    "fishing_dmg": 1,
    "fishing_def": 0,
    "fishing_luck": 0,
    "gear": [],
    "discovered": [],
    "fishes": [],
    "stored_fishes": []
}


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


def ensure_player(data, user_id):
    plr_id = str(user_id)

    # create data
    if plr_id not in data:
        data[plr_id] = copy.deepcopy(DEFAULT_USER)
    # update older data
    else:
        for key, value in DEFAULT_USER.items():
            if key not in data[plr_id]:
                data[plr_id][key] = copy.deepcopy(value) if isinstance(
                    value, (list, dict)) else value

    return plr_id


def add_stat(user_id, stat, amount=1):
    data = load_data()

    plr_id = ensure_player(data, user_id)

    data[plr_id][stat] += amount

    save_data(data)


def reset_stat(user_id, stat):
    data = load_data()

    plr_id = ensure_player(data, user_id)

    data[plr_id][stat] = 0

    save_data(data)


def discover_potion(user_id, potion):
    data = load_data()

    plr_id = ensure_player(data, user_id)

    if potion not in data[plr_id]["discovered"]:
        data[plr_id]["discovered"].append(potion)

    save_data(data)


def add_fish(user_id, fish, size, color, rank, value):
    data = load_data()

    plr_id = ensure_player(data, user_id)

    fish_entry = {
        "fish": fish,
        "size": size,
        "color": color,
        "rank": rank,
        "value": value
    }

    data[plr_id]["fishes"].append(fish_entry)

    save_data(data)


def add_gear(user_id, item, category, cost):
    data = load_data()

    plr_id = ensure_player(data, user_id)

    if cost > data[plr_id]["money"]:
        return False
    elif item in data[plr_id]["gear"]:
        return False
    else:
        data[plr_id]["gear"][item] = category
        save_data(data)
        return True


'''
def remove_and_store(user_id, fish,):
    data = load_data()
    plr_id = ensure_player(data, user_id)

    fish_entry = {
        "fish": fish,
        "size": size,
        "color": color,
        "rank": rank,
        "value": value
    }

    data[plr_id]["fishes"].append(fish_entry)

    save_data(data)
'''

# embed function


def embed_func(char, msg, color, char_img, img_leng):
    embed = discord.Embed(
        title=char, description='\"*' + msg+'*\"', colour=color)
    embed.set_thumbnail(url=char_img[random.randint(0, img_leng)])
    return embed


blacklist = ["faggot", "fag", "nigger", "nigga", "trannie", "tranny", "kill yourself", "kys"
             "negro", "chicano", "chicana", "heil hitler", "cuck", "retard", "niga", "rape",
             "cotton picker", "chink"]


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
            btn = self.children[ingrednum]
            picked = indgredient
            index = ingrednum
            if interaction.user.id != int(self.user):
                await interaction.response.send_message("You can make your own potion using /potion!", ephemeral=True)
                return

            if picked in picked_ingred:
                await interaction.response.send_message("You already mixed this ingredient!", ephemeral=True)
                return

            btn.style = discord.ButtonStyle.red
            btn.disabled = True
            picked_ingred.append(picked)
            self.count += 1
            await interaction.response.edit_message(view=self)

            self.selected |= (1 << index)

            bitmask = self.selected
            if self.count == 3:
                if bitmask in index_lookup:  # win
                    embed = discord.Embed(title=self.name+" Mixed A...", description='\"*' +
                                          cel_potions[index_lookup[bitmask]] + " Potion!"+'*\"', colour=color)
                    embed.set_thumbnail(url=pot_img[index_lookup[bitmask]])
                    discover_potion(
                        str(self.user), cel_potions[index_lookup[bitmask]])
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


@bot.tree.command(name="brew-potions", description="Concoct your own potion!")
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
                         speech[random.randrange(speech_len)], color, pic, leng)

    user_id = str(interaction.user.id)
    user = str(interaction.user.display_name)
    fail = characters.char_library[name]["failed"]
    fail_len = len(fail)
    fail_processed = fail[random.randrange(fail_len)]
    pic_len = len(pic)
    pic_process = pic[random.randrange(pic_len)]
    view = PotionMixer(user_id, user, color, fail_processed,
                       pic_process, timeout=60)
    await interaction.channel.send(embed=embed, view=view)


# inventory command

class storage_view(View):
    def __init__(self, fishes: list, user: str):
        self.fish_data = fishes
        self.user = user
        options = []

        for i, fish in enumerate(self.fish_data):
            options.append(
                discord.SelectOption(
                    label=fish,
                    value=str(i)
                )
            )

        super().__init__()
        self.add_item(storage_select(options, self.user))


class storage_select(discord.ui.Select):
    def __init__(self, fish_options: list, user: str):
        self.user = user
        self.fish_options = fish_options
        self.data = load_data()
        self.stored_fish = []
        self.fish_data = self.data[self.user]["fishes"]

        super().__init__(
            placeholder="Choose fish to store!",
            options=self.fish_options,
            min_values=1,
            max_values=5
        )

    async def callback(self, interaction: discord.Interaction):
        selected_values = self.values  # list of selected values

        for value in selected_values:
            index = int(value)
            self.stored_fish.append(self.options[index].label)

        # test
        fishes = [
            {
                "fish": "Royal Red Shrimp",
                "size": "41",
                "color": "Red",
                "rank": "F",
                "value": 545
            },
            {
                "fish": "Chyrstal Jellyfish",
                "size": 177,
                "color": "Glossy",
                "rank": "D",
                "value": 1239
            },
            {
                "fish": "Anomalocaris",
                "size": 400000,
                "color": "########",
                "rank": "?",
                "value": 6536
            },
            {
                "fish": "Goblin Shark",
                "size": 112,
                "color": "Damascus",
                "rank": "E",
                "value": 1536
            },
            {
                "fish": "Tiger Shrimp",
                "size": 25,
                "color": "Moss",
                "rank": "F",
                "value": 345
            },
        ]

        for current_fish in self.stored_fish:
            for i, fish in enumerate(fishes):  # self.fish_data
                if current_fish in fish:
                    print("found in index: "+i)

        print(self.stored_fish)
        # ['Anomalocaris $6536', 'Goblin Shark $1536', 'Goblin Shark $1536']


class inventory(View):
    def __init__(self, user_id: int, name: str, data: list, display: bool, category: str, storedfish: list, *, timeout=60):
        super().__init__(timeout=timeout)
        self.user = user_id
        self.name = name
        self.data = data
        self.display = display
        self.type = category
        self.plr_data = load_data()
        self.page = 1
        self.store_fish = storedfish

        if self.type != "fish":
            self.remove_item(self.option3)

    @discord.ui.button(label="Back", style=discord.ButtonStyle.blurple)
    async def option2(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can check all the stuff you have using /inventory!", ephemeral=True)
            return

        if self.page == 1 and self.type != "gear":
            return
        elif self.page == 0:
            return

        self.page -= 1

        if self.type == "potion":
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
                title=f"{self.name}'s Potions - 341/{len(self.data)} (Page {self.page})",
                description="\n".join(display_potions)
            )

        elif self.type == "fish":

            page_size = 5
            start = (self.page - 1) * page_size
            end = start + page_size

            all_fish = self.plr_data[str(self.user)]["fishes"]
            formatted = []

            sort_fish = sorted(all_fish, key=lambda fish: int(
                fish["value"]), reverse=True)

            for i, fish in enumerate(sort_fish):
                formatted.append(
                    f"Fish: {fish["fish"]}\nSize: {fish["size"]} lb\nColor: {fish["color"]}\nRarity: {fish["rank"]}\nValue: ${fish["value"]}")

            display_fish = formatted[start:end]

            embed = discord.Embed(
                title=f"{self.name}'s Fishes (Page {self.page})", description="\n--------------\n".join(display_fish))

        elif self.type == "gear":

            all_gear = self.plr_data[str(self.user)]["gear"]
            sorted_category = {
                "line": [],
                "reel": [],
                "handle": [],
                "bait": []
            }
            categories = sorted_category.keys()
            categories = list(categories)
            cat_name = {"line": "Fishing Lines", "reel": "Fishing Rod Reels",
                        "handle": "Fishing Rod Handles", "bait": "Baits"}

            for gear_name, gear_type in all_gear.items():
                if gear_type == "line":
                    sorted_category["line"].append(gear_name)
                elif gear_type == "reel":
                    sorted_category["reel"].append(gear_name)
                elif gear_type == "handle":
                    sorted_category["handle"].append(gear_name)
                elif gear_type == "bait":
                    sorted_category["bait"].append(gear_name)

            embed = discord.Embed(
                title=f"{self.name}'s {cat_name[categories[self.page]]}", description="\n".join(sorted_category[categories[self.page]]))

        await interaction.edit_original_response(embed=embed)

    @discord.ui.button(label="Next", style=discord.ButtonStyle.blurple)
    async def option1(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can check all the stuff you have using /inventory!", ephemeral=True)
            return

        self.page += 1

        if self.type == "potion":
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
                title=f"{self.name}'s Potions - 341/{len(self.data)} (Page {self.page})",
                description="\n".join(display_potions)
            )

        elif self.type == "fish":
            page_size = 5
            start = (self.page - 1) * page_size
            end = start + page_size

            all_fish = self.plr_data[str(self.user)]["fishes"]
            formatted = []
            store_fish_format = []
            store_value_format = []

            sort_fish = sorted(all_fish, key=lambda fish: int(
                fish["value"]), reverse=True)

            for i, fish in enumerate(sort_fish):
                formatted.append(
                    f"Fish: {fish["fish"]}\nSize: {fish["size"]} lb\nColor: {fish["color"]}\nRarity: {fish["rank"]}\nValue: ${fish["value"]}")
                store_fish_format.append(fish["fish"])
                store_value_format.append(fish["value"])

            display_fish = formatted[start:end]
            self.store_fish = store_fish_format[start:end]
            self.store_value = store_value_format[start:end]

            embed = discord.Embed(
                title=f"{self.name}'s Fishes (Page {self.page})", description="\n--------------\n".join(display_fish))

        elif self.type == "gear":

            if self.page > 3:
                self.page == 3
                return

            all_gear = self.plr_data[str(self.user)]["gear"]
            sorted_category = {
                "line": [],
                "reel": [],
                "handle": [],
                "bait": []
            }
            categories = sorted_category.keys()
            categories = list(categories)
            cat_name = {"line": "Fishing Lines", "reel": "Fishing Rod Reels",
                        "handle": "Fishing Rod Handles", "bait": "Baits"}

            for gear_name, gear_type in all_gear.items():
                if gear_type == "line":
                    sorted_category["line"].append(gear_name)
                elif gear_type == "reel":
                    sorted_category["reel"].append(gear_name)
                elif gear_type == "handle":
                    sorted_category["handle"].append(gear_name)
                elif gear_type == "bait":
                    sorted_category["bait"].append(gear_name)

            embed = discord.Embed(
                title=f"{self.name}'s {cat_name[categories[self.page]]}", description="\n".join(sorted_category[categories[self.page]]))

        await interaction.edit_original_response(embed=embed)

    @discord.ui.button(label="Store Fish", style=discord.ButtonStyle.blurple)
    async def option3(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can store all the fish you have using /inventory!", ephemeral=True)
            return

        if self.type == "fish":
            embed = discord.Embed(
                title=f"{self.name} - Store Fish", description="")
            view = storage_view(self.store_fish, self.user)
            try:
                await interaction.followup.send(embed=embed, view=view, ephemeral=self.display)
            except Exception as e:
                traceback.print_exc()
            return


@app_commands.choices(
    stuff=[
        app_commands.Choice(name="Potions", value="potion"),
        app_commands.Choice(name="Fishes", value="fish"),
        app_commands.Choice(name="Gear", value="gear")
    ]
)
@bot.tree.command(name="inventory", description="Check all the stuff you have!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def inventory_cmd(interaction: discord.Interaction, display: bool, stuff: app_commands.Choice[str]):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    user_id = str(interaction.user.id)
    name = str(interaction.user.global_name)
    data = load_data()

    if stuff.value == "potion":
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
            title=f"{name}'s Potions - {len(all_potions)}/172",
            description="\n".join(display_potions))

        # show page buttons if above 10 potions
        if len(all_potions) > 10:
            view = inventory(user_id, name, all_potions, display)
            await interaction.followup.send(embed=embed, view=view, ephemeral=display)
        else:
            await interaction.followup.send(embed=embed, ephemeral=display)

    elif stuff.value == "fish":
        all_fish = data[user_id]["fishes"]
        formatted = []
        storage_format = []

        sort_fish = sorted(all_fish, key=lambda fish: int(
            fish["value"]), reverse=True)

        for i, fish in enumerate(sort_fish):
            formatted.append(
                f"Fish: {fish["fish"]}\nSize: {fish["size"]} lb\nColor: {fish["color"]}\nRarity: {fish["rank"]}\nValue: ${fish["value"]}")
            storage_format.append(f"{fish["fish"]} ${str(fish["value"])}")

        display_fish = formatted[:5]
        storage_fish_display = storage_format[:5]

        embed = discord.Embed(
            title=f"{name}'s Fishes", description="\n--------------\n".join(display_fish))

        if len(all_fish) > 10:
            view = inventory(user_id, name, all_fish, display,
                             stuff.value, storage_fish_display)
            await interaction.followup.send(embed=embed, view=view, ephemeral=display)
        else:
            await interaction.followup.send(embed=embed, ephemeral=display)

    elif stuff.value == "gear":
        all_gear = data[user_id]["gear"]
        sorted_category = {
            "line": [],
            "reel": [],
            "handle": [],
            "bait": []
        }

        for gear_name, gear_type in all_gear.items():
            if gear_type == "line":
                sorted_category["line"].append(gear_name)
            elif gear_type == "reel":
                sorted_category["reel"].append(gear_name)
            elif gear_type == "handle":
                sorted_category["handle"].append(gear_name)
            elif gear_type == "bait":
                sorted_category["bait"].append(gear_name)

        embed = discord.Embed(
            title=f"{name}'s Fishing Lines", description="\n".join(sorted_category["line"]))

        view = inventory(user_id, name, sorted_category, display, stuff.value)
        await interaction.followup.send(embed=embed, view=view, ephemeral=display)


# leaderboard command

@app_commands.choices(
    boards=[
        app_commands.Choice(name="Potions", value="potion"),
        app_commands.Choice(name="Insults", value="insult"),
        app_commands.Choice(name="Guesses", value="guess"),
        app_commands.Choice(name="Tic-Tac-Toe", value="ttt")
    ]
)
@bot.tree.command(name="leaderboard", description="Check top ten users!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def leaderboard(interaction: discord.Interaction, boards: app_commands.Choice[str]):
    await interaction.response.send_message("May be slow. Please be patient...", ephemeral=True)

    async def boardfunc(data_id, phrase, title_phrase):
        data = load_data()
        all_user_ids = []
        all_users_names = []
        total = []
        combined = []
        top_ten = []

        # pull user ids
        for user in data:
            all_user_ids.append(user)

        # pull names from user ids and totals
        for i in all_user_ids:
            member = interaction.guild.get_member(int(i))
            if member:
                get_name = member.display_name
            else:
                user = await bot.fetch_user(int(i))
                get_name = user.global_name
            all_users_names.append(get_name)
            total.append(data[i][data_id])

        # combine and sort
        for x in range(len(all_users_names)):
            combined.append(f"{all_users_names[x]} - {total[x]}")

        sort_users = sorted(combined, reverse=True, key=lambda x: int(
            x.split(" - ")[1]))

        for i, value in enumerate(sort_users[:10], start=1):
            top_ten.append(f"{i}. {value} {phrase}")

        embed = discord.Embed(title=f"{title_phrase}",
                              description="\n".join(top_ten), color=0xC9A227)
        await interaction.channel.send(embed=embed)

    if boards.value == "potion":
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
            member = interaction.guild.get_member(int(i))
            if member:
                get_name = member.display_name
            else:
                user = await bot.fetch_user(int(i))
                get_name = user.global_name
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

    elif boards.value == "insult":
        await boardfunc("robo_slur", "slur", "Top Ten Robot Haters")
    elif boards.value == "guess":
        await boardfunc("jade_score", "Guesses", "Top Ten Coin Flip Guessers")
    elif boards.value == "ttt":
        await boardfunc("winT", "Tic Tac toe Wins", "Top Ten Tic-Tac-Toe Winners")


# Check when was "when update" was last said

@bot.tree.command(name="last-update", description='Check when "When Update" was last said in this channel.')
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def lastuptd(interaction: discord.Interaction):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    # get the channel that the command was used in
    channel = interaction.channel

    # search messages
    target_message = None

    async for msg in channel.history(limit=10000):   # adjust limit as needed
        if any(phrase in msg.content.lower() for phrase in updt_listen):
            target_message = msg
            break

    if not target_message:
        return await interaction.followup.send(
            "Nobody has said it in recent history.",
            ephemeral=True
        )

    # time math
    now = datetime.now(timezone.utc)
    delta = now - target_message.created_at

    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    await interaction.followup.send(
        f"It's been **{days}d {hours}h {minutes}m {secs}s** since someone said it.",
        ephemeral=True
    )


# Lulu and Jade RNG games

@app_commands.choices(
    games=[
        app_commands.Choice(name="6 Sided Dice", value="6"),
        app_commands.Choice(name="20 Sided Dice", value="20"),
        app_commands.Choice(name="Play Dice", value="game")
    ]
)
@bot.tree.command(name="lulu-dice", description='Play dice with Lulu!')
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def lulugames(interaction: discord.Interaction, games: app_commands.Choice[str]):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    data = characters.char_library

    async def edit_embed(num):
        await asyncio.sleep(2)
        embed.description = phrases[num]
        await msg.edit(embed=embed)

    if games.value == "6":
        value = random.randint(1, 6)
        embed = embed_func(data["lulu"]["name"],
                           f"Hmm... You rolled a... **{value}**!",
                           data["lulu"]["color"],
                           data["lulu"]["img"],
                           data["lulu"]["pic_leng"]
                           )
        await interaction.channel.send(embed=embed)

    elif games.value == "20":
        value = random.randint(1, 20)

        phrases = [
            f"Aww... You got {value}. Better luck next time.",
            f"Mmm... You got {value}. Not too bad.",
            f"Ooo! You got {value}! Nice!",
            f"Khu, khu! You got {value}! It's your lucky day!"
        ]

        if value <= 5:
            pick = 0
        elif value <= 10:
            pick = 1
        elif value <= 15:
            pick = 2
        else:
            pick = 3

        embed = embed_func(data["lulu"]["name"],
                           phrases[pick],
                           data["lulu"]["color"],
                           data["lulu"]["img"],
                           data["lulu"]["pic_leng"]
                           )
        await interaction.channel.send(embed=embed)

    elif games.value == "game":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        dice3 = random.randint(1, 6)
        dice4 = random.randint(1, 6)
        usertotal = dice3 + dice4
        mention = interaction.user.display_name

        phrases = [
            "Khu, khu! Let's play dice!",
            f"Aww... I got a {dice1} and {dice2}!",
            f"Khu, Khu. I got a {dice1} and {dice2}!",
            f"Khuuu! I got a {dice1} and {dice2}!",
            "Your turn!",
            f"You got a {dice3} and {dice4}!",
            f"Gah! {mention}, You win...",
            "What?! A tie?? Aww...",
            "Khu, Khu, Khu! I win!"
        ]

        embed = embed_func(
            data["lulu"]["name"],
            phrases[0],
            data["lulu"]["color"],
            data["lulu"]["img"],
            data["lulu"]["pic_leng"]
        )

        msg = await interaction.channel.send(embed=embed)

        if total <= 4:
            pick = 1
        elif total <= 8:
            pick = 2
        else:
            pick = 3

        await edit_embed(pick)
        await edit_embed(4)

        await edit_embed(5)

        if usertotal > total:
            await edit_embed(6)
        elif usertotal == total:
            await edit_embed(7)
        else:
            await edit_embed(8)


# Jade coin guessing game buttons and logic

class JadeGame(View):
    def __init__(self, user_id: int, name: str, *, timeout=60):
        super().__init__(timeout=timeout)
        self.user = user_id
        self.name = name
        self.data = characters.char_library
        self.value = random.randint(0, 1)
        self.losses = 0
        self.plrData = load_data()
        self.wins = self.plrData[str(self.user)]["jade_score"]
        self.phrases = [
            "Aww, You still got 2 more tries. Don't sweat it.",
            "You still have another try! You got this.",
            "Aww, it's okay... You can always try again!",
            "Hey! You guessed correctly!",
            "Another one correct!",
            "You're a really good guesser!",
            "Wow, you're on a roll!",
            "Still going? That amazing!",
            "Flawless! How are you doing this??",
            "Nothings stopping you huh?",
            "Even this is shocking to me!",
            "Im speachless at how good your guessing skills are."
        ]

    @discord.ui.button(label="Heads", style=discord.ButtonStyle.blurple)
    async def option1(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can start your own game using /jade-coin!", ephemeral=True)
            return

        # win
        if self.value == 0:
            add_stat(str(self.user), "jade_score")
            plrdata = load_data()
            self.wins = plrdata[str(self.user)]["jade_score"]
            embed = embed_func(self.data["jade"]["name"],
                               f"{self.name} ({self.wins}) - {self.phrases[random.randint(3, 11)]}",
                               self.data["jade"]["color"],
                               self.data["jade"]["img"],
                               self.data["jade"]["pic_leng"])
        # loss
        else:
            self.losses += 1
            reset_stat(str(self.user), "jade_score")
            embed = embed_func(self.data["jade"]["name"],
                               f"{self.name} - {self.phrases[self.losses-1]}",
                               self.data["jade"]["color"],
                               self.data["jade"]["img"],
                               self.data["jade"]["pic_leng"])
            if self.losses >= 3:
                await interaction.message.edit(view=None)

        await interaction.edit_original_response(embed=embed)

        self.value = random.randint(0, 1)

    @discord.ui.button(label="Tails", style=discord.ButtonStyle.blurple)
    async def option2(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can start your own game using /jade-coin!", ephemeral=True)
            return

        # win
        if self.value == 1:
            add_stat(str(self.user), "jade_score")
            plrdata = load_data()
            self.wins = plrdata[str(self.user)]["jade_score"]
            embed = embed_func(self.data["jade"]["name"],
                               f"{self.name} ({self.wins}) - {self.phrases[random.randint(3, 11)]}",
                               self.data["jade"]["color"],
                               self.data["jade"]["img"],
                               self.data["jade"]["pic_leng"])
        # loss
        else:
            self.losses += 1
            reset_stat(str(self.user), "jade_score")
            embed = embed_func(self.data["jade"]["name"],
                               f"{self.name} - {self.phrases[self.losses-1]}",
                               self.data["jade"]["color"],
                               self.data["jade"]["img"],
                               self.data["jade"]["pic_leng"])
            if self.losses >= 3:
                await interaction.message.edit(view=None)

        await interaction.edit_original_response(embed=embed)

        self.value = random.randint(0, 1)


@app_commands.choices(
    games=[
        app_commands.Choice(name="Coin Flip", value="flip"),
        app_commands.Choice(name="Coin Guessing Game", value="game")
    ]
)
@bot.tree.command(name="jade-coin", description='Play coin games with Jade!')
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def jadegames(interaction: discord.Interaction, games: app_commands.Choice[str]):
    await interaction.response.send_message("Working on it...", ephemeral=True)\

    data = characters.char_library
    coin = ["Heads", "Tails"]
    user_id = str(interaction.user.id)
    user = str(interaction.user.display_name)

    if games.value == "flip":
        value = random.randint(0, 1)
        embed = embed_func(data["jade"]["name"],
                           f"You got... **{coin[value]}**!",
                           data["jade"]["color"],
                           data["jade"]["img"],
                           data["jade"]["pic_leng"])
        await interaction.channel.send(embed=embed)

    elif games.value == "game":
        embed = embed_func(data["jade"]["name"],
                           f"Okay {user}, Ready to play? Heads or Tails?",
                           data["jade"]["color"],
                           data["jade"]["img"],
                           data["jade"]["pic_leng"])

        view = JadeGame(user_id, user, timeout=60)
        await interaction.channel.send(embed=embed, view=view)


# Check how many times you insulted MollyBot

@bot.tree.command(name="insult-count", description='Check all the times you insulted MollyBot.')
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def counter(interaction: discord.Interaction):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    user_id = str(interaction.user.id)
    name = str(interaction.user.global_name)
    data = load_data()

    count = data[user_id]["robo_slur"]

    await interaction.channel.send(f"{name} has called MollyBot a slur {count} times.")


# Liz's choice

@bot.tree.command(name="elizabeths-choice", description='Ask Elizabeth for a book recommendation.')
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def book(interaction: discord.Interaction):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    data = characters.char_library
    phrases = characters.liz_book_phrase
    books = characters.liz_books

    randBook = random.randrange(len(books))
    pickBook = books[randBook]

    if randBook <= 60:  # num = amount of books not manga
        # book
        say = phrases[random.randrange(0, 17)]
    else:
        # manga, manhwa
        say = phrases[random.randrange(18, len(phrases))]

    embed = embed_func(data["elizabeth"]["name"],
                       say.format(book=pickBook),
                       data["elizabeth"]["color"],
                       data["elizabeth"]["img"],
                       data["elizabeth"]["pic_leng"])

    await interaction.channel.send(embed=embed)


# tic tac toe

class ttgame(View):
    def __init__(self, user_id: int, user: str, pick_char: str, smart: bool, *, timeout=60):
        super().__init__(timeout=timeout)
        self.user = user_id
        self.name = user
        self.char = pick_char
        self.picked_button = []
        self.ai_pick = []
        self.leftover_buttons = list(range(9))
        self.turn = random.randrange(2)
        win_list = {0: [0, 1, 2],
                    1: [3, 4, 5],
                    2: [6, 7, 8],
                    3: [0, 3, 6],
                    4: [1, 4, 7],
                    5: [2, 5, 8],
                    6: [0, 4, 8],
                    7: [6, 4, 2]}
        self.tiles = [None, None, None, None, None, None, None, None, None]
        self.smart = smart

        async def embed_setup(name, phrase_id):
            data = characters.char_library
            return embed_func(f"{data[name]["name"]} - {self.name}",
                              data[name]["ttt"][phrase_id],
                              data[name]["color"],
                              data[name]["img"],
                              data[name]["pic_leng"])

        async def win_func(interaction):
            for i in win_list.values():
                if all(num in self.picked_button for num in i):
                    if self.char == "lulu":
                        embed = await embed_setup(self.char, random.randint(8, 12))
                    elif self.char == "lilith":
                        embed = await embed_setup(self.char, random.randint(7, 12))
                    else:
                        embed = await embed_setup(self.char, random.randint(7, 10))

                    for i in range(9):
                        buttons = self.children[i]
                        buttons.disabled = True
                        add_stat(user_id, "winT")
                    return await interaction.response.edit_message(embed=embed, view=self)

                elif all(num in self.ai_pick for num in i):
                    if self.char == "lulu":
                        embed = await embed_setup(self.char, random.randint(13, 16))
                    elif self.char == "lilith":
                        embed = await embed_setup(self.char, random.randint(13, 17))
                    else:
                        embed = await embed_setup(self.char, random.randint(13, 14))

                    for i in range(9):
                        buttons = self.children[i]
                        buttons.disabled = True

                    add_stat(user_id, "loseT")
                    return await interaction.response.edit_message(embed=embed, view=self)

            if self.leftover_buttons == []:
                if self.char == "lulu":
                    embed = await embed_setup(self.char, random.randint(17, 20))
                elif self.char == "lilith":
                    embed = await embed_setup(self.char, random.randint(18, 21))
                else:
                    embed = await embed_setup(self.char, random.randint(15, 19))

                add_stat(user_id, "tieT")
                return await interaction.response.edit_message(embed=embed, view=self)

        async def ai_move(pick):
            ai_btn = self.children[pick]
            ai_btn.label = "O"
            ai_btn.style = discord.ButtonStyle.blurple
            ai_btn.disabled = True
            self.ai_pick.append(pick)
            self.leftover_buttons.remove(pick)
            self.tiles[pick] = "O"

        async def find_winning_move(board, player):
            win_combo = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [6, 4, 2]]

            for combo in win_combo:
                spots = [board[i] for i in combo]

                if spots.count(player) == 2 and spots.count(None) == 1:
                    return combo[spots.index(None)]

            return None

        async def smart_ai(board):
            # 1. Try to win
            move = await find_winning_move(board, "O")
            if move is not None:
                return move

            # 2. Try to block
            move = await find_winning_move(board, "X")
            if move is not None:
                return move

            # 3. Take center
            if board[4] is None:
                return 4

            # 4. Take a corner
            for i in [0, 2, 6, 8]:
                if board[i] is None:
                    return i

            # 5. Take any side
            for i in [1, 3, 5, 7]:
                if board[i] is None:
                    return i

        # button logic
        async def button(interaction: discord.Interaction, buttnum: int):
            btn = self.children[buttnum]

            if interaction.user.id != int(self.user):
                await interaction.response.send_message("You can play your own game using /tic-tac-toe!", ephemeral=True)
                return

            if btn in self.picked_button:
                await interaction.response.send_message("This button is already picked!", ephemeral=True)
                return

            if self.turn == 0:
                if self.char == "lulu":
                    embed = await embed_setup(self.char, random.randint(5, 7))
                else:
                    embed = await embed_setup(self.char, random.randint(4, 6))
                rng = random.choice(list(self.leftover_buttons))
                await ai_move(rng)
                self.turn = 1
                return await interaction.response.edit_message(embed=embed, view=self)

            # player
            btn.label = "X"
            btn.style = discord.ButtonStyle.red
            btn.disabled = True
            self.picked_button.append(buttnum)
            self.leftover_buttons.remove(buttnum)
            self.tiles[buttnum] = "X"

            if await win_func(interaction):
                return

            # AI
            if self.leftover_buttons:
                if self.smart:
                    rng = await smart_ai(self.tiles)
                else:
                    rng = random.choice(list(self.leftover_buttons))

                await ai_move(rng)
            await win_func(interaction)

            await interaction.response.edit_message(view=self)

        # create embed with buttons
        row_items = 0
        row_count = 0
        for i in range(9):
            if row_items == 3:
                row_count += 1
                row_items = 0

            buttn = discord.ui.Button(
                label="‎", style=discord.ButtonStyle.gray, row=row_count, id=i)

            async def callback(interaction, buttnum=i):
                await button(interaction, buttnum)
            buttn.callback = callback
            self.add_item(buttn)

            row_items += 1


@bot.tree.command(name="tic-tac-toe", description="Play Tic-Tac-Toe against the cast!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def tttgame(interaction: discord.Interaction):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    data = characters.char_library
    pick_char = random.choice(list(data.keys()))
    user_id = interaction.user.id
    user = str(interaction.user.display_name)
    rng = random.randrange(2)
    difficulty = False

    if rng == 0:
        difficulty = True

    if pick_char == "lulu":
        rng = random.randrange(5)
    else:
        rng = random.randrange(4)

    embed = embed_func(f"{data[pick_char]["name"]} - {user}",
                       data[pick_char]["ttt"][rng],
                       data[pick_char]["color"],
                       data[pick_char]["img"],
                       data[pick_char]["pic_leng"])

    view = ttgame(user_id, user, pick_char, difficulty, timeout=60)
    await interaction.channel.send(embed=embed, view=view)


@bot.tree.command(name="ttt-stats", description="Check your stats in Tic-Tac-Toe!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def tttgame(interaction: discord.Interaction):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    user_id = str(interaction.user.id)
    name = str(interaction.user.global_name)
    data = load_data()

    win = data[user_id]["winT"]
    tie = data[user_id]["tieT"]
    lose = data[user_id]["loseT"]
    ratio = 0
    if lose == 0:
        ratio = win
    else:
        ratio = int(win)/int(lose)

    embed = discord.Embed(
        title=f"{name}'s Tic-Tac-Toe Stats",
        description=f"Wins: {win}\nTies: {tie}\nLosses: {lose}\nW/L Ratio: {round(float(ratio), 2)}")

    await interaction.channel.send(embed=embed)


# lilith fishing game

fish_rates = [.05, .1, 1, 5, 10, 25, 40, 70]
Ranks = ["?", "S", "A", "B", "C", "D", "F", "E"]
base_line_len = [150, 120, 100, 70, 50, 40, 20, 10]
line_len_mutiplier = [3, 2, 1, 1, .8, .6, .4, .2]
fishes = characters.lily_fishes


def lily_loss(name):
    lily_data = characters.char_library
    phrases = [
        "You win some and you lose some.",
        "Don't sweat it too much kid.",
        "You almost had it.",
        "You can always try again.",
        "Plently of fish in the sea.",
        "Next time kiddo...",
        "Oh... There it goes...",
        "Oh well.",
        "Difficult, huh?",
        "Don't worry, it's not easy.",
        "Awww, so close..."
    ]
    embed = embed_func(f"({name}) {lily_data["lilith"]["name"]}",
                       phrases[random.randrange(len(phrases))],
                       lily_data["lilith"]["color"],
                       lily_data["lilith"]["img"],
                       lily_data["lilith"]["pic_leng"])
    return embed


class reel(View):
    def __init__(self, user_id, name, plr_data, rank_num, line_len, fish, fish_rank, *, timeout=600):
        super().__init__(timeout=timeout)
        self.user = user_id
        self.name = name
        self.data = plr_data
        self.fish_rarity_rank_num = rank_num
        self.line_length = line_len
        self.picked_fish = fish
        self.picked_rarity = fish_rank
        self.line_strength = self.data[str(self.user)]["fishing_hp"]
        self.reel_power = self.data[str(self.user)]["fishing_dmg"]
        self.rod_handling = self.data[str(self.user)]["fishing_def"]
        self.bait_luck = self.data[str(self.user)]["fishing_luck"]

        self.running = True
        self.grace = False
        self.message = None
        self.finished = False

        self.fish_moves = ["Pulling Left", "Pulling Right", "Resisting"]
        self.fish_picked_move = None

        self.normalized = self.fish_rarity_rank_num/170
        self.time_range = 5 - .5
        self.switch_timing = 5 - (self.time_range * round(self.normalized, 2))
        self.dmg_range = 150 - 1
        self.fish_damage = round(1 + (self.dmg_range * self.normalized))

    async def game_embed(self, emb_color):
        view = self
        embed = discord.Embed(
            title="Hooked!", description=f"Fish: {self.picked_fish}\nRank: {self.picked_rarity}\n\n{self.fish_picked_move}!\n\nLine length: {self.line_length}m\nLine strength: {self.line_strength}", color=emb_color)
        await self.message.edit(embed=embed, view=view)

    def start_reel_loop(self):
        self.loop_task = asyncio.create_task(self.reeling_loop())

    async def reeling_loop(self):
        while self.running:
            self.fish_picked_move = random.choice(self.fish_moves)
            self.grace = False
            await self.game_embed(0x808080)
            await asyncio.sleep(round(self.switch_timing, 2))

    @discord.ui.button(label="Pull Left", style=discord.ButtonStyle.blurple)
    async def left(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can catch your own fish using /fishing!", ephemeral=True)
            return

        view = self

        if self.fish_picked_move == "Pulling Left":
            self.grace = True
            await self.game_embed(0x00FF00)
        else:
            if self.rod_handling == 0:
                self.line_strength = self.line_strength - self.fish_damage
                self.grace = False
                await self.game_embed(0xFF0000)
                if self.line_strength <= 0:
                    view.running = False
                    embed = lily_loss(self.name)
                    self.loop_task.cancel()
                    await self.message.edit(embed=embed, view=None)
            else:
                self.line_strength = round(self.line_strength -
                                           (self.fish_damage - (self.fish_damage * (self.rod_handling/100))), 3)
                self.grace = False
                await self.game_embed(0xFF0000)
                if self.line_strength <= 0:
                    view.running = False
                    embed = lily_loss(self.name)
                    self.loop_task.cancel()
                    await self.message.edit(embed=embed, view=None)

    @discord.ui.button(label="Reel", style=discord.ButtonStyle.red)
    async def reelButt(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can catch your own fish using /fishing!", ephemeral=True)
            return

        view = self
        # '''
        if self.grace:
            self.line_length = self.line_length - self.reel_power
            await self.game_embed(0x00FF00)
        else:
            if self.rod_handling == 0:
                self.line_strength = self.line_strength - self.fish_damage
                self.grace = False
                await self.game_embed(0xFF0000)
                if self.line_strength <= 0:
                    view.running = False
                    embed = lily_loss(self.name)
                    self.loop_task.cancel()
                    await self.message.edit(embed=embed, view=None)
            else:
                self.line_strength = round(self.line_strength -
                                           (self.fish_damage - (self.fish_damage * (self.rod_handling/100))), 3)
                self.grace = False
                await self.game_embed(0xFF0000)
                if self.line_strength <= 0:
                    view.running = False
                    embed = lily_loss(self.name)
                    self.loop_task.cancel()
                    await self.message.edit(embed=embed, view=None)
        # '''
        x = True
        if self.finished:
            return
        # Fish catch
        if self.line_length <= 0:
            # if x:
            view.running = False
            self.finished = True
            if self.loop_task:
                self.loop_task.cancel()

            for item in self.children:
                item.disabled = True

            self.stop()

            lily_data = characters.char_library

            fish_color_rate = characters.fish_color_rate
            color_ranks = ["F", "D", "C", "B", "A", "S", "Z"]
            fish_colors = characters.fish_colors
            fish_size_rate = characters.fish_size_rate
            size_ranks = ["F", "D", "C", "B", "A", "S"]
            fish_sizes = characters.fish_sizes

            effective_luck = 1 + math.sqrt(self.bait_luck) / 10
            adjusted_color_rates = [r ** (1 / effective_luck)
                                    for r in fish_color_rate]
            adjusted_size_rates = [r ** (1 / effective_luck)
                                   for r in fish_size_rate]

            color_rng = random.choices(
                range(len(fish_color_rate)), weights=adjusted_color_rates, k=1)[0]
            pick_color_rank = color_ranks[color_rng]
            picked_color = random.choice(fish_colors[pick_color_rank])

            size_rng = random.choices(
                range(len(fish_size_rate)), weights=adjusted_size_rates, k=1)[0]
            pick_size_rank = size_ranks[size_rng]
            picked_size = random.choice(fish_sizes[pick_size_rank])

            base_fish_value = self.fish_rarity_rank_num * 6

            color_multiplier = [1.0, 1.2, 1.5, 2.2, 3.5, 6.0, 15.0]

            value = base_fish_value * \
                (1 + math.log10(picked_size)) * color_multiplier[color_rng]
            value = int(value)

            embed = embed_func(f"({self.name}) - {lily_data["lilith"]["name"]}", f"You caught a {picked_size}lb, {picked_color} {self.picked_fish}. An {self.picked_rarity} rank fish. It's Valued at... {value}! Nice work!",
                               lily_data["lilith"]["color"], lily_data["lilith"]["img"], lily_data["lilith"]["pic_leng"])

            add_fish(str(self.user), self.picked_fish, picked_size,
                     picked_color, self.picked_rarity, value)

            await self.message.edit(embed=embed, view=None)

    @discord.ui.button(label="Pull Right", style=discord.ButtonStyle.blurple)
    async def right(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can catch your own fish using /fishing!", ephemeral=True)
            return

        view = self

        if self.fish_picked_move == "Pulling Right":
            self.grace = True
            await self.game_embed(0x00FF00)
        elif self.line_strength <= 0:
            view.running = False
            embed = lily_loss(self.name)
            self.loop_task.cancel()
            await self.message.edit(embed=embed, view=None)
        else:
            if self.rod_handling == 0:
                self.line_strength = self.line_strength - self.fish_damage
                self.grace = False
                await self.game_embed(0xFF0000)
                if self.line_strength <= 0:
                    view.running = False
                    embed = lily_loss(self.name)
                    self.loop_task.cancel()
                    await self.message.edit(embed=embed, view=None)
            else:
                self.line_strength = round(self.line_strength -
                                           (self.fish_damage - (self.fish_damage * (self.rod_handling/100))), 3)
                self.grace = False
                await self.game_embed(0xFF0000)
                if self.line_strength <= 0:
                    view.running = False
                    embed = lily_loss(self.name)
                    self.loop_task.cancel()
                    await self.message.edit(embed=embed, view=None)


class fish(View):
    def __init__(self, user_id: int, user: str, *, timeout=600):
        super().__init__(timeout=timeout)
        self.user = user_id
        self.name = user
        self.wait_timer = random.randrange(10)
        self.pressed = False
        self.catch = False
        self.running = True
        self.bait_word = None
        self.message = None
        self.timings = [.7, .8, .9, 1, 2, 3]
        self.bait_list = [
            "Bite",
            "Yank",
            "Pull",
            "Snatch",
            "Stretch",
            "Draw",
            "Tug",
            "Jerk",
            "Drag",
            "Wring",
            "Rustle",
            "Boing",
            "Grab",
            "Twitch",
            "Creek"
        ]
        self.data = load_data()
        ensure_player(self.data, user_id)
        self.plr_luck = self.data[str(user_id)]["fishing_luck"]

        self.effective_luck = 1 + math.sqrt(self.plr_luck) / 10
        self.adjusted_rates = [r ** (1 / self.effective_luck)
                               for r in fish_rates]

        # pick fish
        self.rarity_rng = random.choices(
            range(len(fish_rates)), weights=self.adjusted_rates, k=1)[0]
        self.picked_rarity = Ranks[self.rarity_rng]
        self.picked_fish_list = fishes[self.picked_rarity]
        self.weights = list(
            reversed([i + 1 for i in range(len(self.picked_fish_list))]))
        self.picked_fish = random.choices(
            self.picked_fish_list, weights=self.weights, k=1)[0]

        # create line distance (scales with fish rarity)
        self.fish_index = self.picked_fish_list.index(self.picked_fish)
        self.flipped_index = (len(self.picked_fish_list) - 1) - self.fish_index
        self.fish_rarity_rank_num = round(
            round(self.flipped_index * line_len_mutiplier[self.rarity_rng]) +
            base_line_len[self.rarity_rng])
        self.line_length = (self.fish_rarity_rank_num + random.randint(1, 30))

    def start_loop(self):
        self.loop_task = asyncio.create_task(self.timer_loop())

    async def timer_loop(self):
        while self.running:
            embed = discord.Embed(
                title=f"{self.name} - Fishing...", description="...")
            await self.message.edit(embed=embed)
            await asyncio.sleep(random.randint(1, 7))
            self.bait_word = random.choice(list(self.bait_list))
            embed = discord.Embed(
                title=f"{self.name} - Fishing...", description=self.bait_word)
            await self.message.edit(embed=embed)
            await asyncio.sleep(random.choice(list(self.timings)))
            self.bait_word = None

    @discord.ui.button(label="Reel", style=discord.ButtonStyle.blurple)
    async def game(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can catch your own fish using /fishing!", ephemeral=True)
            return

        view = self
        plr_data = load_data()
        x = True

        # if self.bait_word in ["Bite", "Yank", "Pull", "Snatch", "Draw", "Tug", "Wring", "Grab"]:
        if x:
            view.running = False
            self.loop_task.cancel()
            embed = discord.Embed(
                title="Hooked!", description=f"Fish: {self.picked_fish}\nRank: {self.picked_rarity}\n\nLine length: {self.line_length}\nLine strength: ...", color=0x808080)
            view = reel(self.user, self.name, plr_data, self.fish_rarity_rank_num,
                        self.line_length, self.picked_fish, self.picked_rarity)
            view.start_reel_loop()
            view.message = self.message
            await self.message.edit(embed=embed, view=view)
        else:
            view.running = False
            embed = lily_loss(self.name)
            self.loop_task.cancel()
            await self.message.edit(embed=embed, view=None)


@bot.tree.command(name="fishing", description="Go fishing with Lilith!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def fishgame(interaction: discord.Interaction):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    data = characters.char_library
    user_id = interaction.user.id
    user_name = str(interaction.user.display_name)
    phrase = [
        "Want to go fishing?",
        "Let's get started. Just be patient."
    ]

    def lily(msg):
        return embed_func(data["lilith"]["name"],
                          msg,
                          data["lilith"]["color"],
                          data["lilith"]["img"],
                          data["lilith"]["pic_leng"])

    embed = lily(phrase[0])
    msg = await interaction.channel.send(embed=embed)
    await asyncio.sleep(2)

    embed = lily(phrase[1])
    await msg.edit(embed=embed)
    await asyncio.sleep(2)

    embed = discord.Embed(title=f"{user_name} - Fishing...", description="...")
    view = fish(user_id, user_name, timeout=300)
    view.message = await msg.edit(embed=embed, view=view)
    view.start_loop()


# shop

class shop(View):
    def __init__(self, user_id: int, name: str, display: bool, category: str, *, timeout=60):
        super().__init__(timeout=timeout)
        self.user = user_id
        self.name = name
        self.data = load_data()
        self.display = display
        self.category = category
        self.message = None
        self.page = -1
        self.page_size = None
        self.cat_name = {"line": "Fishing Lines", "reel": "Fishing Rod Reels",
                         "handle": "Fishing Rod Handles", "bait": "Baits"}
        self.stat = {"line": "Tensile Strength", "reel": "Reeling Power",
                     "handle": "Rod Handling", "bait": "Lure"}
        self.item_name_ext = {"line": "Fishing Line", "reel": "Reel",
                              "handle": "Handle", "bait": ""}
        self.stat_name = {"line": "fishing_hp", "reel": "fishing_dmg",
                          "handle": "fishing_def", "bait": "fishing_luck"}
        self.shop = []
        self.item = []
        self.shop_items = []
        self.shop_map = {
            "line": characters.fishing_lines,
            "reel": characters.rod_reels,
            "handle": characters.rod_handles,
            "bait": characters.baits}

    async def render(self):
        self.data = load_data()
        self.shop = self.shop_map.get(self.category)
        self.shop_items = list(self.shop.keys())

        self.item = self.shop_items[self.page]
        self.item_values = self.shop[self.item]

        self.item_stat = self.item_values[0]
        self.item_cost = self.item_values[1]

        embed = discord.Embed(
            title=f"{self.name} - Shop",
            description=f"Your Money: ${self.data[self.user]["money"]}\n---------------------\n{self.cat_name[self.category]}:\n\n\"{self.item} {self.item_name_ext[self.category]}\"\n{self.item_stat} {self.stat[self.category]}\n${self.item_cost}")

        return embed

    @discord.ui.button(label="Back", style=discord.ButtonStyle.blurple)
    async def option2(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can buy your own gear using /pudge-pro-shop!", ephemeral=True)
            return

        if self.page <= 0:
            return

        self.page -= 1
        embed = await self.render()
        await interaction.edit_original_response(embed=embed)

    @discord.ui.button(label="Buy", style=discord.ButtonStyle.red)
    async def buy(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can buy your own gear using /pudge-pro-shop!", ephemeral=True)
            return

        try:
            bought = add_gear(
                self.user, self.item, self.category, self.item_cost)
        except Exception as e:
            traceback.print_exc()

        if bought:
            add_stat(self.user, "money", -self.item_cost)
            embed = await self.render()
            await interaction.edit_original_response(embed=embed)
            if self.data[self.user][self.stat_name[self.category]] < self.item_stat:
                reset_stat(self.user, self.stat_name[self.category])
                add_stat(
                    self.user, self.stat_name[self.category], self.item_stat)
        else:
            await interaction.followup.send("You dont have the money or you already bought it.", ephemeral=True)

    @discord.ui.button(label="Next", style=discord.ButtonStyle.blurple)
    async def option1(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can buy your own gear using /pudge-pro-shop!", ephemeral=True)
            return

        if self.page < len(self.shop_items):
            self.page += 1
        else:
            return

        embed = await self.render()

        await interaction.edit_original_response(embed=embed)


'''
sell in bulk:

Rank: dropdown
color rank: dropdown
size: modal
value: modal
fish: modal: name of fish
'''


class sell_view(View):
    def __init__(self):
        super().__init__()
        self.add_item(sell_select())


class sell_select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Sell All", value="all"),
            discord.SelectOption(label="Sell by Rank", value="rank"),
            discord.SelectOption(label="Sell by Value", value="value"),
        ]

        super().__init__(
            placeholder="Choose how to sell...",
            options=options,
            min_values=1,
            max_values=1
        )

    async def callback(self, interaction: discord.Interaction):
        choice = self.values[0]

        if choice == "all":
            await interaction.response.send_message("Selling all fish...")

        elif choice == "rank":
            await interaction.response.send_message("Select rank next...")

        elif choice == "value":
            await interaction.response.send_message("Enter value range...")


class shop_category(View):
    def __init__(self, user_id: int, name: str, display: bool, *, timeout=60):
        super().__init__(timeout=timeout)
        self.user = user_id
        self.name = name
        self.display = display
        self.page = 1

    async def cat_setup(self, cat):
        embed = discord.Embed(
            title=f"{self.name} - Bass Pro Shop", description=f"Click Next.")
        view = shop(self.user, self.name, self.display, cat)

        return embed, view

    @discord.ui.button(label="Fishing Lines", style=discord.ButtonStyle.gray)
    async def shop1(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.follo.send_message("You can buy your own gear using /pudge-pro-shop!", ephemeral=True)
            return

        func = await self.cat_setup("line")
        embed = func[0]
        view = func[1]
        await interaction.edit_original_response(embed=embed, view=view)

    @discord.ui.button(label="Reels", style=discord.ButtonStyle.gray)
    async def shop2(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.follo.send_message("You can buy your own gear using /pudge-pro-shop!", ephemeral=True)
            return

        func = await self.cat_setup("reel")
        embed = func[0]
        view = func[1]
        await interaction.edit_original_response(embed=embed, view=view)

    @discord.ui.button(label="Rod Handles", style=discord.ButtonStyle.gray)
    async def shop3(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.follo.send_message("You can buy your own gear using /pudge-pro-shop!", ephemeral=True)
            return

        func = await self.cat_setup("handle")
        embed = func[0]
        view = func[1]
        await interaction.edit_original_response(embed=embed, view=view)

    @discord.ui.button(label="Bait", style=discord.ButtonStyle.gray)
    async def shop4(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.follo.send_message("You can buy your own gear using /pudge-pro-shop!", ephemeral=True)
            return

        func = await self.cat_setup("bait")
        embed = func[0]
        view = func[1]
        await interaction.edit_original_response(embed=embed, view=view)

    @discord.ui.button(label="Sell", style=discord.ButtonStyle.gray)
    async def shop5(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.follo.send_message("You can sell your own fish using /pudge-pro-shop!", ephemeral=True)
            return

        embed = discord.Embed(
            title=f"{self.name} - Fish Market", description="-Warning: selling fish in bulk means you can sell fish with rare colors, sizes, and the fish itself. Make sure to lock the fish you like and sell by value as it has a lower chance of selling the more rare fishes-")
        view = sell_view()
        await interaction.followup.send(embed=embed, view=view, ephemeral=self.display)


@bot.tree.command(name="pudge-pro-shop", description="Purchase all your fishing gear here!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def fishshop(interaction: discord.Interaction, display: bool):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    user_id = str(interaction.user.id)
    name = str(interaction.user.global_name)

    embed = discord.Embed(
        title=f"{name} - Bass Pro Shop",
        description="Pick a category.")
    view = shop_category(user_id, name, display)
    await interaction.followup.send(embed=embed, view=view, ephemeral=display)


# dating sim vvvvvvvvvvvvvvvvvvvvvvvvvv

class date_dialogue(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="talk", value="1"),
            discord.SelectOption(label="kiss", value="2"),
            discord.SelectOption(label="flirt", value="3"),
        ]

        super().__init__(
            placeholder="pick option",
            options=options,
            min_values=1,
            max_values=1
        )

    async def callback(self, interaction: discord.Interaction):
        choice = self.values[0]

        if choice == "all":
            await interaction.response.send_message("talk")

        elif choice == "rank":
            await interaction.response.send_message("kiss")

        elif choice == "value":
            await interaction.response.send_message("flirt")


class dating_sim(View):
    def __init__(self, user_id: int, user: str, *, timeout=600):
        super().__init__(timeout=timeout)
        self.user = user_id
        self.name = user
        time_count = 0
        self.add_item(date_dialogue())

        self.wait_timer = random.randrange(10)
        self.pressed = False
        self.catch = False
        self.running = True
        self.bait_word = None
        self.message = None

        self.data = load_data()
        ensure_player(self.data, user_id)

        def start_loop(self):
            self.loop_task = asyncio.create_task(self.timer_loop())

        async def timer_loop(self):
            while self.running:
                embed = discord.Embed(
                    title=f"{name}'s {place} date!",
                    description=f'{clock}\n\n{character}\n"{dialogue}"')
                await self.message.edit(embed=embed)
                await asyncio.sleep(1)
                time_count += 1

    @discord.ui.button(label="Move closer", style=discord.ButtonStyle.red)
    async def game(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if interaction.user.id != int(self.user):
            await interaction.response.send_message("You can catch your own fish using /fishing!", ephemeral=True)
            return

        view = self
        plr_data = load_data()

        if self.time_count >= 180:
            view.running = False
            self.loop_task.cancel()
            embed = discord.Embed("placeholder")
            await self.message.edit(embed=embed)


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
@bot.tree.command(name="dating", description="Take the cast out on a date!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def dating(interaction: discord.Interaction, character: app_commands.Choice[str]):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    user_id = str(interaction.user.id)
    name = str(interaction.user.global_name)

    embed = discord.Embed(
        title=f"{name}'s {place} date!",
        description=f'{clock}\n\n{character}\n"{dialogue}"')
    embed.set_thumbnail("placeholder")
    view = dating_sim(user_id, name)
    await interaction.followup.send(embed=embed, view=view)


'''
pick character, place/date location, and start mini game

live data embed
    embed:
        title: user's {place} date! + char icon
        energy: 120

        name
        {dialouge}

        move closer button (update icon rather than have a stat number)
        dropdown: user dialouge, give gifts

the closer you get, the more intimate you dialouge gets

mistakes:
getting too close too fast
coming off to strong

rng mood. if mood is bad, higher chance for mistakes. also changes dialouge options?
moods: depressed, sad, angry, upset, tired, relaxed, happy, cheerful, exited, bliss, horny
rates: 0.1, 5, 10, 15, 18, 100, 30, 20, 10, 5, 2

character likes, dislikes, and personaility:
food, gifts, date locations.

how to make progressing slow:
give small amounts of exp
liniear incremental exp 10/0, 20/0, 30/0, etc.
mistakes decrease exp
depending on mistake it can take more exp away

levels:
strangers, distant, aqiantance, familiar, friendly, friends, good friends, best friends, close friends, boyfriend, partners, couples, lovers,
special:
engaged, married.
corruption? (ask paps)

rewards:
side hug, hold hands, hug, caressing face, kiss on cheek, cuddling, nuzzling, kiss, pillow talk,
other:
light biting, deep kiss, hicky, nsfw rewards...
'''

# guide command vvvvvvvvvvvvvvvvvv


@bot.tree.command(name="guide", description="Everything to know about my dearest!")
@app_commands.guilds(discord.Object(id=DEV_GUILD_ID), discord.Object(id=MAEVE_GUILD_ID))
async def guide(interaction: discord.Interaction):
    await interaction.response.send_message("Working on it...", ephemeral=True)


# reaction messages
char_nicknames = {
    "lovestruck elizabeth": ["freak", "whore", "slut", "my bitch"],
    "astrologist elizabeth": [],
    "elvira": ["mommy"],
    "lulu": ["lulu the booboo", "lulu the poopoo"],
    "elizabeth": ["liz", "four eyes", "nerd", "izzy", "lizzie", "lizzy", "starlight"],
    "agnes": ["aggy"],
    "celine": ["its lupus", "it's lupus", "it has to be lupus", "it is lupus", "is it lupus", "it's never what",
               "its never what", "you have lupus", "do you have lupus", "he have lupus", "she have lupus", "has lupus", "have lupus"],
    "maeve": [],
    "jade": ["sunshine"],
    "arthur": ["goodie two shoes", "white knight", "prince charming", "penis-haver", "penis haver"],
    "annie": ["ann"],
    "lilith": ["lily"],
    "angelika": ["angel"],
    "dahlia": [],
    "elena": [],
    "mollybot": ["clankers", "tin skin", "toaster", "wireback", "cog sucker", "gear muncher", "clanker", "gear head", "tin can", "oil drinker", "oil guzzler"]
}
listen = ("hii", "haii", "hey", "how are you", "hello", "howdy",
          "greetings", "morning", "afternoon", "evening", "what's up", "whats up", "sup", "wasap", "yo")
bye_listen = ("bye", "goodbye", "take care", "see you later",
              "see ya", "later", "cya", "night", "farewell", "goodnight")
updt_listen = ("when update", "update when", "when is the update", "is the update out", "is update out", "next update",
               "update out yet", "updated yet", "is it updated", "has it updated", "update coming", "update plz", "update pls",
               "did update come out", "has the update come out", "update come yet", "new update when", "did they update",
               "have they updated", "update already", "bro update when", "still no update", "update now", "update please", "update pretty please")


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


def response(content, msg, liz):
    name, nick = get_name(content)

    if nick and re.search(rf"\b{re.escape(nick)}\b", content):
        greeting_type = "nick"
    elif any(phrase in content for phrase in listen) and liz and re.search(rf"\b{re.escape('mom')}\b", content):
        greeting_type = "mom"
        name = "elvira"
    elif any(phrase in content for phrase in bye_listen) and liz and re.search(rf"\b{re.escape('mom')}\b", content):
        greeting_type = "mom2"
        name = "elvira"
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

    embed = embed_func(char_name, greetings[random.randrange(length)].format(
        mention=msg.author.mention, value=random.randint(0, 99)), color, picture, img_length)

    if name == "mollybot" and nick:
        add_stat(msg.author.id, "robo_slur")

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
        embed = embed_func(char_name, greetings[random.randrange(length)].format(
            mention=msg.author.mention, value=random.randint(0, 99)), color, picture, img_length)
        return embed


expel_dial = characters.expel_dial


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    # liz exclusive
    if msg.author.id == 773248713329344522:
        liz = True
    else:
        liz = False

    # lulu language
    embed = lulu_response(msg.content.lower(), msg)
    if embed:
        await msg.channel.send(embed=embed)
        return

    # respond to key words and name
    embed = response(msg.content.lower(), msg, liz)
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
        global_name = user.display_name
    if title == "Ban Result:" or title == "Kick Result:":
        embed = discord.Embed(title="Maeve Midnight",  description='\"*' +
                              expel_dial[random.randint(0, 8)].format(mention=global_name)+'*\"', color=0x4C2F35)
        embed.set_thumbnail(url=characters.ma_img)
        await msg.channel.send(embed=embed)
        return

    # passive interactions
    '''
    cast = ["lulu", "elizabeth", "agnes", "celine", "maeve", "jade", "arthur",
            "annie", "lilith", "angelika", "dahlia", "elena", "mollybot",
            "lovestruck elizabeth", "astrologist elizabeth", "elvira"
            ]
    rng = random.randint(0, 75)
    if rng == 8:
        data = characters.char_library
        char = cast[random.randrange(len(cast))]
        embed = embed_func(
            data[char]["name"],
            data[char]["passive"][random.randrange(
                len(data[char]["passive"]))],
            data[char]["color"],
            data[char]["char_img"],
            data[char]["img_leng"])
        await msg.channel.send(embed=embed)
        return
'''
    await bot.process_commands(msg)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)

#paps is big, fat, and stinky, for wanting to give himself spoilers!!!!
