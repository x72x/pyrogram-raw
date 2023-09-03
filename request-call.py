#This is taken from https://github.com/LonamiWebs/Telethon-calls/blob/master/calls.py and modified
"""
Start a telegram phone call.

https://docs.pyrogram.org/telegram/functions/phone/request-call
"""
import hashlib
import os
import random

from pyrogram.raw.functions.phone import RequestCall
from pyrogram.raw.functions.messages import GetDhConfig
from pyrogram.raw.types import PhoneCallProtocol
from pyrogram import Client, raw

app = Client("name")

async def main():
    await app.start()
    user_id = "DevZaid" # user id or username
    dh_config: "raw.types.messages.DhConfig" = await app.invoke(GetDhConfig(version=0, random_length=256))
    protocol = PhoneCallProtocol(min_layer=93, max_layer=93, udp_p2p=True,library_versions=[app.app_version])
    random_id, g, p, a = random.randint(0, 0x7fffffff - 1), dh_config.g, int.from_bytes(dh_config.p, 'big'), 0
    while not (1 < a < p - 1):
        # "A chooses a random value of a, 1 < a < p-1"
        a = int.from_bytes(bytes(x ^ y for x, y in zip(os.urandom(256), dh_config.random)), 'little')
    g_a = pow(g, a, p)
    integer_to_bytes = lambda integer: int.to_bytes(
        integer,
        length=(integer.bit_length() + 8 - 1) // 8,  # 8 bits per byte,
        byteorder='big',
        signed=False
    )
    g_a_hash = hashlib.sha256(integer_to_bytes(g_a)).digest()
    peer = await app.resolve_peer(user_id)
    if not isinstance(peer, raw.types.InputPeerUser):
        print("invalid user id")
        return False
    res: "raw.types.phone.PhoneCall" = await app.invoke(
        RequestCall(
            user_id=peer,
            random_id=random_id,
            g_a_hash=g_a_hash,
            protocol=protocol,
            video=False # True to request video call
        )
    )
    print(res)

app.run(main())