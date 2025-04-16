from logger import logger
from typing import Optional
from telegram import Update, User
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from models.bot_steps import BotSteps

async def end_hour(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "זהו עכשיו רק את הטווח העליון באותו פורמט (<HH:MM>) וסיימנו",
    )
    
    await update.message.reply_text(
        "__שים לב__ \n"
        "ניתן להכניס שעות רק __עבור אותו יום__, לכן שעת הסיום חייבת להיות גדולה משעת ההתחלה",
        parse_mode=ParseMode.MARKDOWN_V2
    )

    user: Optional[User] = update.message.from_user
    entered_end_hour: str = update.message.text

    logger.info("End Hour of %s: %s", user.first_name, entered_end_hour)

    return BotSteps.END.value
