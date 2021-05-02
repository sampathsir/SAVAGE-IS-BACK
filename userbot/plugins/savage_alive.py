

import asyncio
import os

from telethon import __version__ 
from userbot import ALIVE_NAME, TG_CHANNEL, TG_GRUP
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd

LIGHTNING_ALV_IMG = os.environ.get("LIGHTNING_ALV_IMG", None)
if LIGHTNING_ALV_IMG is None:
    ALV_LIGHTNING = "https://telegra.ph/file/3d0acf2f0b5fd015d3b40.jpg"
else:
    ALV_LIGHTNING = LIGHTNING_ALV_IMG

version = "4.5"
python_version = "3.8.5"

# Functions
def lightning_Read_time(seconds: int) -> str:
    count = 0
    kirsh = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            lol_hehehe, result = divmod(seconds, 60)
        else:
            lol_hehehe, result = divmod(seconds, 24)
        if seconds == 0 and lol_hehehe == 0:
            break
        time_list.append(int(result))
        seconds = int(lol_hehehe)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        kirsh += time_list.pop() + ", "

    time_list.reverse()
    kirsh += ":".join(time_list)
                
    return kirsh

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SAVAGE BOY"

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet😁😁"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet😁😁"


from userbot import CMD_LIST

pm_caption = "__                       **😎🔥 𝐒𝐀𝐕𝐀𝐆𝐄_𝐁𝐎𝐓 😎🔥**  __\n\n"
pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
pm_caption += "✘ ΔβØỮŦ Μ¥ Ş¥ŞŦ€Μ ✘\n\n"
pm_caption += "➾ 𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍**     ➣ 𝟏.𝟏𝟕.𝟓\n"
pm_caption += "➾ 𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏    ➣ [𝐒𝐀𝐕𝐀𝐆𝐄](https://t.me/joinchat/RPrJW2IU-Uo4MGRl)\n"
pm_caption += "➾ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐍𝐍𝐋 ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/0KCyT0MHyAhmMmRl)\n"
pm_caption += "➾ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/qCIk-af6VW1kNDll)\n"
pm_caption += "➾ 𝐂𝐑𝐄𝐀𝐓𝐎𝐑     ➣ [⚡𝐒𝐀𝐌𝐄𝐄𝐑⚡](@SAMEER_795)\n" 
                  
pm_caption += " \n"
pm_caption += "[✨𝑫𝑬𝑷𝑳𝑶𝒀 𝒀𝑶𝑼𝑹 𝑺𝑨𝑽𝑨𝑮𝑬✨](https://github.com/sameerpanthi/SAVAGE-IS-BACK)"

@borg.on(lightning_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def lightning(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, ALV_LIGHTNING, caption=pm_caption)
    await alive.delete()

