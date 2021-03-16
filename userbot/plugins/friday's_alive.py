"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import os
import time

from userbot import ALIVE_NAME, Lastupdate
from userbot.plugins import currentversion
from userbot.utils import lightning_cmd, sudo_cmd

FRI_IMAGE = os.environ.get("FRI_IMAGE", None)
if FRI_IMAGE is None:
    FRI_IMG = "https://telegra.ph/file/00f60d92a8e02db2a9877.mp4"
else:
    FRI_IMG = FRI_IMAGE


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

    pm_caption = "🔥🔥𝐒𝐀𝐕𝐀𝐆𝐄 𝐎𝐍 𝐅𝐈𝐑𝐄🔥🔥\n"
        pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
        pm_caption += "𝐎𝐖𝐍𝐄𝐑             : [⚡丂卂爪乇乇尺⚡](@sameer_795)\n" 
        pm_caption += "𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : 1.17.5\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐀𝐍𝐍𝐄𝐋  : [ᴊᴏɪɴ](https://t.me/SAVAGE_TECHY)\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏    : [ᴊᴏɪɴ](https://t.me/SAVAGE_TEAM_BOT)\n"
        pm_caption += "𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏       : [𝐒𝐀𝐕𝐀𝐆𝐄](https://t.me/SAVAGE_TEAM_BOLTE)\n\n"
        pm_caption += "[ꀷꏂᖘ꒒ꂦꌩ ꌩꂦꀎꋪ ꂦꅐꈤ ꌚꍏ꒦ꍏꁅꏂ](https://github.com/sameerpanthi/SAVAGE-IS-BACK)\n"


@borg.on(lightning_cmd(pattern=r"falive"))
@borg.on(sudo_cmd(pattern=r"falive", allow_sudo=True))
async def friday(falive):
    await falive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(falive.chat_id, FRI_IMG, caption=pm_caption)
    await falive.delete()
