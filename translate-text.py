"""
Translate a given text.

https://docs.pyrogram.org/telegram/functions/messages/translate-text
"""

from pyrogram.raw.functions.messages import TranslateText
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    # to translate from an message in chat
    chat_id = "y88f8" # user, group, supergroup, channel ( int | str )
    to_lang = "en" # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    message_id = [266, 720] # list of messages ids
    res: raw.types.messages.TranslatedText = await app.invoke(
        TranslateText(
            peer=await app.resolve_peer(chat_id),
            to_lang=to_lang,
            id=message_id
        )
    )
    print(res)

    # to translate from text
    text = "مرحبا كيف حالكم"
    to_lang = "en" # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    res: raw.types.messages.TranslatedText = await app.invoke(
        TranslateText(
            to_lang=to_lang,
            text=[
                raw.types.TextWithEntities(
                    text=text,
                    entities=[
                        raw.types.MessageEntityUnknown(offset=1, length=1)
                    ]
                )
            ]
        )
    )
    print(res)


app.run(main())

