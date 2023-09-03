"""
Delete a channel/supergroup.

https://docs.pyrogram.org/telegram/functions/channels/delete-channel
"""

from pyrogram.raw.functions.channels import DeleteChannel
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    chat_id = -10000000000
    peer = await app.resolve_peer(chat_id)
    if not isinstance(peer, raw.types.InputPeerChannel):
        print("This chat_id not for channel/supergroup")
        return False
    res: "raw.types.Udates" = await app.invoke(
        DeleteChannel(
            channel=peer
        )
    )
    print(res)

app.run(main())

