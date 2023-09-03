"""
Delete the user’s account from the telegram servers.

https://docs.pyrogram.org/telegram/functions/account/delete-account
"""

from pyrogram.raw.functions.account import DeleteAccount, GetPassword
from pyrogram.raw.types import InputCheckPasswordEmpty
from pyrogram.raw.types.account import Password
from pyrogram.utils import compute_password_check

from pyrogram import Client

app = Client("name")

async def main():
    await app.start()
    i: "Password" = await app.invoke(GetPassword())
    if not i.has_password:
        password = InputCheckPasswordEmpty()
    else:
        current_password = input("- Enter your password : - ")
        password = compute_password_check(i, current_password)
    res: "bool" = await app.invoke(
        DeleteAccount(
            reason="reason",
            password=password
        )
    )
    print(res)



app.run(main())