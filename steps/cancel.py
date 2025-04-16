from logger import logger
from telegram.ext import (ConversationHandler, ContextTypes)
from telegram import ReplyKeyboardRemove, Update

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)

    await update.message.reply_text(
        "לא חייב לקבוע עכשיו, אפשר גם במועד אחר. פשוט תפנה אליי בפקודת /start", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
