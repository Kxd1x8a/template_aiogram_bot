from aiogram import F, Router
from aiogram.types import Message
from src.bot.types import Album

router = Router(name=__name__)


@router.message(F.media_group_id)
async def echo_album(message: Message, album: Album):
    return album.copy_to(chat_id=message.chat.id)


@router.message()
async def echo_message(message: Message):
    try:
        return message.send_copy(message.chat.id)
    except TypeError:
        return message.answer("i can't copy it.")
