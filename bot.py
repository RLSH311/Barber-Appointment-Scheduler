import logging
from typing import Final, Optional

from models.bot_stages import BotStages
from models.frequency import Frequency, FREQUENCIES, FREQUENCIES_REGEX
from models.day_of_the_week import DayOfTheWeek, DAYS_OF_THE_WEEKS, DAYS_OF_THE_WEEKS_REGEX

from telegram._user import User

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

ACCESS_TOKEN: Final = "7822483945:AAGyZe1gf2cYxC-iNEyLhYBAU2ATL0iTqRI"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start_then_enter_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and ask the user for his email."""

    await update.message.reply_text(
        "נמאס לך שאין לך תורים לספר? עזוב שטויות, תן לי לטפל בזה. \n"
        "נמאס לך לדבר? תשלח /cancel ונעצור את השיחה.\n\n"
        "מה המייל שלך? אם תשלח מייל לא נכון לא תדע שנקבע לך תור אז חבל עליך \n"
        "(עד שלא תכניס מייל תקין אני לא מתקדם) \n",
    )

    return BotStages.FREQUENCY.value


async def set_email_then_enter_frequency(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user: Optional[User] = update.message.from_user
    entered_email: str = update.message.text

    reply_keyboard = [FREQUENCIES]
    placeholder: str = " or ".join(FREQUENCIES) + "?"

    logger.info("Email of %s: %s", user.first_name, entered_email)
    await update.message.reply_text(
        "תודה רבה אח שלנו 💪🏻 \n"
        "עכשיו נוכל לעדכן אותך כשאנחנו מוצאים לך תור. \n"
        "עכשיו תגיד, באיזו תדירות היית רוצה להסתפר?",
        ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder=placeholder
        ),
    )

    return BotStages.INTERVAL.value


async def set_frequency_then_enter_interval(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user: Optional[User] = update.message.from_user
    entered_frequency: str = update.message.text

    logger.info("Frequency of %s: %s", user.first_name, entered_frequency)
    await update.message.reply_text(
        "אוקי זה הצעד הראשון. עכשיו אשמח לדעת מה האינטרוול בו תרצה תור? \n"
        f"לצורך העניין אם הכנסת שהתדירות שלך היא \"{Frequency.WEEKLY}\" ובחרת תדירות X אז יקבע לך תור אחת ל-X {Frequency.WEEKLY}",
        ReplyKeyboardMarkup(
            one_time_keyboard=True, input_field_placeholder="1 - 10"
        ),
    )

    return BotStages.DAY_OF_THE_WEEK.value


# TODO: make the option to insert multiple answers
async def set_interval_then_enter_day_of_the_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user: Optional[User] = update.message.from_user
    entered_frequency: str = update.message.text
    reply_keyboard = [DAYS_OF_THE_WEEKS]

    logger.info("Interval of %s: %s", user.first_name, entered_frequency)
    await update.message.reply_text(
        "אוקי אנחנו עוד מעט מסיימים נשמה שלי, רק ציין לי באילו ימים היית רוצה שאנסה למצוא לך תור? \n"
        "אם תבחר כמה ימים, אבחר תור (יחיד) רנדומלי באחד מהימים הללו",
        ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True
        ),
    )

    return BotStages.START_HOUR.value


async def set_day_of_the_week_then_enter_start_hour(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user: Optional[User] = update.message.from_user
    entered_day: str = update.message.text

    logger.info("Day of %s: %s", user.first_name, entered_day)
    await update.message.reply_text(
        "אין לנו עוד הרבה שלבים כפרה עליך, אני רק צריך שתכניס את טווח השעות שתרצה לקבוע בהן תור."
        "נתחיל מהטווח התחתון: <HH:MM>",
        ReplyKeyboardMarkup(
            one_time_keyboard=True, input_field_placeholder="<HH:MM>"
        ),
    )

    return BotStages.END_HOUR.value


async def set_start_hour_then_enter_end_hour(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user: Optional[User] = update.message.from_user
    entered_start_hour: str = update.message.text

    logger.info("Start Hour of %s: %s", user.first_name, entered_start_hour)
    await update.message.reply_text(
        "זהו עכשיו רק את הטווח העליון וסיינו: <HH:MM>",
        ReplyKeyboardMarkup(
            one_time_keyboard=True, input_field_placeholder="<HH:MM>"
        ),
    )

    return BotStages.END.value

async def set_end_hour_then_end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Stores the selected gender and asks for a photo."""
    user: Optional[User] = update.message.from_user
    entered_start_hour: str = update.message.text

    logger.info("End Hour of %s: %s", user.first_name, entered_start_hour)


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END



def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder() \
        .concurrent_updates(False) \
        .token(ACCESS_TOKEN) \
        .build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start_then_enter_email)],
        states={
            BotStages.FREQUENCY.value: [MessageHandler(filters.Regex("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"), set_email_then_enter_frequency)],
            BotStages.INTERVAL.value: [MessageHandler(filters.Regex(FREQUENCIES_REGEX), set_frequency_then_enter_interval)],
            BotStages.DAY_OF_THE_WEEK.value: [MessageHandler(filters.Regex("^([1-9]|10)$"), set_interval_then_enter_day_of_the_week)],
            BotStages.START_HOUR.value: [MessageHandler(filters.Regex(DAYS_OF_THE_WEEKS_REGEX), set_day_of_the_week_then_enter_start_hour)],
            BotStages.END_HOUR.value: [MessageHandler(filters.Regex("^(?:[01]\d|2[0-3]):[0-5]\d$"), set_start_hour_then_enter_end_hour)],
            BotStages.END.value: [MessageHandler("^(?:[01]\d|2[0-3]):[0-5]\d$", set_end_hour_then_end)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()