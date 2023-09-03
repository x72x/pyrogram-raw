"""
Invite a set of users to a group call.

https://docs.pyrogram.org/telegram/functions/phone/invite-to-group-call
"""
from typing import Union
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.phone import InviteToGroupCall
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    chat_id = -10000000000000000
    user_ids : Union["int", "str"] = [5112345678, "DevZaid"]
    peer_channel = await app.resolve_peer(chat_id)
    if not isinstance(peer_channel, raw.types.InputPeerChannel):
        print("This chat_id not for channel/supergroup")
        return False
    peer_users = [await app.resolve_peer(i) for i in user_ids]
    get_channel: "raw.types.messages.ChatFull" = await app.invoke(
        GetFullChannel(
            channel=peer_channel
        )
    )
    call: "raw.types.InputGroupCall" = get_channel.full_chat.call
    res: "raw.types.Updates" = await app.invoke(
        InviteToGroupCall(
            call=call,
            users=peer_users
        )
    )
    print(res)

app.run(main())