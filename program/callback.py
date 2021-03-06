# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â¨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
ð­ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) [ð§](https://telegra.ph/file/f4e1c2ebc7a14110faf47.jpg)**

 **Éª'á´ á´ á´á´á´ á´É´á´á´ á´á´sÉªá´ á´ Éªá´á´á´ Êá´Êá´á´

âââââââââââââââââââ
â£Â» á´á´ á´á´ê±Éªá´ á´Êá´Êá´Ê Êá´á´. 
â£Â» ÊÉªÉ¢Ê Ç«á´á´ÊÉªá´Ê á´á´ê±Éªá´.
â£Â» á´ Éªá´á´á´ á´Êá´Ê ê±á´á´á´á´Êá´á´á´.
â£Â» á´á´á´ á´É´á´á´á´ ê°á´á´á´á´Êá´ê±.
â£Â» ê±á´á´á´Êê°á´ê±á´ ê±á´á´á´á´.
âââââââââââââââââââ**

ð **á´á´ê±ÉªÉ¢É´á´á´ ÊÊ : [Êá´á´á´á´Ê](https://t.me/The_cat_lover0)**""",
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


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

ð **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

ð¡ **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

â¡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð á´á´á´á´¡", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â¨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

Â» **press the button below to read the explanation and see the list of available commands !**

â¡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ð·ð» á´Êá´ á´á´á´", callback_data="cbadmin"),
                    InlineKeyboardButton("ð§ð» Êá´á´á´á´Ê á´á´á´", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("ð É´ÉªÊÊá´ á´á´á´", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("ð á´á´á´á´¡", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® here is the basic commands:

Â» /play (song name/link) - play music on video chat
Â» /vplay (video name/link) - play video on video chat
Â» /vstream - play live video from yt live/m3u8
Â» /playlist - show you the playlist
Â» /video (query) - download video from youtube
Â» /song (query) - download song from youtube
Â» /lyric (query) - scrap the song lyric
Â» /search (query) - search a youtube video link

Â» /ping - show the bot ping status
Â» /uptime - show the bot uptime status
Â» /alive - show the bot alive info (in group)

â¡ï¸ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð á´á´á´á´¡", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® here is the admin commands:

Â» /pause - pause the stream
Â» /resume - resume the stream
Â» /skip - switch to next stream
Â» /stop - stop the streaming
Â» /vmute - mute the userbot on voice chat
Â» /vunmute - unmute the userbot on voice chat
Â» /volume `1-200` - adjust the volume of music (userbot must be admin)
Â» /reload - reload bot and refresh the admin data
Â» /userbotjoin - invite the userbot to join group
Â» /userbotleave - order userbot to leave from group

â¡ï¸ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð á´á´á´á´¡", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® here is the sudo commands:

Â» /rmw - clean all raw files
Â» /rmd - clean all downloaded files
Â» /sysinfo - show the system information
Â» /update - update your bot to latest version
Â» /restart - restart your bot
Â» /leaveall - order userbot to leave from all group

â¡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð á´á´á´á´¡", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nÂ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"âï¸ **settings of** {query.message.chat.title}\n\nâ¸ : pause stream\nâ¶ï¸ : resume stream\nð : mute userbot\nð : unmute userbot\nâ¹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("â¹", callback_data="cbstop"),
                      InlineKeyboardButton("â¸", callback_data="cbpause"),
                      InlineKeyboardButton("â¶ï¸", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("ð", callback_data="cbmute"),
                      InlineKeyboardButton("ð", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("ð á´Êá´sá´", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("â nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
