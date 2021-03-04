from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!</b>

Lund lega vro???""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Ganna sune", url="https://t.me/anonymousarmy_1"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "takhlif ho kucch?", url="https://t.me/Nidhisupport"
                    ),
                    InlineKeyboardButton(
                        "Update", url="https://t.me/Nidhiupdates"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Namaskar neeche diye gye buttons ka pryog kre, warna maa chudwa....",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Ganna search kre.", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Menu band kre.", callback_data="close"
                    )
                ]
            ]
        )
    )
