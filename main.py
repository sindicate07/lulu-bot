import discord
from discord.ext import commands
from discord import app_commands
import logging
from dotenv import load_dotenv
import os
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# bot is active and syncs any commands to guild id


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")
    try:
        guild = discord.Object(id=1315069563280556072)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands to guild {guild.id}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

GUILD_ID = discord.Object(id=1315069563280556072)

# colors: lulu 0x8B463C, liz 0x7084B1,

# embed function


def embed_func(char, msg, color, char_img, leng):
    embed = discord.Embed(title=char, description='\"*' +
                          msg+'*\"', colour=color)
    embed.set_thumbnail(url=char_img[random.randint(0, leng)])
    return embed


# channeling
lulu_pics = [
    "https://images-ext-1.discordapp.net/external/WpJ_Xe9h48y3gxf96sDjRhGiwkd6CkWMPzml4KB2EGI/https/i.imgur.com/ib81H8T.png",
    "https://images-ext-1.discordapp.net/external/OEWHsURx9lgZYqzoEthpqELowYh69aMWE2bKskIMuLY/https/i.imgur.com/BKsou7M.png",
    "https://images-ext-1.discordapp.net/external/asOHhJHepMhKzY3pKtxE0FDMPnEAnaTifbZbp3RFFHc/https/i.imgur.com/hBBetW4.png",
    "https://images-ext-1.discordapp.net/external/pJKI_-daZ99UT-sfjaV4UwcSV9wcQyivwHKTTdPI1p8/https/i.imgur.com/M1STWbA.png",
    "https://images-ext-1.discordapp.net/external/8AzckEjq3FnJr7eKoIC_CIpqEmJCYQ412reg_aH5XwU/https/i.imgur.com/vFqiPJS.png;https",
    "https://images-ext-1.discordapp.net/external/GjWBO_01QnZ8PckogcVoozeHYzh1c8MluEWEqadxAcU/https/i.imgur.com/HGgZvHL.png"
]

liz_pics = [
    "https://images-ext-1.discordapp.net/external/4FOCdPuFHkGztRiBdydPQO6K2JPaYIlJ__lr1qnrLmg/https/i.imgur.com/jZmYP9u.png",
    "https://images-ext-1.discordapp.net/external/m5q1ER9-_7JFO-dWsD9MbvuKclRTeg_3PF3xnO98Qfg/https/i.imgur.com/Cl6NB2M.png",
    "https://images-ext-1.discordapp.net/external/xATB-aVNCSBrb1H3cOImbP8jhkiaCYopWM1Hdq3hD2g/https/i.imgur.com/CVrcsPT.png",
    "https://images-ext-1.discordapp.net/external/u2T5mArXIH75AlBX5kxVR7pcuNpe865oABZ8Lkt2lU0/https/i.imgur.com/xzkxWr9.png",
    "https://images-ext-1.discordapp.net/external/W-tWhKfS9kqQktq-FCdA9LZ_7V3PlCVjGIlxcnTTNrA/https/i.imgur.com/5B4bTX9.png",
    "https://images-ext-1.discordapp.net/external/MyBG3gSWU1Q-c7FrbxgW1M1icd-ksYVNUPi4lHaZ4U4/https/i.imgur.com/4kKRxLz.png"
]


@app_commands.choices(
    charater=[
        app_commands.Choice(name="Lulu", value="lulu"),
        app_commands.Choice(name="Elizabeth", value="liz")
    ]
)
@bot.tree.command(name="channel", description="Speak their tounge", guild=GUILD_ID)
async def channel(interaction: discord.Interaction, charater: app_commands.Choice[str], speech: str):
    await interaction.response.send_message("Working on it...", ephemeral=True)
    if charater.value == "lulu":
        embed = embed_func("Luna K. Lutz - :lu_khu:",
                           speech, 0x8B463C, lulu_pics, 5)
    elif charater.value == "liz":
        embed = embed_func("Elizabeth - :el_dafuk:",
                           speech, 0x7084B1, liz_pics, 5)
    await interaction.channel.send(embed=embed)

sayings = [
    '\"*I dunno! Maybe just wait a bit!*\"',
    '\"*That\'s a very unique question! I\'m sure a thousand people haven\'t asked that already!\"',
    '\"*Try being patient bitch!*\"',
    '\"*Itchers be like "when update" my witch in magic it\'s out when it\'s out!*\"',
    '\"*Me when.*\"',
    '\"*Dumbidiotsaywhenupdate?*\"',
    '\"*You just got one! Be patient, bitch!*\"',
    '\"*Seriously?*\"',
    '\"*I dunno! You tell me!*\"',
    '\"*Who knows!*\"',
    '\"*uhhhh*\"',
    '\"*I dont know!*\"']

greetings = [
    '\"*Salutations friend, I am definitely Lulu!*\"',
    '\"*Khu khu khu! Hello {mention}! It is I!*\"',
    '\"*That\'s me! Hi {mention}*\"',
    '\"*Hallo {mention}, ik ben de machtige Lulu!*\"',
    '\"*你好你好 {mention}，我絕對是真的 Lulu, 哈哈哈!*\"',
    '\"*Bonjour {mention}, C\'est moi Lulu!*\"',
    '\"*Jajaja! Hola {mention}! Me llamos La Lulu!*\"',
    '\"*Salve a {mention}! Sono la grande Lulú, Strega dell\'Altopiano!*\"',
    '\"*Ave {mention}! Ego fabulosa magus Lulu! Cogito ergo sum.*\"',
    '\"*こんにちは {mention}! 私は史上最高の魔女ルルです!*\"',
    '\"*Khu khu khu! Witaj {mention}! Oto ja, Lulu!*\"',
    '\"*Bati ni {mention}! Ako si Lulu ang dakilang banal na mangkukulam, kumusta ka na?*\"',
]


def embeded_msg(msg):
    embed = embed_func("Luna K. Lutz - :lu_khu:", msg, 0x8B463C, lulu_pics, 5)
    return embed


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    # when update

    content = msg.content.lower()
    if any(phrase in content for phrase in ("when update", "update when", "when is the update")):
        pick = random.randint(0, 1)
        if pick == 1:
            embed = embed_func("Luna K. Lutz - :lu_khu:",
                               sayings[random.randint(1, 12)], 0x8B463C, lulu_pics, 5)
            await msg.channel.send(embed=embed)
            return
        elif pick == 0:
            embed = embed_func(
                "Elizabeth - :el_dafuk:", sayings[random.randint(1, 12)], 0x7084B1, liz_pics, 5)
            await msg.channel.send(embed=embed)
            return

    # greetings

    if msg.content.lower() == "hello lulu":
        embed = embeded_msg(greetings[random.randint(
            0, 2)].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "hi lulu":
        embed = embeded_msg(greetings[random.randint(
            0, 2)].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "haii lulu":
        embed = embeded_msg(greetings[random.randint(
            0, 2)].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "hallo lulu":
        embed = embeded_msg(greetings[3].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "nihao lulu":
        embed = embeded_msg(greetings[4].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "bonjour lulu":
        embed = embeded_msg(greetings[5].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "hola lulu":
        embed = embeded_msg(greetings[6].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "ciao lulu":
        embed = embeded_msg(greetings[7].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "ave lulu":
        embed = embeded_msg(greetings[8].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "konnichiwa lulu":
        embed = embeded_msg(greetings[9].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "witam lulu":
        embed = embeded_msg(greetings[10].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return
    elif msg.content.lower() == "kumusta lulu":
        embed = embeded_msg(greetings[11].format(mention=msg.author.mention))
        await msg.channel.send(embed=embed)
        return

    await bot.process_commands(msg)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
