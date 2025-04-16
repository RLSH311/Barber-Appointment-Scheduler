from logger import logger
from typing import Optional
from telegram import Update, User
from telegram.ext import ContextTypes

from models.bot_steps import BotSteps

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "מה המייל שלך? אם תשלח מייל לא נכון לא תדע שנקבע לך תור אז חבל עליך \n"
        "(עד שלא תכניס מייל תקין אני לא מתקדם) \n")

    user: Optional[User] = update.message.from_user
    entered_email: str = update.message.text

    logger.info(f"Email of {user.first_name}: {entered_email}")

    return BotSteps.FREQUENCY.value
