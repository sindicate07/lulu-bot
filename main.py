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

# embed function


def embed_func(char, msg, color, char_img, img_leng):
    embed = discord.Embed(title=char, description='\"*' +
                          msg+'*\"', colour=color)
    embed.set_thumbnail(url=char_img[random.randint(0, img_leng)])
    return embed


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
agnes_pics = [
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431938931108216894/agnes_bottom_og1.png?ex=68ff3c8d&is=68fdeb0d&hm=732418916587fb1ec34b2b39c96384cb6f6712e93581d2e8b54d9c4571052a3b&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431938954025893938/References_202312032037501.png?ex=68ff3c92&is=68fdeb12&hm=0d6ce831553a16896b0d6e66cbb34c5f3fa1bacce0b0fdb7538de06d58b3d4cf&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431938985457877065/References_202312032037502.png?ex=68ff3c9a&is=68fdeb1a&hm=5860b6bc2ebf6cbeb39d70d04f02baeaa789077ae5a8eb86c1d27cfba1fda4a3&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431939006676996096/References_202312032037503.png?ex=68ff3c9f&is=68fdeb1f&hm=ce750f7f30315aa312cb9137143fdd99f9ee780bbeeb8c0b9c0775c8bea6da1d&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431939030727266396/References_202312032037504.png?ex=68ff3ca5&is=68fdeb25&hm=86a6c29b84b2c75232d95b9e4c79ce43ad7bb05816590b5237f354434331d8de&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431939054169100328/References_202312032037505.png?ex=68ff3caa&is=68fdeb2a&hm=aace006014948f29bce57e26932e9416af81166f3758d44a62b1a6c2afa9d20e&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431939078042947698/References_202312032037506.png?ex=68ff3cb0&is=68fdeb30&hm=b35cb901aac2e3dbd5e90afc2bdc749c9310e1b83851f572e9da62f86b6fa87a&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431939139317661777/Agnes_bust.webp?ex=68ff3cbe&is=68fdeb3e&hm=921744f2dcf8054776ffd18b33f41fff67cde264c7d49cac24f44aab1b4e567f&"
]
celine_pics = [
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431932409900699679/cel_og_11.png?ex=68ff367a&is=68fde4fa&hm=94fe98cbdea52a32b19383453aa40cbf878fe6bced3521d2385846e5749367f6&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431932432667640042/References_202401222311541.png?ex=68ff367f&is=68fde4ff&hm=6e5655904f9d5fd00b40609c98df3779f4b1cb55b8f9868ff21cd07586154788&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431932453941018684/References_202401222311542.png?ex=68ff3685&is=68fde505&hm=a34078962459b892afbd4015a75452b97b064313f7ad349406bfcbbaaae0d51b&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431932471833792652/References_202401222311543.png?ex=68ff3689&is=68fde509&hm=3a593a8110d0657fb0e82b71b7f6ef0a9048408623dea8cc84eac969967f7807&"
]
maeve_pics = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
jade_pics = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
arthur_pics = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
annie_pics = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
lily_pics = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
angel_pics = [
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431928882906529892/References_202311152044481.png?ex=68ff3331&is=68fde1b1&hm=a02f60f246b596b36c301be5bca0c8050af89adebfc0217d36b004338397e6a6&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431928910437683323/References_202311152044482.png?ex=68ff3338&is=68fde1b8&hm=9c6066349b2e27e900cb5db1ff33e951d2e4c6ac6db96c7f6eb10348bd2d108a&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431929026657783938/SPOILER_Angelika_sptires_without_background1.png?ex=68ff3353&is=68fde1d3&hm=80e76e2d8fd9874271383d1d9537def6b6e7a5711ba0853885dd03d4feaf5375&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431929054252236830/SPOILER_Angelika_sptires_without_background2.png?ex=68ff335a&is=68fde1da&hm=e29f20845ced9e5b226391f1f2c285d488cd663f17e7033985dafa68ff4d3af2&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1431929080101736548/SPOILER_Angelika_sptires_without_background3.png?ex=68ff3360&is=68fde1e0&hm=4e2276e4488ff4909c8c1933eac87feac8cf9d7c1d99839884af63238abafdb1&"
]

blacklist = ["faggot", "fag", "nigger", "nigga", "trannie", "tranny",
             "negro", "chicano", "chicana", "heil hitler", "cuck", "retard", "nig"]

# handler function to add readbility


def Char_handler(content, name, speech, color, img, img_leng):
    if any(phrase in content for phrase in (blacklist)):
        return
    else:
        embed = embed_func(name, speech, color, img, img_leng)
        return embed

# channeling command


@app_commands.choices(
    charater=[
        app_commands.Choice(name="Lulu", value="lulu"),
        app_commands.Choice(name="Elizabeth", value="liz"),
        app_commands.Choice(name="Agnes", value="agnes"),
        app_commands.Choice(name="Céline", value="celine"),
        app_commands.Choice(name="Maeve", value="maeve"),
        app_commands.Choice(name="Jade", value="jade"),
        app_commands.Choice(name="Arthur", value="arthur"),
        app_commands.Choice(name="Annie", value="annie"),
        app_commands.Choice(name="Lilith", value="lily"),
        app_commands.Choice(name="Angelika", value="angel"),
    ]
)
@bot.tree.command(name="channel", description="Speak their tounge", guild=GUILD_ID)
async def channel(interaction: discord.Interaction, charater: app_commands.Choice[str], speech: str):
    await interaction.response.send_message("Working on it...", ephemeral=True)

    content = speech.lower()

    if charater.value == "lulu":
        embed = Char_handler(content, "Luna K. Lutz - <:lu_khu:971274776993730611>",
                             speech, 0x8B463C, lulu_pics, 5)
    elif charater.value == "liz":
        embed = Char_handler(content, "Elizabeth - <:el_dafuk:971938013775036458>",
                             speech, 0x7084B1, liz_pics, 5)
    elif charater.value == "agnes":
        embed = Char_handler(content, "Agnes - <:ag_what:1139410327411372082>",
                             speech, 0xA59FAA, agnes_pics, 7)
    elif charater.value == "celine":
        embed = Char_handler(content, "Céline - <:ce_yeps:1177389031055700128>",
                             speech, 0xA59FAA, celine_pics, 3)
    elif charater.value == "maeve":
        embed = Char_handler(content, "Maeve - <:ma_smile:1285178007761453057>",
                             speech, 0xA59FAA, maeve_pics, 0)
    elif charater.value == "jade":
        embed = Char_handler(content, "Jade - <:ja_happy:972245318269825046>",
                             speech, 0xA59FAA, jade_pics, 0)
    elif charater.value == "arthur":
        embed = Char_handler(content, "Arthur - <:ar_fear:1193115969724350464>",
                             speech, 0xA59FAA, arthur_pics, 0)
    elif charater.value == "annie":
        embed = Char_handler(content, "Annie - <:an_wawawa:971938323490799678>",
                             speech, 0xA59FAA, annie_pics, 0)
    elif charater.value == "lily":
        embed = Char_handler(content, "Lilith - <:li_happy:1430168122626801795>",
                             speech, 0xA59FAA, lily_pics, 0)
    elif charater.value == "angel":
        embed = Char_handler(content, "Angelika - <:ang_uhh:972250143254536212>",
                             speech, 0xA59FAA, angel_pics, 4)

    await interaction.channel.send(embed=embed)

sayings = [
    'I dunno! Maybe just wait a bit!',
    'That\'s a very unique question! I\'m sure a thousand people haven\'t asked that already!',
    'Try being patient bitch!',
    'Itchers be like "when update" my witch in magic it\'s out when it\'s out!',
    'Me when."',
    'Dumbidiotsaywhenupdate?',
    'You just got one! Be patient, bitch!',
    'Seriously?',
    'I dunno! You tell me!',
    'Who knows!',
    'uhhhh',
    'I dont know!',
    'Take a really good guess when!']

lulu_language = {
    "hallo lulu": 'Hallo {mention}, ik ben de machtige Lulu!',
    "nihao lulu": '你好你好 {mention}，我絕對是真的 Lulu, 哈哈哈!',
    "bonjour lulu": "Bonjour {mention}, C'est moi Lulu!",
    "hola lulu": 'Jajaja! Hola {mention}! Me llamos La Lulu!',
    "ciao lulu": "Salve a {mention}! Sono la grande Lulú, Strega dell'Altopiano!",
    "ave lulu": 'Ave {mention}! Ego fabulosa magus Lulu! Cogito ergo sum.',
    "konnichiwa lulu": 'こんにちは {mention}! 私は史上最高の魔女ルルです!',
    "witam lulu": 'Khu khu khu! Witaj {mention}! Oto ja, Lulu!',
    "kumusta lulu": 'Bati ni {mention}! Ako si Lulu ang dakilang banal na mangkukulam, kumusta ka na?',
}

# reaction messages

char_library = {
    "lulu": {
        "name": "Luna K. Lutz - <:lu_khu:971274776993730611>",
        "color": 0x8B463C,
        "img": lulu_pics,
        "pic_leng": 5,
        "greet": [
            "Salutations friend, I am definitely Lulu!",
            "Khu khu khu! Hello {mention}! It is I!",
            "That's me! Hi {mention}"
        ]
    },
    "elizabeth": {
        "name": "Elizabeth - <:el_dafuk:971938013775036458>",
        "color": 0x7084B1,
        "img": liz_pics,
        "pic_leng": 5,
        "greet": [
            "hey..."
        ]
    },
    "agnes": {
        "name": "Agnes - <:ag_what:1139410327411372082>",
        "color": 0xA59FAA,
        "img": agnes_pics,
        "pic_leng": 7,
        "greet": []
    },
    "celine": {
        "name": "Céline - <:ce_yeps:1177389031055700128>",
        "color": 0xA59FAA,
        "img": celine_pics,
        "pic_leng": 3,
        "greet": []
    },
    "maeve": {
        "name": "Maeve - <:ma_smile:1285178007761453057>",
        "color": 0xA59FAA,
        "img": maeve_pics,
        "pic_leng": 0,
        "greet": [
            "Hello Dear",
            "Hello young-one. How may I help you?"
            "Oh! Hello, {mention}. You called for me?"
        ]
    },
    "jade": {
        "name": "Jade - <:ja_happy:972245318269825046>",
        "color": 0xA59FAA,
        "img": jade_pics,
        "pic_leng": 0,
        "greet": []
    },
    "arthur": {
        "name": "Arthur - <:ar_fear:1193115969724350464>",
        "color": 0xA59FAA,
        "img": arthur_pics,
        "pic_leng": 0,
        "greet": []
    },
    "annie": {
        "name": "Annie - <:an_wawawa:971938323490799678>",
        "color": 0xA59FAA,
        "img": annie_pics,
        "pic_leng": 0,
        "greet": []
    },
    "lilith": {
        "name": "Lilith - <:li_happy:1430168122626801795>",
        "color": 0xA59FAA,
        "img": lily_pics,
        "pic_leng": 0,
        "greet": []
    },
    "angelika": {
        "name": "Angelika - <:ang_uhh:972250143254536212>",
        "color": 0xA59FAA,
        "img": angel_pics,
        "pic_leng": 4,
        "greet": []
    }
}


listen = ("hi", "haii", "hey", "heya", "how are you", "hello", "howdy")
char_listen = ("lulu", "elizabeth", "agnes", "celine", "maeve",
               "jade", "arthur", "annie", "lilith", "angelika")

special_name = ("liz", "aggy", "ann", "lily", "angel")


def response(content, msg):
    if any(phrase in content for phrase in (listen)):
        for name in char_listen:
            if name in content:
                color = char_library[name]["color"]
                picture = char_library[name]["img"]
                length = char_library[name]["pic_leng"]
                greetings = char_library[name]["greet"]
                embed = embed_func(name.capitalize(), greetings[random.randint(0, 2)].format(
                    mention=msg.author.mention), color, picture, length)
                return embed


def lulu_response(content, msg):
    if any(phrase in content for phrase in (lulu_language)):
        for lang in lulu_language:
            if lang in content:
                embed = embed_func("Luna K. Lutz - <:lu_khu:971274776993730611>",
                                   lulu_language[lang].format(mention=msg.author.mention), 0x8B463C, lulu_pics, 5)
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



