import discord
from discord.ext import commands
from discord import app_commands
import logging
from dotenv import load_dotenv
import os
import random
import characters
import re

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


blacklist = ["faggot", "fag", "nigger", "nigga", "trannie", "tranny",
             "negro", "chicano", "chicana", "heil hitler", "cuck", "retard", "niga"]

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
        app_commands.Choice(name="MollyBot", value="mollybot")
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

    await interaction.channel.send(embed=embed)

# reaction messages
char_nicknames = {
    "lulu": ["lulu the booboo"],
    "elizabeth": ["liz", "four eyes"],
    "agnes": ["aggy"],
    "celine": [],
    "maeve": [],
    "jade": [],
    "arthur": [],
    "annie": ["ann"],
    "lilith": ["lily"],
    "angelika": ["angel"],
    "dahlia": [],
    "elena": [],
    "mollybot": []
}
listen = ("hii", "haii", "hey", "how are you", "hello", "howdy", "greetings")
bye_listen = ("bye", "goodbye", "take care", "see you later",
              "see ya", "later", "cya", "night", "farewell")
updt_listen = ("when update", "update when", "when is the update", "is the update out", "is update out",
               "update out yet", "updated yet", "is it updated", "has it updated", "did the update", "update soon", "update coming", "update plz", "update pls", "when patch", "patch when", "is there an update", "did update come out", "has the update come out", "update come yet", "new update when", "new patch when", "did they update", "have they updated", "update already", "bro update when", "still no update", "update now")


def get_name(content: str):
    msg = content.lower()
    for name, nickname in char_nicknames.items():
        if name in msg:
            return name, None
        for nick in nickname:
            if nick in msg:
                return name, nick
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








