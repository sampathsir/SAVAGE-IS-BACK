

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

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet๐๐"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet๐๐"


from userbot import CMD_LIST

pm_caption = "__                       **๐๐ฅ ๐๐๐๐๐๐_๐๐๐ ๐๐ฅ**  __\n\n"
pm_caption += f"               __โผ๐ผ๐ฐ๐๐๐ด๐โ__\n**      ใ{DEFAULTUSER}ใ**\n\n"
pm_caption += "โ ฮฮฒรแปฎลฆ ฮยฅ ลยฅลลฆโฌฮ โ\n\n"
pm_caption += "โพ ๐๐๐๐๐๐๐๐        โฃ ๐.๐๐.๐\n"
pm_caption += "โพ ๐๐๐๐ ๐๐๐๐๐     โฃ [๐๐๐๐๐๐](https://t.me/joinchat/RPrJW2IU-Uo4MGRl)\n"
pm_caption += "โพ ๐๐๐๐๐๐๐ ๐๐๐๐๐ โฃ [๐๐๐๐](https://t.me/joinchat/0KCyT0MHyAhmMmRl)\n"
pm_caption += "โพ ๐๐๐๐๐๐๐ ๐๐๐๐๐ โฃ [๐๐๐๐](https://t.me/joinchat/qCIk-af6VW1kNDll)\n"
pm_caption += "โพ ๐๐๐๐๐๐๐     โฃ [โก๐๐๐๐๐๐โก](@SAMEER_795)\n" 
                  
pm_caption += " \n"
pm_caption += "[โจ๐ซ๐ฌ๐ท๐ณ๐ถ๐ ๐๐ถ๐ผ๐น ๐บ๐จ๐ฝ๐จ๐ฎ๐ฌโจ](https://github.com/sameerpanthi/SAVAGE-IS-BACK)"

@borg.on(lightning_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def lightning(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, ALV_LIGHTNING, caption=pm_caption)
    await alive.delete()

