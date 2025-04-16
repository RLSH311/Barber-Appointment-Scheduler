from logger import logger
from typing import Optional
from telegram import ReplyKeyboardRemove, Update, User
from telegram.ext import ContextTypes

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user: Optional[User] = update.message.from_user

    await update.message.reply_text(
        "לסיכום: \n"
        f"אקבע לך תור בין השעות {1}-{2} בכל יום {1} אחת ל-{1} {1} \n"
        f"אני אודיע למייל {2}",
        reply_markup=ReplyKeyboardRemove()
    )
