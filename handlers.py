from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards import main_kb

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer_photo(
        photo="https://i.pinimg.com/736x/5d/3c/3a/5d3c3ab24930e481d97d31d35df03525.jpg",
        caption=(
            f"Йоу <b> {message.from_user.first_name} </b>, Это мой adapter или же переходник на мои проекты, прайс, услуги, каналы, юзернеймы и в общем все обо мне"
        ),
        reply_markup=main_kb
   )

@router.message(Command("repa"))
async def repa_cmd(message: Message):
    await message.answer(f"<b> Вот мои отзывы </b> --- @repatag")

@router.message(Command("channel"))
async def channel_cmd(message: Message):
    await message.answer(f"<b> Вот мой канал </b> --- @infernalSoft")

@router.message(Command("username"))
async def username_cmd(message: Message):
    await message.answer(f"<b> Вот список моих юзернеймов </b> --- @chap1to @vktag @brabus6x6")

@router.message(Command("price"))
async def price_cmd(message: Message):
    await message.answer(f"<b> Вот мои услуги и цены на всё </b> --- @pricechapito")