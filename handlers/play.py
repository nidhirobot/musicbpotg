from pyrogram import Client, filters
from pyrogram.types import Message

import tgcalls
from converter import convert
from youtube import download
import sira
from config import DURATION_LIMIT
from helpers.wrappers import errors
from helpers.errors import DurationLimitError


@Client.on_message(
    filters.command("play")
    & filters.group
    & ~ filters.edited
)
@errors
async def play(client: Client, message_: Message):
    audio = (message_.reply_to_message.audio or message_.reply_to_message.voice) if message_.reply_to_message else None

    res = await message_.reply_text("Rukk bc kr rha play....")

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"abbe bsdk {DURATION_LIMIT} ki music file allowed nhi, mein toh sirf {audio.duration / 60} tk ki music file play, maa chuda...."
            )

        file_name = audio.file_id + audio.file_name.split(".")[-1]
        file_path = await convert(await message_.reply_to_message.download(file_name))
    else:
        messages = [message_]
        text = ""
        offset = None
        length = None

        if message_.reply_to_message:
            messages.append(message_.reply_to_message)

        for message in messages:
            if offset:
                break

            if message.entities:
                for entity in message.entities:
                    if entity.type == "url":
                        text = message.text or message.caption
                        offset, length = entity.offset, entity.length
                        break

        if offset == None:
            await res.edit_text("Lund play kru??")
            return

        url = text[offset:offset+length]

        file_path = await convert(download(url))

    try:
        is_playing = tgcalls.pytgcalls.is_playing(message_.chat.id)
    except:
        is_playing = False

    if is_playing:
        position = await sira.add(message_.chat.id, file_path)
        await res.edit_text(f"tera gaana {position} pr play krunga mc...")
    else:
        await res.edit_text("Kr rha hun play sun lo bhosdiwalon...")
        tgcalls.pytgcalls.join_group_call(message_.chat.id, file_path, 48000)
