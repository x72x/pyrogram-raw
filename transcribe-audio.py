"""
Transcribe voice message.

https://docs.pyrogram.org/telegram/functions/messages/transcribe-audio
"""

import asyncio
from pyrogram.raw.functions.messages import TranscribeAudio
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    chat_id = 6316628074 # user, channel, supergroup, group
    peer = await app.resolve_peer(chat_id)
    meesage_id = 319522

    res:"raw.types.messages.TranscribedAudio" = await app.invoke(
        TranscribeAudio(
            peer=peer,
            msg_id=meesage_id
        )
    )
    print(res)

    while res.pending:
        await asyncio.sleep(5)
        res:" raw.types.messages.TranscribedAudio" = await app.invoke(
            TranscribeAudio(
                peer=peer,
                msg_id=meesage_id
            )
        )
        print(res)

app.run(main())

