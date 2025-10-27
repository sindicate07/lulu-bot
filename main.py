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
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432278122476077146/IMG_54311.png?ex=69007872&is=68ff26f2&hm=bee3ae7852ea795017c7d68f312cfcdd8f72d31870ed69e9b0625a5d1ef8382c&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432278122820276244/IMG_54312.png?ex=69007872&is=68ff26f2&hm=0477a310c0530089ba1044b937c7f7c7c2d3ca709f0ec6d8d8b1b7c7958b8d8e&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432278123151364096/SPOILER_Maeve_sprites_backgroundless1.png?ex=69007873&is=68ff26f3&hm=a6fd1dedec44069ab38410fe36008348225ac0125246164a054e8cbe6b60c172&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432278123491229706/SPOILER_Maeve_sprites_backgroundless2.png?ex=69007873&is=68ff26f3&hm=3692cd8c31d4ed9695ab825da5e50aace6f735b4387931ddbf8de092984032a5&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432278123814064180/SPOILER_Maeve_sprites_backgroundless3.png?ex=69007873&is=68ff26f3&hm=c2ccd768dfdc813611131cefbcda897e5bc6235bed1ffba921c2f881774bd50e&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432278124158128209/SPOILER_Maeve_sprites_backgroundless4.png?ex=69007873&is=68ff26f3&hm=cbb3609dbe519c65f207f461f18162f72c85fbc25b127eb15592f4963ed5db64&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432278124758040636/SPOILER_Maeve_sprites_backgroundless5.png?ex=69007873&is=68ff26f3&hm=9c854781a326b9a64233d6d22d7e8896692d09f6504eb62f11b4d220d593c190&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432278125139726437/SPOILER_Maeve_sprites_backgroundless6.png?ex=69007873&is=68ff26f3&hm=45f3bfed8be8206587c6d7ab8c92dd906a1f54e7dcb3aaba6a3c5ce88d07dc0a&"
]
jade_pics = [
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282571529519114/SPOILER_jade_sprites_blank1.png?ex=69007c97&is=68ff2b17&hm=b984335d9944ce8eec74ce8b8247e7fd77287ad59333699cf410c9955b2bb87c&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282571881971723/SPOILER_jade_sprites_blank2.png?ex=69007c97&is=68ff2b17&hm=07159c1a7bfa347452153678ad2eb35f02d3b9c0824c43ac5edfd2bed169e66a&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282572267982910/SPOILER_jade_sprites_blank3.png?ex=69007c97&is=68ff2b17&hm=81d4486006dc1a9ef802f8edef8485889164c72a8070958b186a16f360da5917&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282572762775613/SPOILER_jade_sprites_blank4.png?ex=69007c97&is=68ff2b17&hm=3e96cf2bb30d61d49a32578726881be6d22ab8ddc4fff1256f0995b4383be029&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282573236736041/SPOILER_jade_sprites_blank5.png?ex=69007c97&is=68ff2b17&hm=fc78a0f7681163f8b995177a8dd11324843de5ab60fa5867f642997f8699492e&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282573588926495/SPOILER_jade_sprites_blank6.png?ex=69007c98&is=68ff2b18&hm=03e849b00b575bad8bcea5f291c1955ab745f5484cac6062124004cae835bad6&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282574008488028/SPOILER_jade_sprites_blank7.png?ex=69007c98&is=68ff2b18&hm=b8203ae1f56217f8675e4f464f2dfef4bb8d9d89c586617fae8c31d15782046f&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282574398427156/SPOILER_jade_sprites_blank8.png?ex=69007c98&is=68ff2b18&hm=ce6667ded3d10e86fd13d377229ebcf54dbfe7055a5b76ff20a45ecdcad6e8ed&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282574805270640/SPOILER_jade_sprites_blank9.png?ex=69007c98&is=68ff2b18&hm=d3404f9cfb1c0c34d14c35b3ab817f73bcdfe3860cbc457cc5682f5abfe3fbb3&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432282575187218562/SPOILER_jade_sprites_blank10.png?ex=69007c98&is=68ff2b18&hm=7db9095904ea5010c95f629112b637b93bb2149a2bcb48c1fb9f9a671c2cf70a&"
]
arthur_pics = [
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432286230317371402/mc_og_cross1.png?ex=69007fff&is=68ff2e7f&hm=f2e0d785aa8416bf45fb978a19f058cedcadbb5ac69bda04eb88393e66cbabed&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432286230929739866/mc_og_wand11.png?ex=69008000&is=68ff2e80&hm=0f37427e3db1a4b6a4c580d324b460776e74e09ad0b88026561ddc1709dea1cb&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432286231475126283/References_202311061619231.png?ex=69008000&is=68ff2e80&hm=d20b4af5e0c3f8bdbdb0e46ace3cb32b546e91f311c906aae413a95d5a2cc01a&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432286231969927209/References_202311061619232.png?ex=69008000&is=68ff2e80&hm=b9ffa0ea208847bcf2a7b307d54cad718c5c95de3330428b1ce06a4e63ada62d&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432286232381095976/References_202311061619233.png?ex=69008000&is=68ff2e80&hm=549bbef1b41b174862ce0f2e14f5d6cca676a6b5a4a8e4bfb00f256555788526&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432286232766844989/References_202311061619234.png?ex=69008000&is=68ff2e80&hm=f9075898392aad4d7ebba5b7903c6c4edb252ce5c095f9fac662ac7bf65e785d&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432286233207508993/References_202311061619235.png?ex=69008000&is=68ff2e80&hm=5a6c27eef7fe65d018458e2773f66ffdd42207b49f617e57f41d44f6c64b2de3&"
]
annie_pics = [
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290438542266439/annie_elf_og_fingers1.png?ex=690083eb&is=68ff326b&hm=4047511471fc9ac322ba6831ca4bd1f1fe27f9d048e669f5a4cacead845f0f4c&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290439095910501/annie_succ_og_fingers1.png?ex=690083eb&is=68ff326b&hm=b054231ede02c8450395a2ea632cb5efa03be6da44840021f1cc538495133854&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290439511408722/annie_succ_og_normal1.png?ex=690083eb&is=68ff326b&hm=e75aebb777f07e11df563b5dc956e0407f8307f5408e60e4c3403af152fb5bf1&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290440476102686/AnnieSpriteSheet_11.png?ex=690083eb&is=68ff326b&hm=27929a9c990f5247c34d13b3ea081783a0a12b37cdcd07169533e7371740e6db&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290441314959370/AnnieSpriteSheet_12.png?ex=690083eb&is=68ff326b&hm=5ca157d42d823f1e93e5557130ce64502474eea18d4726527e7dbf80fcaacdf4&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290442044506163/AnnieSpriteSheet_13.png?ex=690083ec&is=68ff326c&hm=2504a1b3dd291433f3c23a62b3701f004da11c399535b1141f5c990c7b42d050&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290442463940708/AnnieSpriteSheet_14.png?ex=690083ec&is=68ff326c&hm=df7b52a012e048e08d7737451d80be193d7505d26423e155ca5191b62035a23a&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290442837495949/SPOILER_Annie_sprites_no_background1.png?ex=690083ec&is=68ff326c&hm=18e87d27f2450ffd77b114bf3b4535427b938012cf51ec078f91e34dbbe2a372&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290443214852096/SPOILER_Annie_sprites_no_background2.png?ex=690083ec&is=68ff326c&hm=25033aa4347eb4b6ece8c661386e6579876af55203c9e770f183726a3eb8d08a&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290443592470608/SPOILER_Annie_sprites_no_background3.png?ex=690083ec&is=68ff326c&hm=98a609625bfff9b7742afa330a38e03e77dbe707c24e2caae58d7d98b4f122da&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290541630001226/SPOILER_Annie_sprites_no_background4.png?ex=69008403&is=68ff3283&hm=0b946919d286dab4719345ffd68ff63dca158a98e08376a90ed36ee88d55f24e&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290541957287997/SPOILER_Annie_sprites_no_background5.png?ex=69008403&is=68ff3283&hm=6bb1b4d8b368e3061ef0e6eb0831ab1b018479f69cc0703e642cfd7a19ee63d5&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432290542284177461/SPOILER_Annie_sprites_no_background6.png?ex=69008403&is=68ff3283&hm=cf03deea38ea0334612fa3f38e9b5353bc089701f593476db64121b49f8ffd95&"
]
lily_pics = [
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298033151873034/lilith_og_11.png?ex=69008afd&is=68ff397d&hm=cd8ab18b3041ac8c10f8bddf5c4c673cdc259790941e7e9b5952d74f8a33026f&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298033516773466/IMG_54313.png?ex=69008afe&is=68ff397e&hm=56786b3d498c3d01d72a9217b0fcf016243dcbebb960f408c10cb9a54f3618bd&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298033940402226/IMG_54314.png?ex=69008afe&is=68ff397e&hm=e29426b25a37f6514d5022e95fa41bbc438e7ddd7ca35b6eb6d6e85e02578e8d&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298407493636126/SPOILER_lilith_sprites_v051.png?ex=69008b57&is=68ff39d7&hm=6592a5694598c2d8a9536e89bd2b457ed231aff72017f26103cc2e9cfd0bdee1&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298407938228224/SPOILER_lilith_sprites_v052.png?ex=69008b57&is=68ff39d7&hm=865ade05726615d18f60493e47fa76540fd2c1cb29e56074a41015224d7666e2&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298408395411486/SPOILER_lilith_sprites_v053.png?ex=69008b57&is=68ff39d7&hm=f7c792bc547bb48c2b58337b19ea75a4d5d2dcd7e6c37b7fa873f1433ece9f1d&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298408747601970/SPOILER_lilith_sprites_v054.png?ex=69008b57&is=68ff39d7&hm=836ecc08ab972f0ae410250e9b8fdbd738e94a62946188651378a83f8564c324&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298409200451686/SPOILER_lilith_sprites_v055.png?ex=69008b57&is=68ff39d7&hm=5e2a18dc505293de699a7f29ade20ebf177894e2c836949da8ce04dc7e6ce6bc&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298409632469062/SPOILER_lilith_sprites_v056.png?ex=69008b57&is=68ff39d7&hm=43e6fc45c1fb5ebf93a375eceb1bdf26efa2af4993b4bb9177b30b3d5c94252c&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298410068672552/SPOILER_lilith_sprites_v057.png?ex=69008b57&is=68ff39d7&hm=7a8b1b66d5615fa5e2c7f631e044ff823d8f623f51092d98cfb69055cccf5ffe&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298410412736694/SPOILER_lilith_sprites_v058.png?ex=69008b57&is=68ff39d7&hm=c42bbb1f996087e07b5408836ab4af1a92b33028a7f215dc5b443551b9d65c23&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298410714857512/SPOILER_lilith_sprites_v059.png?ex=69008b57&is=68ff39d7&hm=9cdc1cd1640657476d890a68ba0bb24226bbd9e11edcd8b9036b16825098fa81&",
    "https://cdn.discordapp.com/attachments/1315241130631237682/1432298411079635024/SPOILER_lilith_sprites_v0510.png?ex=69008b58&is=68ff39d8&hm=e96ac67334f41525e686aafa1c6db93cdb407a3569929a657931fe922c13cae1&"
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
                             speech, 0x21686A, celine_pics, 3)
    elif charater.value == "maeve":
        embed = Char_handler(content, "Maeve - <:ma_smile:1285178007761453057>",
                             speech, 0x4C2F35, maeve_pics, 7)
    elif charater.value == "jade":
        embed = Char_handler(content, "Jade - <:ja_happy:972245318269825046>",
                             speech, 0x8E624D, jade_pics, 9)
    elif charater.value == "arthur":
        embed = Char_handler(content, "Arthur - <:ar_fear:1193115969724350464>",
                             speech, 0x291B1C, arthur_pics, 6)
    elif charater.value == "annie":
        embed = Char_handler(content, "Annie - <:an_wawawa:971938323490799678>",
                             speech, 0xFF2E72, annie_pics, 12)
    elif charater.value == "lily":
        embed = Char_handler(content, "Lilith - <:li_happy:1430168122626801795>",
                             speech, 0xEAE2CE, lily_pics, 12)
    elif charater.value == "angel":
        embed = Char_handler(content, "Angelika - <:ang_uhh:972250143254536212>",
                             speech, 0x262B42, angel_pics, 4)

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
        "color": 0x21686A,
        "img": celine_pics,
        "pic_leng": 3,
        "greet": []
    },
    "maeve": {
        "name": "Maeve - <:ma_smile:1285178007761453057>",
        "color": 0x4C2F35,
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
        "color": 0x8E624D,
        "img": jade_pics,
        "pic_leng": 0,
        "greet": []
    },
    "arthur": {
        "name": "Arthur - <:ar_fear:1193115969724350464>",
        "color": 0x291B1C,
        "img": arthur_pics,
        "pic_leng": 0,
        "greet": []
    },
    "annie": {
        "name": "Annie - <:an_wawawa:971938323490799678>",
        "color": 0xFF2E72,
        "img": annie_pics,
        "pic_leng": 0,
        "greet": []
    },
    "lilith": {
        "name": "Lilith - <:li_happy:1430168122626801795>",
        "color": 0xEAE2CE,
        "img": lily_pics,
        "pic_leng": 0,
        "greet": []
    },
    "angelika": {
        "name": "Angelika - <:ang_uhh:972250143254536212>",
        "color": 0x262B42,
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




