"""
Transfer channel ownership.

https://docs.pyrogram.org/telegram/functions/channels/edit-creator
"""
from pyrogram.raw.functions.channels import EditCreator
from pyrogram.raw.functions.account import GetPassword
from pyrogram.raw.types import InputCheckPasswordEmpty
from pyrogram.raw.types.account import Password
from pyrogram.utils import compute_password_check
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    chat_id = -1000000000
    new_owner_id = "DevZaid" # user id or username
    peer_channel = await app.resolve_peer(chat_id)
    peer_user = await app.resolve_peer(new_owner_id)
    if not isinstance(peer_channel, raw.types.InputPeerChannel):
        print("This chat_id not for channel/supergroup")
        return False
    if not isinstance(peer_user, raw.types.InputPeerUser):
        print("This user_id not for channel/supergroup")
        return False
    i: "Password" = await app.invoke(GetPassword())
    if not i.has_password:
        password = InputCheckPasswordEmpty()
    else:
        current_password = input("- Enter your password : - ")
        password = compute_password_check(i, current_password)

    res: "raw.types.Update" = await app.invoke(
        EditCreator(
            channel=peer_channel,
            user_id=peer_user,
            password=password
        )
    )
    print(res)

app.run(main())

