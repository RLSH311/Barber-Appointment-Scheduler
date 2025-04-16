from logger import logger
from typing import Optional
from models.frequency import FREQUENCIES


from telegram import ReplyKeyboardMarkup, Update, User
from telegram.ext import ContextTypes

from models.bot_steps import BotSteps

async def frequency(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    placeholder: str = " or ".join(FREQUENCIES)

    await update.message.reply_text(
        "עכשיו תגיד, באיזו תדירות היית רוצה להסתפר?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[FREQUENCIES], one_time_keyboard=True, input_field_placeholder=placeholder
        ),
    )

    user: Optional[User] = update.message.from_user
    entered_frequency: str = update.message.text

    logger.info("Frequency of %s: %s", user.first_name, entered_frequency)

    return BotSteps.INTERVAL
