#Made by @Kraken_The_BadASS for @HellBot_Official

from userbot.utils import mellow_cmd
from var import Var



borg.on(mellow_cmd(pattern="wspr ?(.*)"))
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr) 
    await tap[0].click(event.chat_id)
    await event.delete()