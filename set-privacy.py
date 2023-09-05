"""
Change privacy settings of current account.

https://docs.pyrogram.org/telegram/functions/account/set-privacy
"""
from pyrogram.raw.functions.account import SetPrivacy
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    # Get any privacy key from : https://docs.pyrogram.org/telegram/base/input-privacy-key#pyrogram.raw.base.InputPrivacyKey
    key = raw.types.InputPrivacyKeyStatusTimestamp() # To change last seen privacy settings

    # Get privacy rule from: https://docs.pyrogram.org/telegram/base/input-privacy-rule#pyrogram.raw.base.InputPrivacyRule
    rule = raw.types.InputPrivacyValueAllowContacts() # Allow only my contacts to see my last seen
    # for "Nobody" can see your last seen, use: raw.types.InputPrivacyValueDisallowAll()
    # You can use multiple rules, ex: choose Nobody can see your last seen, and add a list of users can see your last seen
    # rule2 = raw.types.InputPrivacyValueAllowUsers(users=[await app.resolve_peer("DevZaid")])
    z: "raw.types.account.PrivacyRules" = await app.invoke(
        SetPrivacy(
            key=key,
            # rules = [rule, rule2], # You can add just one rule
            rules=[rule],
        )
    )
    print(z)

app.run(main())