"""
Report a peer for violation of telegram’s Terms of Service.

https://docs.pyrogram.org/telegram/functions/account/report-peer#pyrogram.raw.functions.account.ReportPeer
"""

from pyrogram.raw.functions.account import ReportPeer
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    chat_id = -100123456789 # user, channel, supergroup, group
    peer = await app.resolve_peer(chat_id)

    # Get reasons from here :
    #   https://docs.pyrogram.org/telegram/base/report-reason#pyrogram.raw.base.ReportReason
    reason = raw.types.InputReportReasonSpam()
    meesage = "Your message to telegram team"
    res: "bool" = await app.invoke(
        ReportPeer(
            peer=peer,
            reason=reason,
            message=meesage
        )
    )
    print(res)

app.run(main())

