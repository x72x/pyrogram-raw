"""
Report a message in a chat for violation of telegram’s Terms of Service.

https://docs.pyrogram.org/telegram/functions/messages/report
"""

from pyrogram.raw.functions.messages import Report
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    chat_id = -100123456789 # user, channel, supergroup, group
    peer = await app.resolve_peer(chat_id)
    message_ids = [1, 2, 3]

    # Get reasons from here :
    #   https://docs.pyrogram.org/telegram/base/report-reason#pyrogram.raw.base.ReportReason
    reason = raw.types.InputReportReasonSpam()
    meesage = "Your message to telegram team"
    res: "bool" = await app.invoke(
        Report(
            peer=peer,
            id=message_ids,
            reason=reason,
            message=meesage
        )
    )
    print(res)

app.run(main())
