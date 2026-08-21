from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💬 Связь", url="https://t.me/chap1to"),
            InlineKeyboardButton(text="📢 Канал", url="https://t.me/infernalSoft")
         ],
         [
             InlineKeyboardButton(text="⚡Репутация", url="https://t.me/repatag"),
             InlineKeyboardButton(text="💲Услуги и цены", url="https://t.me/pricechapito")
         ],
         [
             InlineKeyboardButton(text="💡Проекты", url="https://t.me/projectchapito")
         ]
    ]
)