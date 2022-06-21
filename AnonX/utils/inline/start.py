from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="[►➕Add Me To Your Chat➕◄]",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="[►Help◄]",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="[►Settings◄]", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="[►👑Owner👑◄]", user_id=OWNER),
            InlineKeyboardButton(
                text="[►Support💬◄]", url=f"{config.SUPPORT_GROUP}"
            ),
        ],[
            InlineKeyboardButton(
                text="[►New Update Or More🔔◄]",
                url="https://t.me/AerodynamicV1_UPDATE",
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="[►➕Add Me To Your Chat➕◄]",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="[►Help◄]", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="[►Developer◄]", user_id=OWNER),
            InlineKeyboardButton(
                text="[►Support💬◄]", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="[►Source Code◄]", url=f"{config.UPSTREAM_REPO}"
                ),InlineKeyboardButton(
                text="[►Update🔔◄]", url="https://t.me/AerodynamicV1_UPDATE"
            ),
        ],
     ]
    return buttons
