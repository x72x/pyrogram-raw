"""
Delete the history of a supergroup.

https://docs.pyrogram.org/telegram/functions/channels/delete-history
"""

from pyrogram.raw.functions.channels import DeleteHistory
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    chat_id = -1000000000000
    peer = await app.resolve_peer(chat_id)
    if not isinstance(peer, raw.types.InputPeerChannel):
        print("This chat_id not for supergroup")
        return False
    # You must be the owner of the supergroup
    res: "raw.types.Updates" = await app.invoke(
        DeleteHistory(
            channel=peer,
            max_id=0,
            for_everyone=True
        )
    )
    print(res)

app.run(main())

