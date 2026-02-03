from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ Bot Status ✨", url="https://t.me/kryshupdate")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Bots ♥", url="https://t.me/kryshupdate")],
    ]

    START = """
Hey {}

Welcome to {}

If you don't trust this bot,
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate Pyrogram (even v2) and Telethon string session.

Use below buttons to learn more!

By @kryshupdate
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - Help Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Restart the process
"""

    ABOUT = """
**About This Bot**

Telegram Bot to generate Pyrogram and Telethon string sessions.

Made with ❤️ by @kryshupdate

Framework : Pyrogram
Language  : Python
    """
