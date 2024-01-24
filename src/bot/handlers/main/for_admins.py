from datetime import datetime, timedelta

from aiogram import types, F, Router
from aiogram.types import ChatPermissions
from aiogram.filters.command import Command

router = Router(name=__name__)


@router.message(Command("mute", prefix="/"), F.chat.type != "private")
async def echo_album(message: types.Message):
    if message.from_user.id in ['*******']:
        mute_time = int(message.text.split(" ")[1])
        dt = datetime.now() + timedelta(minutes=mute_time)
        timestamp = dt.timestamp()
        await message.bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            until_date=int(timestamp),
            permissions=ChatPermissions(can_send_other_messages=False)
        )
        await message.answer("OK")
    else:
        return message.answer("no admin")


@router.message(Command("unmute", prefix="/"), F.chat.type != "private")
async def cmd_start(message: types.Message):
    if message.from_user.id in ['*******']:
        await __name__.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(can_send_other_messages=True)
        )
    else:
        await message.answer("no admin")
