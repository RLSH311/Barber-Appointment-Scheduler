from logger import logger
from typing import Optional
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, User
from telegram.ext import ContextTypes

from models.bot_steps import BotSteps
from models.frequency import FREQUENCY_MAP_TO_HEBREW, Frequency

async def interval(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "עכשיו אשמח לדעת מה האינטרוול בו תרצה תור?",
        reply_markup=ReplyKeyboardRemove()
    )

    await update.message.reply_text(
        f"לצורך העניין אם הכנסת שהתדירות שלך היא \"{Frequency.WEEKLY.name}\" ובחרת תדירות X אז יקבע לך תור אחת ל-X {FREQUENCY_MAP_TO_HEBREW[Frequency.WEEKLY]}",
    )

    await update.message.reply_text(
        "הכנס מספר בין 1 ל-10",
    )

    user: Optional[User] = update.message.from_user
    entered_interval: str = update.message.text

    logger.info(f"Interval of {user.first_name}: {entered_interval}")

    return BotSteps.DAY_OF_THE_WEEK.value
