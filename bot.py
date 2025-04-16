import logging
from typing import Final, Optional

from models.bot_steps import BotSteps
from models.frequency import Frequency, FREQUENCIES, FREQUENCIES_REGEX, FREQUENCY_MAP_TO_HEBREW
from models.day_of_the_week import DAYS_OF_THE_WEEKS, DAYS_OF_THE_WEEKS_REGEX, DAYS_MAP_TO_HEBREW

from telegram._user import User

from telegram.constants import ParseMode
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from steps.cancel import cancel
from steps.day_of_the_week import day_of_the_week
from steps.email import email
from steps.end import end
from steps.end_hour import end_hour
from steps.frequency import frequency
from steps.interval import interval
from steps.start import start
from steps.start_hour import start_hour

ACCESS_TOKEN: Final = "7822483945:AAGyZe1gf2cYxC-iNEyLhYBAU2ATL0iTqRI"

# async def start_then_enter_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     await update.message.reply_text(
#         "נמאס לך שאין לך תורים לספר? עזוב שטויות, תן לי לטפל בזה. \n"
#         "נמאס לך לדבר? תשלח /cancel ונעצור את השיחה.\n\n"
#         "מה המייל שלך? אם תשלח מייל לא נכון לא תדע שנקבע לך תור אז חבל עליך \n"
#         "(עד שלא תכניס מייל תקין אני לא מתקדם) \n",
#     )

#     return BotSteps.FREQUENCY.value


# async def set_email_then_enter_frequency(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     user: Optional[User] = update.message.from_user
#     entered_email: str = update.message.text

#     placeholder: str = " or ".join(FREQUENCIES)

#     logger.info(f"Email of {user.first_name}: {entered_email}")

#     await update.message.reply_text(
#         "עכשיו נעדכן אותך כשנמצא לך תור 💪🏻 \n\n"
#         "עכשיו תגיד, באיזו תדירות היית רוצה להסתפר?",
#         reply_markup=ReplyKeyboardMarkup(
#             keyboard=[FREQUENCIES], one_time_keyboard=True, input_field_placeholder=placeholder
#         ),
#     )

#     return BotSteps.INTERVAL.value


# async def set_frequency_then_enter_interval(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     user: Optional[User] = update.message.from_user
#     entered_frequency: str = update.message.text

#     await update.message.reply_text(
#         "אוקי זה הצעד הראשון. עכשיו אשמח לדעת מה האינטרוול בו תרצה תור?",
#         reply_markup=ReplyKeyboardRemove()
#     )

#     await update.message.reply_text(
#         f"לצורך העניין אם הכנסת שהתדירות שלך היא \"{Frequency.WEEKLY.name}\" ובחרת תדירות X אז יקבע לך תור אחת ל-X {FREQUENCY_MAP_TO_HEBREW[Frequency.WEEKLY]}",
#     )

#     await update.message.reply_text(
#         "הכנס מספר בין 1 ל-10",
#     )

#     return BotSteps.DAY_OF_THE_WEEK.value


# TODO: make the option to insert multiple answers
# async def set_interval_then_enter_day_of_the_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     user: Optional[User] = update.message.from_user
#     entered_frequency: str = update.message.text
#     reply_keyboard = [DAYS_OF_THE_WEEKS]
#     placeholder: str = " or ".join(DAYS_OF_THE_WEEKS)

#     logger.info("Interval of %s: %s", user.first_name, entered_frequency)
#     await update.message.reply_text(
#         "אוקי אנחנו עוד מעט מסיימים נשמה שלי, רק ציין לי באילו ימים היית רוצה שאנסה למצוא לך תור?",
#         reply_markup=ReplyKeyboardRemove()
#     )
#     await update.message.reply_text(
#         "אמצא לך תורים לפי התדירות והאינטרוול שהזנת, אך ורק בימים שאתה מעוניין בהם",
#         reply_markup=ReplyKeyboardMarkup(
#             reply_keyboard, one_time_keyboard=True, input_field_placeholder=placeholder),
#     )


#     return BotSteps.START_HOUR.value


# async def set_day_of_the_week_then_enter_start_hour(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     user: Optional[User] = update.message.from_user
#     entered_day: str = update.message.text

#     logger.info("Day of %s: %s", user.first_name, entered_day)
#     await update.message.reply_text(
#         "אין לנו עוד הרבה שלבים כפרה עליך, אני רק צריך שתכניס את טווח השעות שתרצה לקבוע בהן תור.",
#         reply_markup=ReplyKeyboardRemove()
#     )
#     await update.message.reply_text(
#         "נתחיל מהטווח התחתון בפורמט הבא בלבד <HH:MM> ושעה תקנית",
#     )

#     return BotSteps.END_HOUR.value


# async def set_start_hour_then_enter_end_hour(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     user: Optional[User] = update.message.from_user
#     entered_start_hour: str = update.message.text

#     logger.info("Start Hour of %s: %s", user.first_name, entered_start_hour)
#     await update.message.reply_text(
#         "זהו עכשיו רק את הטווח העליון באותו פורמט (<HH:MM>) וסיימנו",
#     )
    
#     await update.message.reply_text(
#         "__שים לב__ \n"
#         "ניתן להכניס שעות רק __עבור אותו יום__, לכן שעת הסיום חייבת להיות גדולה משעת ההתחלה",
#         parse_mode=ParseMode.MARKDOWN_V2
#     )

#     return BotSteps.END.value

# async def set_end_hour_then_end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user: Optional[User] = update.message.from_user
#     entered_start_hour: str = update.message.text

#     logger.info("End Hour of %s: %s", user.first_name, entered_start_hour)

#     await update.message.reply_text(
#         "לסיכום: \n"
#         f"אקבע לך תור בין השעות {1}-{2} בכל יום {1} אחת ל-{1} {1} \n"
#         f"אני אודיע למייל {2}",
#         reply_markup=ReplyKeyboardRemove()
#     )


# async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Cancels and ends the conversation."""
#     user = update.message.from_user
#     logger.info("User %s canceled the conversation.", user.first_name)
#     await update.message.reply_text(
#         "לא חייב לקבוע עכשיו, אפשר גם במועד אחר. פשוט תפנה אליי בפקודת /start", reply_markup=ReplyKeyboardRemove()
#     )

#     return ConversationHandler.END



def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder() \
        .concurrent_updates(False) \
        .token(ACCESS_TOKEN) \
        .build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            BotSteps.EMAIL.value: [MessageHandler(filters.ALL, email)],
            # BotSteps.EMAIL.value: [MessageHandler(filters.Regex("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"), email)],
            BotSteps.FREQUENCY.value: [MessageHandler(filters.Regex("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"), frequency)],
            BotSteps.INTERVAL.value: [MessageHandler(filters.Regex(FREQUENCIES_REGEX), interval)],
            BotSteps.DAY_OF_THE_WEEK.value: [MessageHandler(filters.Regex("^([1-9]|10)$"), day_of_the_week)],
            BotSteps.START_HOUR.value: [MessageHandler(filters.Regex(DAYS_OF_THE_WEEKS_REGEX), start_hour)],
            BotSteps.END_HOUR.value: [MessageHandler(filters.Regex("^(?:[01]\\d|2[0-3]):[0-5]\\d$"), end_hour)],
            BotSteps.END.value: [MessageHandler(filters.Regex("^(?:[01]\\d|2[0-3]):[0-5]\\d$"), end)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# TODO: Add Error Handlers
if __name__ == "__main__":
    main()