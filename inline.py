from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

gg_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Boshlash➡️", callback_data="1")
        ]
    ]
)

fan_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Matematika", callback_data="2"),
            InlineKeyboardButton(text="Fizra", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="Literatura", callback_data="4"),
            InlineKeyboardButton(text="Ximiya", callback_data="5")
        ],
        [
            InlineKeyboardButton(text="Biologiya", callback_data="6"),
            InlineKeyboardButton(text="Angliyski", callback_data="7")
        ]
    ]
)