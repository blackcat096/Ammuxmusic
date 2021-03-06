from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""â¨ **Welcome {message.from_user.mention()} !**\n
ð­ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) [ð§](https://telegra.ph/file/f4e1c2ebc7a14110faf47.jpg)]**

Éª'á´ á´ á´á´á´ á´É´á´á´ á´á´sÉªá´ á´ Éªá´á´á´ Êá´Êá´á´

âââââââââââââââââââ
â£Â» á´á´ á´á´ê±Éªá´ á´Êá´Êá´Ê Êá´á´. 
â£Â» ÊÉªÉ¢Ê Ç«á´á´ÊÉªá´Ê á´á´ê±Éªá´.
â£Â» á´ Éªá´á´á´ á´Êá´Ê ê±á´á´á´á´Êá´á´á´.
â£Â» á´á´á´ á´É´á´á´á´ ê°á´á´á´á´Êá´ê±.
â£Â» ê±á´á´á´Êê°á´ê±á´ ê±á´á´á´á´.
âââââââââââââââââââ

ð **á´á´ê±ÉªÉ¢É´á´á´ ÊÊ : [Êá´á´á´á´Ê](https://t.me/The_cat_lover0)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â á´á´á´ á´á´ Êá´ÊÊ â",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("âÊá´sÉªá´", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("á´á´sÉªá´ á´á´á´", callback_data="cbcmds"),
                    InlineKeyboardButton("Êá´á´á´á´Ê", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "É´á´á´á´¡á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "á´á´á´á´¡", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "sá´á´Êá´á´", url="https://telegra.ph/-01-05-492"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¨ Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "ð£ Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\nâ¨ Bot is working normally\nð My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\nâ¨ Bot Version: `v{__version__}`\nð Pyrogram Version: `{pyrover}`\nâ¨ Python Version: `{__python_version__}`\nð PyTgCalls version: `{pytover.__version__}`\nâ¨ Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing video & music on your Group's video chat** â¤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("ð `PONG!!`\n" f"â¡ï¸ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "ð¤ bot status:\n"
        f"â¢ **uptime:** `{uptime}`\n"
        f"â¢ **start time:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "â¤ï¸ Thanks for adding me to the **Group** !\n\n"
                "Appoint me as administrator in the **Group**, otherwise I will not be able to work properly, and don't forget to type `/userbotjoin` for invite the assistant.\n\n"
                "Once done, then type `/reload`",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ð£ Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("ð­ Support", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("ð¤ Assistant", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
