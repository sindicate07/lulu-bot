# grab pictures
import random
import pics

lulu_pics = pics.lulu_pics
liz_pics = pics.liz_pics
agnes_pics = pics.agnes_pics
celine_pics = pics.celine_pics
maeve_pics = pics.maeve_pics
jade_pics = pics.jade_pics
arthur_pics = pics.arthur_pics
annie_pics = pics.annie_pics
lily_pics = pics.lily_pics
angel_pics = pics.angel_pics
dahlia_pics = pics.dahlia_pics
elena_pics = pics.elena_pics
molly_pics = pics.molly_pics
loveliz_pics = pics.loveliz_pics
starliz_pics = pics.starliz_pics
elvira_pics = pics.elvira_pics

# character dialouge
char_library = {
    "lulu": {"name": "Luna K. Lutz - <:lu_khu:971274776993730611>", "color": 0x8B463C, "img": lulu_pics, "pic_leng": 5, "greet": [
        "Salutations friend, I am definitely Lulu!",
        "Khu khu khu! Hello {mention}! It is I!",
        "That's me! Hi {mention}",
        "Miss {mention}! Good to see you!",
        "Hey! Dear classmates! How are you?",
        "Bwa! G-Good Day!",
        "Oh, what is it, My dear companion?",
        "Miss {mention}! Good day!",
        "Greetings, Miss {mention}.",
        "Greetings... again!"
    ], "bye": [
        "See you soon, Miss {mention}!",
        "I shall retire to my humble abode. You are welcomed in...anytime.",
        "Khu khu, Good day Miss {mention}.",
        "Farewell, Miss {mention}!"
    ], "nick": [
        "D-DONT CALL ME BY THAT NAME, PLEASE!",
        "Th-There was no need to call me that!"
    ], "updt": [
        "I dunno! Maybe just wait a bit!",
        "Me when.",
        "I dunno! You tell me!",
        "Who knows!",
        "Khu, khu, khu! Only I know because of my all seeing eye! And I won't tell you!",
        "I don't know.",
        "Maybe Miss Jade knows!",
        "Maybe Miss Elizabeth knows!",
        "Maybe Miss Arthur knows!",
        "Maybe Miss Maeve knows!",
        "Maybe Miss Lilith knows!",
        "Maybe Miss Angelika knows!",
        "Maybe Miss Agnes knows!"
    ]
    },
    "elizabeth": {"name": "Elizabeth - <:el_dafuk:971938013775036458>", "color": 0x7084B1, "img": liz_pics, "pic_leng": 8, "greet": [
        "What.",
        "Did you need something?",
        "Could you not bother me?",
        "I don't have time for you.",
        "What do you want?! And you better sum in up in less than 50 characters!",
        "As you can see, I'm busy.",
        "Yeah, yeah, yeah. Save it.",
        "What does a milk-drinking witch like you want from me?"
    ], "bye": [
        "...",
        "Thank you.",
        "...Bye.",
        "Right.",
        "Have a good day yourself."
    ], "nick": [
        "What in the actual stars did you call me?",
        "Call me that name and it will be the last time you say it.",
        "Excuse me?",
        "Say it again... I dare you.",
        "...",
        "You better address me properly!",
        "Shut up! I solo your favorite verse!",
        "You mule! What did you just call me?!",
        "This milk drinking witch... The audacity!"
    ], "updt": [
        "That\'s a very unique question! I\'m sure a thousand people haven\'t asked that already!",
        "Seriously?",
        "How stupid can you be?",
        "Keep going...",
        "Can you say anything else?",
        "Can you cut it out?",
        "Just shut up already!",
        "Oh my stars. Anything new that comes out of your mouth?",
        "Shut up! I solo your favorite verse!"
    ]
    },
    "agnes": {"name": "Agnes - <:ag_what:1139410327411372082>", "color": 0xA59FAA, "img": agnes_pics, "pic_leng": 7, "greet": [
        "Away with you.",
        "Leave this server. And you better do it now. I know what you are. I can see through your disguise",
        "No refunds.",
        "Are you buying something?",
        "What do you want from my store!?",
        "Wanna purchase some Tlacuawls noses?",
        "are you here to buy something? Or are you up to something else?",
        "What do you want?",
        "Hello."
    ], "bye": [
        "Hm. Pleasure doing business with you!",
        "Goodbye.",
        "Bye.",
        "You better purchase something next time.",
        "Come again... with more money."
    ], "nick": [
        "Get out.",
        "Do you want me to set you ablaze? Perhaps tied up? Maybe I should-(maybe we shouldn't finish the rest)",
        "Grrrr... Get out. Now!"
    ], "updt": [
        "Try being patient bitch!",
        "You just got one! Be patient, bitch!",
        "You keep rambling on and I'll put a curse on you!",
        "Your nonsense can be taken anywhere but here",
        "Get out. Now.",
        "I'll tell you if you'll be my one and only."
    ], "teach": [
        "Come on kiddo. Make me a potion so I can go home already.",
        "Why don't you try making that explosion potion again?",
        "They told me to cover for today. Why dont you make a sleeping potion?",
        "Alright you punks. Make me a potion. Any will do.",
        "Ah, for today's homework. Err... A demon repellent is due by the end of tommorow. Good luck!",
        "Great... Maeve asked me to teach you morons again. Out of curtesy, a antidote is due by the end of today.",
        "Yeah, yeah. You know the drill you brat. Make me anything. I got places to be today.",
        "I wonder if you guys can brew wine...?",
        "Make something useful for today, so I can put it up for sale."
    ], "failed": [
        "Ugh... I dont even know why I bother.",
        "Good job! Now make me another. <:ag_what:1139410327411372082>",
        "You ##### ####### #####!",
        "Seriously? This is the best that Maeve's students have to offer?",
        "You bring us witches to shame. Try again.",
        "Wow. You made a absolute mess! Great job.",
        "...",
        "I dont get payed enough for your failures. Try again.",
        "Mess up again and I'm going to curse you!"
    ]
    },
    "celine": {"name": "Céline - <:ce_yeps:1177389031055700128>", "color": 0x21686A, "img": celine_pics, "pic_leng": 16, "greet": [
        "Can you keep a secret?",
        "Wanna be my test subject?",
        "Hey, my dear test subject.",
        "I need a guine pig. Do you want to be one?",
        "Hello, Miss {mention}. Want to participate in my experiments?",
        "Oh my. Did you hurt yourself?",
        "How are you, {mention}? Are you feeling sick?",
        "Ah, my test subject! Greetings."
    ], "bye": [
        "Have a nicey-wonderful daaaaay!",
        "Stop by my office next time!",
        "Do come back! I need to conduct some more experiments on you.",
        "Rest well! After all, I need my dear test subject to be healthy."
    ], "nick": [
        "It's never lupus.",
        "It's not lupus."
    ], "updt": [
        "Take a really good guess when!",
        "Perhaps in a couple of months! developing technology isn't as easy as it seems.",
        "It's statistically unlikely that it will come out soon",
        "Hmmm... maybe after my studies, I can look into it for you.",
        "Currently working on it... do give us some more time!",
        "Hey MollyBot, When is it coming? ...MollyBot?"
    ], "teach": [
        "Hey, why don't you try making a healing potion? That would be very helpful!",
        "You could use my ingredient mixer, XI0021, to make your potions easier.",
        "Could you make me a potion I can use on Ar- my gui- test subject?",
        "I will be developing potions alongside you guys today! Be sure to reel in some results!",
        "They asked me to cover today's potion mixing lesson. How about we make some potions that make you drowsy?",
        "I will be examining your guys' technique with handling dangerous substances! Maeve doesn't want you guys getting hurt so... Be careful!",
        "Mmm... Mhm... Ah...! I want 15 potions done by today. How does that sound everyone?",
        "Maeve said no machinery so we have to do this the old fashioned way. Obviously I already premade mine. If you can match it's color, you pass!"
    ], "failed": [
        "What a disaster! Luckily the classroom didn't blow up!",
        "Aww, don't worry about messing up. I mess up my potions all the time too.",
        "You can always try again!",
        "So close. Come on, I need that potion for my tests!",
        "Nice attempt. I would suggest using the other ingredent for that mix.",
        "Just a couple adjustments and you be good!",
        "Hmm... I should take notes on how badly you messed up.",
        "And the desk is on fire... Moll- Err... Let me find some water.",
        "Careful, that mixture could melt your skin!",
        "Careful, that mixture could blow up!",
        "Careful, that mixture could create toxic fumes that can cause you to asphyxiate!",
        "Careful, that mixture could... Wait, that is new! I must study this reaction!",
        "Careful, that mixture could kill you if you're not careful about handeling!"
    ]
    },
    "maeve": {"name": "Maeve - <:ma_smile:1285178007761453057>", "color": 0x4C2F35, "img": maeve_pics, "pic_leng": 7, "greet": [
        "Hello Dear",
        "Hello young-one. How may I help you?",
        "Oh! Hello, {mention}. You called for me?",
        "Oh, Mister {mention}? How are you? Behaving yourself, I hope.",
        "You know, around here it is said that those who lie to your elders shall be cursed with the banana curse. The more you lie, the more chances you have to comically fall due to a banana peel.",
        "Good day, dear student of mine!",
        "What is it that troubles you, darling?"
    ], "bye": [
        "Good night, my dear student.",
        "Bu-bye!",
        "Oh {mnetion}, please take care!",
        "Miss {mention}. Do keep up with your studies.",
        "Be on your best behavior!"
    ], "updt": [
        "Oh young one! you must be patient!",
        "Oh my, are you that excited? Well you'll have to wait just a little bit longer, okay?",
        "I've asked Céline and it seems like she is still working hard at it.",
        "Our hands are full right now, dear. Do give us more time. Thank you.",
        "Good news! It is being worked on!"
    ], "teach": [
        "Miss Lilith is out sick for today and I will be covering today's lesson. Let's get started with the basics. Growth potions for plants!",
        "Today I will be covering for Miss Lilith and rather than staying in all day, how about we all forge materials potions?",
        "Ah, a potion that promotes body wellness would be nice. Maybe something for strength recovery.",
        "Celine! Please put that away! We talked about this, I can't have the students relying on such things.",
        "Hmm... It says here you can make a love potion. Interesting... Anyways lets continue with the lesson.",
        "Good day, young ones! How about another potion mixing lesson?",
        "Maybe you guys can suprise me today with a potion you came up with! I will be here all day."
    ], "failed": [
        "O-Oh... It's okay young one. We all mess up here and there.",
        "Ah. It's okay. You can always remake it!",
        "Err... I'm not sure why that happened. You could try a different mix!",
        "GAH! STAY CALM! I WILL CONTROL THIS FIRE!",
        "Sigh... Where are you when I need you Lilith...",
        "Oh. Im sure it will be fine right?",
        "Careful!! Celine told me that it can explode in your face!",
        "Ah. It's okay. After all, it is a learning curve.",
        "Hmm... Lets check the textbook to see what went wrong.",
        "That is definitely, not a potion...",
        "Mmm... I failed you as a teacher..."
    ]
    },
    "jade": {"name": "Jade - <:ja_happy:972245318269825046>", "color": 0x8E624D, "img": jade_pics, "pic_leng": 9, "greet": [
        "Hey {mention}! you're here!",
        "Miss {mention}! Good day!",
        "{mention}! It was about time you dropped by!",
        "What's up? Dp you need something?",
        "Hi, {mention}! How are you doing?",
        "{mention}! Good to see you again. Did you need something?",
        "Oh, {mention}! Hi there!"
    ], "bye": [
        "See you at classes, {mention}! Buh-bye!",
        "Always! Good day!",
        "Good day.",
        "{mention}, See you around!",
        "Bored already? Just kidding! See you!"
    ], "nick": [
        "Ehehe.",
        "Aww, thank you!"
    ],  "updt": [
        "Dumbidiotsaywhenupdate?",
        "I dont know!",
        "Hmmm. Maybe next month if we're lucky!",
        "I don't know... maybe Maeve or Lilith might know a thing or two!",
        "Something tells me that it will be next week! or the week after!",
        "Im not sure... But I could bake you a cake if that can cheer you up!",
        "Who knows. Maybe it might be my turn to shine next update? whaddya think?",
        "I wonder if Arthur knows anything..."
    ]
    },
    "arthur": {"name": "Arthur - <:ar_fear:1193115969724350464>", "color": 0x291B1C, "img": arthur_pics, "pic_leng": 6, "greet": [
        "Miss {mention}?",
        "Hey, {mention}. Good evening.",
        "Good morning, Miss {mention}. How are you?",
        "Greetings, ma'am.",
        "Hello Miss {mention}. Could I help you with anything?"
    ], "bye": [
        "Have a wonderful day, Miss {mention}.",
        "Bye. {mention}.",
        "Good day, Miss {mention}.",
        "Good day.",
        "Take care of yourself, Miss. Okay?"
    ], "nick": [
        "Haha. Thank you.",
        "Aww shucks. Really?",
        "Well, I try my best!",
        "<:ar_fear:1193115969724350464>"
    ], "updt": [
        "Itchers be like \"when update\" my witch in magic it\'s out when it\'s out!",
        "uhhhh",
        "If I think about it really hard...",
        "Hmm... Well personally I don't mind waiting. It will come when it comes right?",
        "Maybe they're testing us! After all they want us to be in good behavior.",
        "I heard it's coming out in a couple of months. No promises though.",
        "I wonder if Jade knows anything..."
    ]
    },
    "annie": {"name": "Annie - <:an_wawawa:971938323490799678>", "color": 0xFF2E72, "img": annie_pics, "pic_leng": 12, "greet": [
        "...",
        "I-I-I-I-A-A-ANNIE! C-C-C-C-C-CAKE! B-B-B-B-BROOM!",
        "Eep!",
        "D-D-Do you need something?",
        "H-Hello, {mention}! I'm um, fine... Maybe a little bit hungry.",
        "H-H-Hi..."
    ], "bye": [
        "B-Bye...",
        "Oh... uhm, bye {mention}.",
        "G-Good day... {mention}.",
        "*Bye.*"
    ], "nick": [
        "Oh...",
        "Ah!..."
    ], "updt": [
        "Err...",
        "Eep!",
        "I-Im not too sure...",
        "U-U-U-U-U-UPDATE???",
        "Uh....",
        "Uhm..."
    ]
    },
    "lilith": {"name": "Lilith - <:li_happy:1430168122626801795>", "color": 0xEAE2CE, "img": lily_pics, "pic_leng": 12, "greet": [
        "Good day, {mention}.",
        "Uhm... Why would be talk? I'm just your teacher.",
        "What is it that you want?",
        "Hey kid.",
        "Yes? You needed something?",
        "How is the homework? Did you need help?",
        "What's up, kid? Elizabeth still causing trouble?"
    ], "bye": [
        "Good day, {mention}.",
        "Remember your homework for tonight. That is all.",
        "Goodbye {mention}.",
        "Do ask your humble teacher for advice or anything else.",
        "Zzz......Zzz......",
        "Do behave while you're away."
    ], "nick": [
        "Excuse you. But please adress me properly.",
        "It's Miss Lilith to you, young lady.",
        "I'm too tired to deal with you right now."
    ], "updt": [
        "Listen kid. I already have a lot on my plate. You could ask around, but im busy as of right now.",
        "Try being a bit more patient. Thank you.",
        "If I knew, I would have let you guys know.",
        "Maybe you should focus on your homework rather than things that will come soon.",
        "{mention}, I really don't know what to tell you, but I'm sure they're trying their best."
    ], "teach": [
        "Okay class, simple day. Basics into potion mixing. Just toss in these ingredients and we'll go from there.",
        "Good day class. Let's dive into intermediate studies of potions. Flip through the text book till you find...",
        "If you're feeling confident, do touch on the advanced concepts of potion making. Just don't blow up the place please. Thank you.",
        "uuuaahhhhh... Excuse me. Maybe a sleeping potion would be nice.",
        "...And don't forget what I asked you to make for homework.....Zzz...",
        "Today is a free day. Just turn in a viable product to get points.",
        "Today you will be making a potion that makes you giggle. It should be a fun day, right?",
        "You want to make something? Look, all I ask is that you don't burn the classroom down."
    ], "failed": [
        "I failed you as your teacher...",
        "Close. You would need the other one for that mixture.",
        "Did they not teach you guys anything?",
        "Come on Lilith, you can do this. Let's try a diffrent approch instead.",
        "Did you follow the textbook? Or was my instructions unclear?! Let me try to clarify anything confusing you.",
        "Lucky for you, this didn't go up in flames. Lulu on the other hand...",
        "...Zzz......Oh, what happened? Ah, you can just try again.",
        "You can always try again, it's not the end of the world. But, Miss Elizabeth thinks otherwise.",
        "If you need extra help you can always ask me. After all I am your teacher.",
        "Oh Maeve. What am I going to do...",
        "I tried... But I'll keep trying to help you guys, no matter what.",
        "Close enough... I'll just give you credit this time."
    ]
    },
    "angelika": {"name": "Angelika - <:ang_uhh:972250143254536212>", "color": 0x262B42, "img": angel_pics, "pic_leng": 4, "greet": [
        "Greetings {mention}, How can I help you?",
        "Miss {mention}, You called for me?",
        "Good day, Miss {mention}. What is it that you need my assistance for?",
        "Oh, Miss {mention}. Good evening. Is everything ok? Is there anything I can be of service?",
        "At your service."
    ], "bye": [
        "To you as well, Miss {mention}.",
        "I shall leave to fufill the rest of my duties.",
        "Good day, young one.",
        "Have a good afternoon, young {mention}."
    ], "nick": [
        "?",
        "That's new.",
        "Excuse you."
    ], "updt": [
        "Curious. Well, I think they're working as fast as they can.",
        "Im not to sure. But aleast Hatchet's room is nice and tidy. Would you like me to clean yours too?",
        "Unfortunately, this is one of the things I can't help you with. My apologies."
    ]
    },
    "dahlia": {"name": "Dahlia - <:da_panic:1285172600502353991>", "color": 0x792039, "img": dahlia_pics, "pic_leng": 5, "greet": [
        "Greetings, my lady. What brings you here with me?",
        "Ah, my lady. Did you want to purchase some clothing?",
        "Oh my! You're attire is tarnished! Let me repair it at once!",
        "Do you also want to greet my darlings too? They look happy to see you."
    ], "bye": [
        "Come by for your tailoring needs.",
        "Come again.",
        "Miss {mention}, Come again."
    ], "updt": [
        "It's an art. It takes time to procure such a masterpiece. Maybe if you took the time to create something, you would understand too.",
        "Mhm... My darlings just told me that it will take a few more months.",
        "Hmm... Well if I rushed and did a sloppy job on your garments, you wouldn't be too happy would you?",
        "It needs to be refined and elegant, Just like my work. And with that, It will take awhile."
    ]
    },
    "elena": {"name": "Elena - <:ele_amet:1196910070898888725>", "color": 0xf9c67a, "img": elena_pics, "pic_leng": 5, "greet": [
        "What is it that you seek, young one?",
        "Y-yes, Miss {mention}!?",
        "Did you want to follow the way of the elvish civilization",
        "Would you like to come to the elvish civilization?",
        "Miss {mention}! How joyus to see you here this day! Have you finally decided to come to the elvish civilization",
        "Miss {mention}, there is no need for such savage magic when we have such advanced technologies.",
        "Miss {mention}, would you like to confess your sins to the Goddess of Elves at the Confessional Booth?"
    ], "bye": [
        "E-Eh?? Have I failed in this c-convertion?",
        "Farewell Miss {mention}. Do think about joining us in paradise.",
        "I leave my prayers with you."
    ], "updt": [
        "Seems like our technology has a limit to how fast we could develop it. But do keep your faith as it will be done soon!",
        "With my and your prayers, It shall be done in a timely manner!",
        "I was told the development got backed up at the elvish civilization. Seems like we need a bit longer. This shouldn't worry you though!",
        "Rather than focusing on such meaningless thoughts, perhaps you would like to come to the elvish civilization?"
    ]
    },
    "mollybot": {"name": "MollyBot - <:mollybot:1200692143803617393>", "color": 0xffec9b, "img": molly_pics, "pic_leng": 2, "greet": [
        "A Pleasure, {mention}.",
        "Would You Like A Cookie?",
        "Weird {mention} Equals Lots Of Fun.",
        "Calculating {mention} Charisma... {value} Percent.",
        "Error"
    ], "bye": [
        "Variable Cookie Gift Set To False. The Way Of The Cookie Has Been Lost.",
        "Goodbye, {mention}",
        "Shutting Down...",
        "Error"
    ], "nick": [
        "Such Terms Should Not Be Used",
        "Documenting... Collecting Username... {mention}. On Warning File - Complete",
        "Be Nice",
        "Your Behavior Will Be Noted.",
        "Beware. Offensive Language Will be Punished.",
    ], "updt": [
        "Scanning Multiple Sources... No Data Found For \"Update.\"",
        "Loading...",
        "Data Unavailable.",
        "Update In... {value} Weeks.",
        "Error",
        "The Update Is {value}% Completed.",
        "Playing Voice Recording - \"Perhaps in a couple of months! developing technology isn't as easy as it seems.\"",
        "Playing Voice Recording - \"Take a really good guess when!\"",
        "Playing Voice Recording - \"It's statistically unlikely that it will come out soon\"",
        "Playing Voice Recording - \"Currently working on it... do give us some more time!\"",
        "Playing Voice Recording - \"...\"",
        "Playing Voice Recording - Failed To Retrieve Data.",
    ]
    },
    "lovestruck elizabeth": {"name": "Lovestruck Elizabeth - <:love_liz:1453638480860156058>", "color": 0x5d1323, "img": loveliz_pics, "pic_leng": 12, "greet": [
        "You're kind of charming, you know.",
        "You're are really cute...",
        "Hello darling.",
        "I was thinking... You wanna do somthing naughty?",
        "We should definitely get a room together sometime.",
        "Have you met my copy?",
        "Mmmm... Keep talking",
        "Hello {mention}♡",
        "Heyy {mention}.",
        "Oh! how are you my sweetheart?",
        "Just who I was looking for!",
        "Did you want to play with me?",
        "Came to see me? I could think of something else you can see ♡",
        "Hey cutie pie ♡"
    ], "bye": [
        "Anytime handsome.",
        "Dont keep me waiting ♡",
        "If you stay I will let you do anything to me!",
        "Aww, leaving so soon?",
        "Aww, I'll miss you ♡",
        "Bye babe! ♡",
        "Next time do less talking. If you know where I'm getting at ♡"
    ], "nick": [
        "Only for you ♡",
        "I kinda like it ♡"
    ], "updt": [
        "Who cares about that update when you have me.",
        "I know something better than some silly update.",
        "Instead about worring about the update, you should be worrying about me!",
        "When are you gonna bang me instead?",
        "Thinking about other girls when I'm right here...",
        "Maybe I could get some \"action\" in the next update huh?"
    ]
    },
    "astrologist elizabeth": {"name": "Astrologist Elizabeth - <:star_liz:1453638454964387941>", "color": 0xe4acb9, "img": starliz_pics, "pic_leng": 13, "greet": [
        "Do you like the stars?",
        "Do you want to see the stars too?",
        "I want to watch the stars with you. Wouldn't that be nice?",
        "Have you met my copy?",
        "Oh! Hello. Would you like to know about Sirius? It's quite a fascinating star!",
        "Want to hear about Capella? If you look up you can spot it flashing diffrenty colors at night!",
        "You know what my favorite star is? It's the one that I'm talking with!",
        "Hello {mention}.",
        "Greetings {mention}.",
        "Want to talk about the stars?",
        "You know, I once saw a supernova! There might be another one sooner than you think!",
        "In five billion years the sun will burn out!",
        "Hey! Hey! Did you know, The elves found a star in the 'Tarantula Nebula' in the 'Large Magellanic Cloud' called 'R136a1.' What a strange name huh?"
    ], "bye": [
        "Don't want to hear about the stars?",
        "Maybe you wanted to hear about planets instead...?",
        "Did I bore you?",
        "Wait come back! I have more stars I need to tell you about!",
        "Bye!",
        "Let's talk about more stars next time!",
        "See you soon!",
        "I think of you when I see the stars. I wonder if you think the same too!"
    ], "updt": [
        "Well be glad that the next update will come out before the sun dies!",
        "Not even the stars can tell me when it will come out.",
        "If you look at the stars, you may find your answer!",
        "What? Sorry, I was studying this particular star.",
        "When the stars align.",
        "When the red supergiant star, 'WOH G64' explodes!",
        "Can't see how that's more intresting than whats above you but, I don't know."
    ]
    },
    "elvira": {"name": "Elvira - <:elvira:1453638419350683761>", "color": 0x435680, "img": elvira_pics, "pic_leng": 13, "greet": [
        "Fooling around and wasting time huh. Maeve, I though you had better students...",
        "These nitwits don't even come close to my perfect daughter.",
        "Your grades are dropping, you haven't been into work, and you're not even pursuing anything. And you have the audacity to speak with me?",
        "Don't you have responsibilities to attend to?",
        "What is that you seek, young one?",
        "You wretch. What do you need?",
        "What does the pest want this time?",
        "Oh my. All my daughter does is just talk back to me. Maybe I should punish her, right?",
        "My daughter had so much potential. Truly a shame for her to be a failure."
    ], "bye": [
        "Don't you dare talk to my child.",
        "Do as you please.",
        "I dont want wish to see you again.",
        "Goodbye.",
        "Bye.",
        "Good day."
    ], "nick": [
        "One foolish daughter is enough for me. I don't need another.",
        "You may only adress me as Ms. Williams."
        "You may only call me Ms. Williams."
        "...",
        "Huh?",
        "Hah?",
        "You are mistaken.",
        "A fool like you is not my kin.",
        "Well...",
        "Get. Out. Of my Property."
    ], "updt": [
        "This blockhead has nothing else in their mind.",
        "Think before you speak, because you look very stupid right now.",
        "This donkey can't wait a couple of months. The great stars above...",
        "Maeve, I didn't know you let mouth-breathers roam your academy.",
        "This is who my daughter interacts with? Great heavens, save her soul.",
        "You only bring more shame to Maeve's name.",
        "You imbecile. You should be worring about your pathetic future instead of this.",
        "Oh how the witches have fallen. Thank the stars that you're not the top student. I don't even think you can call yourself a student."
    ]
    }
}

lulu_language = {
    "pneumoultamicroscopivolcaniosis": "OMG {mention}! It's so big! <:lu_khu:971274776993730611>",
    "hallo lulu": 'Hallo {mention}, ik ben de machtige Lulu!',
    "nihao lulu": '你好你好 {mention}，我絕對是真的 Lulu, 哈哈哈!',
    "bonjour lulu": "Bonjour {mention}, C'est moi Lulu!",
    "hola lulu": 'Jajaja! Hola {mention}! Me llamos La Lulu!',
    "ciao lulu": "Salve a {mention}! Sono la grande Lulú, Strega dell'Altopiano!",
    "ave lulu": 'Ave {mention}! Ego fabulosa magus Lulu! Cogito ergo sum.',
    "konnichiwa lulu": 'こんにちは {mention}! 私は史上最高の魔女ルルです!',
    "witam lulu": 'Khu khu khu! Witaj {mention}! Oto ja, Lulu!',
    "kumusta lulu": 'Bati ni {mention}! Ako si Lulu ang dakilang banal na mangkukulam, kumusta ka na?',
    "beannachdan lulu": 'Fàilte {mention}, Is mise a th\' ann, Lulu mhòr! Ciamar a tha thu?',
    "habari lulu": 'habari {mention}! Mimi ni Lulu! Mchawi Mtakatifu wa Milima ya Nyanda za Juu. Nimefurahi kukutana nawe!',
    "guten tag lulu": 'khu khu khu. Ich bin\'s, die einzigartige Lulu! Maeves beste Schülerin! Wie geht es dir, {mention}?',
    "privet lulu": 'Приветствую, товарищ, {mention}! Ты ищешь мудрости y Великой Lulu? Или ты хотел чего-то другого?',
    "ola lulu": 'Ah, {mention}! Sou eu, Lulu! Veio conversar com uma pessoa tão incrível quanto eu?',
    "namaste lulu": 'haahaaha, {mention}! kya tumhen sabase mahaan aur sabase shaktishaalee lulu se kuchh chaahie tha? main tumhaare kisee bhee savaal ka javaab de sakata hoon!',
    "mrhban lulu": 'ah! hal targhab bialtawasul mae lulu aleazimati? ah, \'ajal {mention}! lak mutlaq alhuriyat fi suaali ean \'ayi shay\'in!',
    "annyeonghaseyo lulu": '하하하 {mention}! 여기서 뵙게 되어 반갑습니다! Lulu님, 그레이트를 보러 오셨나요? 무슨 생각 드시나요?'
}

expel_dial = (
    "{mention}, you have done great harm to this academy. Thus, I concluded that you'll be petrified by my own hands. Goodbye.",
    "{mention}, this behavior will not be tolerated. You are hereby permanently expelled from the academy. Good day.",
    "{mention}, You will be executed for causing irreversable harm to my academy. Even though witches cannot die from decapitation, you are unfortunately human. The students will not be able to see or hear you and it will be painless. Goodbye {mention}.",
    "{mention}, You are to never return to this academy. If you are to step foot here once again I will have to use force against you. I am feeling nicer today so I'm letting you off easy. Heed by my warning and you will get to see the light of day again. Good day.",
    "{mention}, this behavior will not be tolerated. You are hereby permanently expelled from the academy. Good day.",
    "{mention}, what you have done here is unforgivable. You will promptly be removed from this academy as I see fit. Whether you live or not will be up to how durable your body and will is.",
    "{mention}, you are a danger to my students and I will not tolerate such depravity. As such, I, 'Maeve Midnight,' will swiftly erase you from existance as I deemed you a threat to the rest of society. You have no place here or anywhere else.",
    "I hope the academy doesn't see your demise, {mention}. I will swiftly take care of you, as you have harmed my academy. Goodbye",
    "{mention}, this behavior will not be tolerated. You are hereby permanently expelled from the academy. Good day."
)
ma_img = "https://images-ext-1.discordapp.net/external/vPYWVmNnHqvL6saMqb_3yMtdKzACtfTxl097ZPl3sfE/https/i.imgur.com/x5C3viN.png?format=webp&quality=lossless&width=648&height=648"

# potions

cel_potions = ("Strength", "Speed", "Invisibility", "Hair Growth", "Sleep", "Healing", "Love", "Blindness", "Intoxication", "Nail Growth", "Hydration", "Nutrition", "Explosion", "Levitation", "Fire Resistance", "Water Breathing", "Stone Skin", "Luck",
               "Misfortune", "Truth", "Wisdom", "Calming", "Rage", "Fear", "Courage", "Charm", "Night Vision", "Clone", "Iron Skin", "Laughing", "Antidote", "Gender Swap", "Voice Deepening", "Voice Raising", "Mana", "Bone Growth", "Silence", "Berserk",
               "Demon repellent", "Guthix Balance", "Energy", "Defence", "Goading", "Sanfew", "Stamina", "Saradomin", "Menaphite", "Kodai", "Dream", "Bravery", "Stink", "Inversion", "Sulphur", "Acid", "Fumigator", "Milk", "Breast Enhancement", "Size",
               "Amphetamine", "Aphrodisiac", "Numbing", "Anesthesia", "Laxitive", "Depression", "Anti-Depressant", "Lesser Healing", "Healing", "Greater Healing", "Super Healing", "Mushroom", "Lesser Mana", "Mana", "Greater Mana", "Super Mana", "Restoration", "Greater Restoration", "Apple Pie", "Banana Split", "Bowl of Soup", "Cooked Fish", "Cooked Marshmallow", "Cooked Shrimp", "Grub Soup", "Pumpkin Pie", "Sake", "Spaghetti", "Teacup", "Coffee Cup", "Milkshake", "Seafood Dinner", "Recall", "Wormhole", "Teleportation", "Magic Mirror", "Ice Mirror", "Return", "Gender Change", "Grapes", "Ale", "Bottled Water", "Night Owl", "Shine", "Invisibility", "Splunker", "Hunter", "Dangersense", "Featherfall", "Water Walking", "Flipper", "Gills", "Obsidian Skin", "Warmth", "Swiftness", "Blinkroot", "Teleportation", "Rage", "Wrath", "Summoning", "Ammo Reservation", "Archery", "Magic Power", "Mana Regeneration", "Endurance", "Ironskin", "Regeneration", "Life Force", "Heartreach", "Calming", "Builder", "Mining", "Lifeforce", "Gravitation", "Titan", "Thorns", "Inferno", "Rage", "Wrath", "Sharpening Station", "Slice of Cake", "Fishing", "Crate", "Sonar", "Flipper", "Gills", "Water Walking", "Warmth", "Ironskin", "Endurance", "Rage", "Wrath", "Thorns", "Lifeforce", "Heartreach", "Magic Power", "Mana Regeneration", "Summoning", "Ammo Reservation", "Archery", "Battle", "Inferno", "Love", "Stink", "Teleportation", "Gravitation", "Courage", "Trapsight", "Bioluminescence", "Luck", "Greater Luck", "Luck (Lesser)", "Builder", "Mining")

index_lookup = {
    1029: 0, 642: 1, 26: 2, 16396: 3, 10304: 4, 2208: 5, 24832: 6, 16912: 7,
    11: 8, 4099: 9, 76: 10, 12544: 11, 3328: 12, 16432: 13, 164: 14, 37: 15,
    38: 16, 17416: 17, 4102: 18, 19456: 19, 2592: 20, 18560: 21, 4672: 22,
    4864: 23, 18433: 24, 1027: 25, 17412: 26, 13312: 27, 4610: 28, 4130: 29,
    8288: 30, 2068: 31, 134: 32, 4609: 33, 4161: 34, 8512: 35, 265: 36, 4168: 37,
    8960: 38, 4356: 39, 2114: 40, 16480: 41, 24578: 42, 20484: 43, 16672: 44,
    4480: 45, 2336: 46, 6656: 47, 578: 48, 328: 49, 8576: 50, 3136: 51, 280: 52,
    259: 53, 196: 54, 22528: 55, 521: 56, 2082: 57, 517: 58, 4256: 59, 2192: 60,
    12289: 61, 12800: 62, 416: 63, 9224: 64, 8706: 65, 131: 66, 4232: 67,
    8328: 68, 1216: 69, 8384: 70, 8336: 71, 17152: 72, 1154: 73, 273: 74,
    17440: 75, 386: 76, 4120: 77, 17424: 78, 5128: 79, 1064: 80, 1044: 81,
    28672: 82, 16513: 83, 8240: 84, 25088: 85, 14: 86, 16898: 87, 772: 88,
    1120: 89, 13: 90, 8232: 91, 16904: 92, 545: 93, 10241: 94, 4162: 95,
    16418: 96, 4116: 97, 100: 98, 8832: 99, 74: 100, 8198: 101, 10272: 102,
    2120: 103, 4132: 104, 6145: 105, 17664: 106, 8449: 107, 6208: 108, 112: 109,
    4108: 110, 268: 111, 3073: 112, 552: 113, 322: 114, 2084: 115, 11264: 116,
    2072: 117, 8202: 118, 4354: 119, 24584: 120, 8201: 121, 4164: 122,
    8204: 123, 770: 124, 20481: 125, 385: 126, 1600: 127, 336: 128, 4176: 129,
    18436: 130, 22: 131, 16768: 132, 168: 133, 2088: 134, 2562: 135, 704: 136,
    24704: 137, 133: 138, 524: 139, 44: 140, 400: 141, 4105: 142, 12304: 143,
    776: 144, 3080: 145, 448: 146, 9472: 147, 8352: 148, 1540: 149, 577: 150,
    4113: 151, 6400: 152, 1036: 153, 2178: 154, 1060: 155, 1284: 156, 584: 157,
    18944: 158, 2058: 159, 5121: 160, 8258: 161, 8260: 162, 10496: 163,
    2060: 164, 1090: 165, 19: 166, 4226: 167, 1568: 168, 6152: 169, 8768: 170,
    67: 171
}

'''
def generate_masks(count=172, bits=15, picks=3):
    """Generate `count` unique random bitmasks with exactly `picks` bits set."""

    max_bit = bits
    pick = picks

    # Create ALL possible 3-bit masks
    all_masks = []
    for i in range(max_bit):
        for j in range(i + 1, max_bit):
            for k in range(j + 1, max_bit):
                mask = (1 << i) | (1 << j) | (1 << k)
                all_masks.append(mask)

    # Safety: There are exactly 455 unique 3-bit masks in 15 bits
    if count > len(all_masks):
        raise ValueError(
            f"count cannot exceed {len(all_masks)} possible combinations")

    # Sample random masks for maximum spread
    selected_masks = random.sample(all_masks, count)

    return selected_masks


# Example usage
masks = generate_masks()
# print(masks)
'''

pot_img = (
    "https://oldschool.runescape.wiki/images/Imp_repellent.png?19317",
    "https://oldschool.runescape.wiki/images/Attack_potion%284%29.png?758a9",
    "https://oldschool.runescape.wiki/images/Antipoison%284%29.png?78f79",
    "https://oldschool.runescape.wiki/images/Relicym%27s_balm%284%29.png?b11fe",
    "https://oldschool.runescape.wiki/images/Strength_potion%284%29.png?a8970",
    "https://oldschool.runescape.wiki/images/Serum_207_%284%29.png?462fd",
    "https://oldschool.runescape.wiki/images/Compost_potion%284%29.png?2aac1",
    "https://oldschool.runescape.wiki/images/Restore_potion%284%29.png?b11fe",
    "https://oldschool.runescape.wiki/images/Guthix_balance%284%29.png?06911",
    "https://oldschool.runescape.wiki/images/Blamish_oil.png?cab41",
    "https://oldschool.runescape.wiki/images/Energy_potion%284%29.png?01f76",
    "https://oldschool.runescape.wiki/images/Defence_potion%284%29.png?6b57c",
    "https://oldschool.runescape.wiki/images/Agility_potion%284%29.png?a203e",
    "https://oldschool.runescape.wiki/images/Combat_potion%284%29.png?43e7d",
    "https://oldschool.runescape.wiki/images/Prayer_potion%284%29.png?219da",
    "https://oldschool.runescape.wiki/images/Super_attack%284%29.png?ff13c",
    "https://oldschool.runescape.wiki/images/Goblin_potion%284%29.png?4d1b1",
    "https://oldschool.runescape.wiki/images/Superantipoison%284%29.png?57bdc",
    "https://oldschool.runescape.wiki/images/Fishing_potion%284%29.png?2632b",
    "https://oldschool.runescape.wiki/images/Super_energy%284%29.png?9cd45",
    "https://oldschool.runescape.wiki/images/Shrink-me-quick.png?199d1",
    "https://oldschool.runescape.wiki/images/Hunter_potion%284%29.png?7331d",
    "https://oldschool.runescape.wiki/images/Goading_potion%284%29.png?4836f",
    "https://oldschool.runescape.wiki/images/Super_strength%284%29.png?fa231",
    "https://oldschool.runescape.wiki/images/Magic_essence%284%29.png?8bd5a",
    "https://oldschool.runescape.wiki/images/Prayer_regeneration_potion%284%29.png?9baad",
    "https://oldschool.runescape.wiki/images/Weapon_poison.png?43659",
    "https://oldschool.runescape.wiki/images/Super_restore%284%29.png?9074d",
    "https://oldschool.runescape.wiki/images/Sanfew_serum%284%29.png?7313d",
    "https://oldschool.runescape.wiki/images/Super_defence%284%29.png?ff13c",
    "https://oldschool.runescape.wiki/images/Antidote%2B%284%29.png?78f79",
    "https://oldschool.runescape.wiki/images/Antifire_potion%284%29.png?38864",
    "https://oldschool.runescape.wiki/images/Divine_super_attack_potion%284%29.png?e2602",
    "https://oldschool.runescape.wiki/images/Divine_super_defence_potion%284%29.png?e2602",
    "https://oldschool.runescape.wiki/images/Divine_super_strength_potion%284%29.png?e2602",
    "https://oldschool.runescape.wiki/images/Ranging_potion%284%29.png?095ed",
    "https://oldschool.runescape.wiki/images/Weapon_poison%2B.png?058f5",
    "https://oldschool.runescape.wiki/images/Divine_ranging_potion%284%29.png?e2602",
    "https://oldschool.runescape.wiki/images/Magic_potion%284%29.png?ed6d0",
    "https://oldschool.runescape.wiki/images/Stamina_potion%284%29.png?717c8",
    "https://oldschool.runescape.wiki/images/Zamorak_brew%284%29.png?37c64",
    "https://oldschool.runescape.wiki/images/Divine_magic_potion%284%29.png?2c9d4",
    "https://oldschool.runescape.wiki/images/Antidote%2B%2B%284%29.png?78f79",
    "https://oldschool.runescape.wiki/images/Bastion_potion%284%29.png?e9754",
    "https://oldschool.runescape.wiki/images/Battlemage_potion%284%29.png?3be33",
    "https://oldschool.runescape.wiki/images/Saradomin_brew%284%29.png?c82f9",
    "https://oldschool.runescape.wiki/images/Surge_potion%284%29.png?17b44",
    "https://oldschool.runescape.wiki/images/Weapon_poison%2B%2B.png?77b8c",
    "https://oldschool.runescape.wiki/images/Extended_antifire%284%29.png?b8cf0",
    "https://oldschool.runescape.wiki/images/Ancient_brew%284%29.png?7fdd8",
    "https://oldschool.runescape.wiki/images/Divine_bastion_potion%284%29.png?e2602",
    "https://oldschool.runescape.wiki/images/Divine_battlemage_potion%284%29.png?2c9d4",
    "https://oldschool.runescape.wiki/images/Anti-venom%284%29.png?38864",
    "https://oldschool.runescape.wiki/images/Menaphite_remedy%284%29.png?b0b20",
    "https://oldschool.runescape.wiki/images/Super_combat_potion%284%29.png?ff13c",
    "https://oldschool.runescape.wiki/images/Forgotten_brew%284%29.png?6600c",
    "https://oldschool.runescape.wiki/images/Super_antifire_potion%284%29.png?320fe",
    "https://oldschool.runescape.wiki/images/Anti-venom%2B%284%29.png?1f712",
    "https://oldschool.runescape.wiki/images/Extended_anti-venom%2B%284%29.png?481c2",
    "https://oldschool.runescape.wiki/images/Divine_super_combat_potion%284%29.png?cb9aa",
    "https://oldschool.runescape.wiki/images/Extended_super_antifire%284%29.png?97fe8",
    "https://oldschool.runescape.wiki/images/Vial_of_blood.png?4afbb",
    "https://oldschool.runescape.wiki/images/Coconut_milk.png?09bb0",
    "https://oldschool.runescape.wiki/images/Magic_potion%284%29.png?ed6d0",
    "https://oldschool.runescape.wiki/images/Anchovy_oil.png?ec289",
    "https://oldschool.runescape.wiki/images/Anti-venom%284%29.png?38864",
    "https://terraria.wiki.gg/images/c/c5/Bottled_Honey.png?d450a0",
    "https://terraria.wiki.gg/images/1/16/Bottled_Water.png?7d5a62",
    "https://terraria.wiki.gg/images/a/a5/Greater_Healing_Potion.png?3b8814",
    "https://terraria.wiki.gg/images/9/96/Greater_Healing_Potion_%28old%29.png?9dc34a",
    "https://terraria.wiki.gg/images/c/cd/Bottled_Water_%28old%29.png?155999",
    "https://terraria.wiki.gg/images/4/47/Healing_Potion.png?2e776b",
    "https://terraria.wiki.gg/images/e/e1/Lesser_Healing_Potion.png?5856e3",
    "https://terraria.wiki.gg/images/d/df/Lesser_Restoration_Potion_%28old%29.png?c75353",
    "https://terraria.wiki.gg/images/8/80/Mana_Potion.png?96d9ef",
    "https://terraria.wiki.gg/images/c/c9/Restoration_Potion.png?794c2c",
    "https://terraria.wiki.gg/images/d/d1/Restoration_Potion_%28old%29.png?f4126a",
    "https://terraria.wiki.gg/images/0/00/Super_Healing_Potion.png?614e36",
    "https://terraria.wiki.gg/images/4/43/Super_Mana_Potion.png?1ac169",
    "https://terraria.wiki.gg/images/2/2e/Lesser_Mana_Potion.png?b2c12c",
    "https://terraria.wiki.gg/images/2/23/Strange_Brew.png?a16f3c",
    "https://terraria.wiki.gg/images/Ammo_Reservation_Potion.png?59b9c7",
    "https://terraria.wiki.gg/images/Archery_Potion.png?bad0ee",
    "https://terraria.wiki.gg/images/Battle_Potion.png?da4193",
    "https://terraria.wiki.gg/images/Biome_Sight_Potion.png?8389bc",
    "https://terraria.wiki.gg/images/Builder_Potion.png?78c9cb",
    "https://terraria.wiki.gg/images/Calming_Potion.png?e2cf6a",
    "https://terraria.wiki.gg/images/Crate_Potion_%28old%29.png?1def73",
    "https://terraria.wiki.gg/images/Crate_Potion.png?758b7d",
    "https://terraria.wiki.gg/images/Dangersense_Potion.png?72634d",
    "https://terraria.wiki.gg/images/Endurance_Potion.png?a735a3",
    "https://terraria.wiki.gg/images/Featherfall_Potion.png?6174b2",
    "https://terraria.wiki.gg/images/Fishing_Potion.png?7c5a67",
    "https://terraria.wiki.gg/images/Flipper_Potion.png?32e7be",
    "https://terraria.wiki.gg/images/Gills_Potion.png?9f051f",
    "https://terraria.wiki.gg/images/Gravitation_Potion.png?51b155",
    "https://terraria.wiki.gg/images/Greater_Luck_Potion.png?2fd3bc",
    "https://terraria.wiki.gg/images/Heartreach_Potion.png?4c9fea",
    "https://terraria.wiki.gg/images/Heartreach_Potion_%28old%29.png?5b618e",
    "https://terraria.wiki.gg/images/Hunter_Potion.png?1cd599",
    "https://terraria.wiki.gg/images/Inferno_Potion.png?f7eb42",
    "https://terraria.wiki.gg/images/Invisibility_Potion.png?e6d035",
    "https://terraria.wiki.gg/images/Ironskin_Potion.png?9f322c",
    "https://terraria.wiki.gg/images/Lesser_Luck_Potion.png?7ae485",
    "https://terraria.wiki.gg/images/Lifeforce_Potion.png?6f440d",
    "https://terraria.wiki.gg/images/Love_Potion.png?722d1f",
    "https://terraria.wiki.gg/images/Luck_Potion.png?becd44",
    "https://terraria.wiki.gg/images/Magic_Power_Potion.png?ea847b",
    "https://terraria.wiki.gg/images/Mana_Regeneration_Potion.png?fa86bf",
    "https://terraria.wiki.gg/images/Mining_Potion.png?53d1ab",
    "https://terraria.wiki.gg/images/Night_Owl_Potion.png?fc26c6",
    "https://terraria.wiki.gg/images/Obsidian_Skin_Potion.png?9ccc99",
    "https://terraria.wiki.gg/images/Rage_Potion.png?5be212",
    "https://terraria.wiki.gg/images/Regeneration_Potion.png?f9eab9",
    "https://terraria.wiki.gg/images/Shine_Potion.png?1531fb",
    "https://terraria.wiki.gg/images/Sonar_Potion.png?59d0cf",
    "https://terraria.wiki.gg/images/Spelunker_Potion.png?74b746",
    "https://terraria.wiki.gg/images/Stink_Potion.png?475c6a",
    "https://terraria.wiki.gg/images/Summoning_Potion.png?43efe7",
    "https://terraria.wiki.gg/images/Swiftness_Potion.png?ee658c",
    "https://terraria.wiki.gg/images/Thorns_Potion.png?b54758",
    "https://terraria.wiki.gg/images/Thorns_Potion_%28old%29.png?b9e740",
    "https://terraria.wiki.gg/images/Titan_Potion.png?8228a0",
    "https://terraria.wiki.gg/images/Warmth_Potion.png?b19d84",
    "https://terraria.wiki.gg/images/Water_Walking_Potion.png?ab0664",
    "https://terraria.wiki.gg/images/Wrath_Potion.png?c3e0fc",
    "https://terraria.wiki.gg/images/Flask_of_Cursed_Flames.png?47c34f",
    "https://terraria.wiki.gg/images/Flask_of_Fire.png?cebe89",
    "https://terraria.wiki.gg/images/Flask_of_Gold.png?ed265a",
    "https://terraria.wiki.gg/images/Flask_of_Ichor.png?e7d7d6",
    "https://terraria.wiki.gg/images/Flask_of_Nanites.png?8c8a10",
    "https://terraria.wiki.gg/images/Flask_of_Party.png?8ab5f5",
    "https://terraria.wiki.gg/images/Flask_of_Poison.png?30d240",
    "https://terraria.wiki.gg/images/Flask_of_Venom.png?a3fc08",
    "https://terraria.wiki.gg/images/b/b7/Gender_Change_Potion.png?b49c70",
    "https://terraria.wiki.gg/images/f/f2/Potion_of_Return.png?48f994",
    "https://terraria.wiki.gg/images/6/67/Recall_Potion.png?ea6c26",
    "https://terraria.wiki.gg/images/8/84/Recall_Potion_%28old%29.png?a73667",
    "https://terraria.wiki.gg/images/3/38/Teleportation_Potion.png?80b76b",
    "https://terraria.wiki.gg/images/3/3b/Wormhole_Potion.png?602e5b",
    "https://terraria.wiki.gg/images/d/dd/Red_Potion.png?7dbc17",
    "https://oldschool.runescape.wiki/images/Attack_mix%282%29.png?2baad",
    "https://oldschool.runescape.wiki/images/Antipoison_mix%282%29.png?78f79",
    "https://oldschool.runescape.wiki/images/Relicym%27s_mix%282%29.png?b11fe",
    "https://oldschool.runescape.wiki/images/Strength_mix%282%29.png?e42b7",
    "https://oldschool.runescape.wiki/images/Restore_mix%282%29.png?4e1b1",
    "https://oldschool.runescape.wiki/images/Energy_mix%282%29.png?3a184",
    "https://oldschool.runescape.wiki/images/Defence_mix%282%29.png?6b57c",
    "https://oldschool.runescape.wiki/images/Agility_mix%282%29.png?248b4",
    "https://oldschool.runescape.wiki/images/Combat_mix%282%29.png?bd75b",
    "https://oldschool.runescape.wiki/images/Prayer_mix%282%29.png?b225e",
    "https://oldschool.runescape.wiki/images/Superattack_mix%282%29.png?fa231",
    "https://oldschool.runescape.wiki/images/Anti-poison_supermix%282%29.png?38864",
    "https://oldschool.runescape.wiki/images/Fishing_mix%282%29.png?4a487",
    "https://oldschool.runescape.wiki/images/Super_energy_mix%282%29.png?9cd45",
    "https://oldschool.runescape.wiki/images/Hunting_mix%282%29.png?1940c",
    "https://oldschool.runescape.wiki/images/Super_str._mix%282%29.png?9f3ef",
    "https://oldschool.runescape.wiki/images/Magic_essence_mix%282%29.png?8bd5a",
    "https://oldschool.runescape.wiki/images/Super_restore_mix%282%29.png?b4c2b",
    "https://oldschool.runescape.wiki/images/Stamina_mix%282%29.png?8dbbb",
    "https://oldschool.runescape.wiki/images/Extended_antifire_mix%282%29.png?b8cf0",
    "https://oldschool.runescape.wiki/images/Ancient_mix%282%29.png?f1dbb",
    "https://oldschool.runescape.wiki/images/Super_antifire_mix%282%29.png?320fe",
    "https://oldschool.runescape.wiki/images/Extended_super_antifire_mix%282%29.png?b8cf0",
    "https://oldschool.runescape.wiki/images/Cadava_potion.png?56d17",
    "https://oldschool.runescape.wiki/images/Potion_of_sealegs.png?ed4b0",
    "https://oldschool.runescape.wiki/images/Potion_%28A_Taste_of_Hope%29.png?64f1b",
    "https://oldschool.runescape.wiki/images/Sulphur_potion.png?a0c7b",
    "https://oldschool.runescape.wiki/images/Bravery_potion.png?05d25",
    "https://oldschool.runescape.wiki/images/Marrentill_potion_%28unf%29.png?717ea",
    "https://oldschool.runescape.wiki/images/Unfinished_serum_%28step_2%29.png?440ab",
    "https://oldschool.runescape.wiki/images/Unfinished_serum_%28step_1%29.png?440ab",
    "https://oldschool.runescape.wiki/images/Strangler_serum.png?70ea6",
)
