from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Heroku.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME

HELP_TEXT = """
ʜᴇʏᴀ! [{}](tg://user?id={})
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ ɪ'ᴍ ᴊᴜꜱᴛ ɴᴏᴛ ᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ ɪ ʜᴀᴠᴇ ʟᴏᴛꜱ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ʏᴏᴜ ʟɪᴋᴇꜱ ᴛʜᴀᴛ.
‣ ɪ ᴄᴀɴ ᴘʟᴀʏ ᴀᴜᴅɪᴏ+ᴠɪᴅᴇᴏ ʙᴏᴛʜ.
‣ ɪ ʜᴀᴠᴇ ᴀʟᴍᴏꜱᴛ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ɴᴇᴇᴅꜱ ᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ 🔘 ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️.
"""


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{HELP_TEXT}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATE}"),
                    InlineKeyboardButton(
                        "ᴏᴛʜᴇʀs", callback_data="others")
                ]
           ]
        ),
    )






@Client.on_callback_query(filters.regex("others"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏʏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗯️ ʜᴇʀᴏᴋᴜ", url=f"https://heroku.com"),
                    InlineKeyboardButton(
                        "ɢɪᴛʜᴜʙ", url=f"https://github.com/Itz-Zaid")
                ],
                [
                    InlineKeyboardButton(
                        "ᴄʀᴇᴅɪᴛs", callback_data="credit"),
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ ɪɴғᴏ", callback_data="repoinfo")
                ],
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="home")
                ]
           ]
        ),
    )


@Client.on_callback_query(filters.regex("credit"))
async def credit(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴄʀᴇᴅɪᴛs ғᴏʀ ᴛʜɪs ʙᴏᴛ

• @{OWNER_USERNAME}
- ʙᴏᴛ ᴏᴡɴᴇʀ


ᴛʜᴀɴᴋs ᴀ ʟᴏᴛ ғᴏʀ ᴄᴏɴᴛʀɪʙᴜᴛɪɴɢ ʏᴏᴜʀ ᴛɪᴍᴇ ᴀɴᴅ sᴋɪʟʟs !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="others")
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cls"))
async def reinfo(_, query: CallbackQuery):
    try:
        await query.message.delete()
        await query.message.reply_to_message.delete()
    except Exception:
        pass


@Client.on_callback_query(filters.regex("repoinfo"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴀʙᴏᴜᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : 

ᴛʜɪs ʀᴇᴘᴏ ɪs ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴅᴇᴘʟᴏʏɪɴɢ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ғᴀᴄɪɴɢ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴɴɪɴɢ ᴘʀᴏʙᴇʟᴍ.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="others")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
