from logger import logger
from typing import Optional
from telegram import ReplyKeyboardRemove, Update, User
from telegram.ext import ContextTypes

from models.bot_steps import BotSteps

async def start_hour(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "אין לנו עוד הרבה שלבים כפרה עליך, אני רק צריך שתכניס את טווח השעות שתרצה לקבוע בהן תור.",
        reply_markup=ReplyKeyboardRemove()
    )
    await update.message.reply_text(
        "נתחיל מהטווח התחתון בפורמט הבא בלבד <HH:MM> ושעה תקנית",
    )

    user: Optional[User] = update.message.from_user
    entered_start_hour: str = update.message.text

    logger.info("Start Hour of %s: %s", user.first_name, entered_start_hour)

    return BotSteps.END_HOUR.value
