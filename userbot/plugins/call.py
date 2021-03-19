"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""


import asyncio

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern=r"call"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    # input_str = event.pattern_match.group(1)

    # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        "`Connecting To Telegram Headquarters...`",
        "`Call Connected.`",
        "`Telegram: Hello This is Telegram HQ. Who is this?`",
        "`Me: Yo this is`  [SAVAGE SUPPORT](t.me/SAVAGE_TEAM_USERBOT)  ,`Please Connect me to my idiot bro  SAMEER 😂`",
        "`User Authorised.`",
        "`Calling SAMEER SUR`  `At +916969696969`",
        "`Private  Call Connected...`",
        "`Me: Hello Sir, Please Ban This Telegram Account.`",
        "`SAMEER: May I Know Who Is This?`",
        "`Me: Yo Brah, itz me`  ",
        "`Pavel: OMG!!! Long time no see, Wassup Brother...\nI'll Make Sure That Guy Account Will Get Banned Within 24Hrs.`",
        "`Me: Thanks, See You Later Brah.`",
        "`SAMEER: Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
        "`Me: Is There Any Issue/Emergency???`",
        "`SAMEER: Yes Sir, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
        "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
        "`SAMEER: Sure Sur \nTC Bye Bye ;)`",
        "`Private Call Disconnected.`",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
