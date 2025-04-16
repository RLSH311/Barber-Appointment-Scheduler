from logger import logger
from typing import Optional
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, User
from telegram.ext import ContextTypes

from models.bot_steps import BotSteps
from models.day_of_the_week import DAYS_OF_THE_WEEKS

async def day_of_the_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [DAYS_OF_THE_WEEKS]
    placeholder: str = " or ".join(DAYS_OF_THE_WEEKS)

    await update.message.reply_text(
        "אוקי אנחנו עוד מעט מסיימים נשמה שלי, רק ציין לי באילו ימים היית רוצה שאנסה למצוא לך תור?",
        reply_markup=ReplyKeyboardRemove()
    )
    await update.message.reply_text(
        "אמצא לך תורים לפי התדירות והאינטרוול שהזנת, אך ורק בימים שאתה מעוניין בהם",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder=placeholder),
    )

    user: Optional[User] = update.message.from_user
    entered_day_of_the_week: str = update.message.text
    
    logger.info("Day Of The Week of %s: %s", user.first_name, entered_day_of_the_week)

    return BotSteps.START_HOUR.value
