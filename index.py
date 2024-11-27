from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# START buyrug'i
def start(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [["Русский", "O'zbek", "English"]]
    update.message.reply_text(
        "Добро пожаловать! Tilni tanlang / Choose a language:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

# Til tanlash
def select_language(update: Update, context: CallbackContext) -> None:
    language = update.message.text
    context.user_data["language"] = language
    phone_button = [[KeyboardButton("📱 Telefon raqamni ulashish", request_contact=True)]]
    update.message.reply_text(
        "Iltimos, telefon raqamingizni ulashing / Пожалуйста, поделитесь вашим номером:",
        reply_markup=ReplyKeyboardMarkup(phone_button, one_time_keyboard=True)
    )

# Telefon raqam olish
def get_phone(update: Update, context: CallbackContext) -> None:
    contact = update.message.contact.phone_number
    context.user_data["phone"] = contact
    update.message.reply_text(f"Rahmat! Telefon raqamingiz: {contact}\nIltimos, joylashuvingizni yuboring.")
    location_button = [[KeyboardButton("📍 Joylashuvni ulashish", request_location=True)]]
    update.message.reply_text(
        "Joylashuvingizni ulashing / Поделитесь вашим местоположением:",
        reply_markup=ReplyKeyboardMarkup(location_button, one_time_keyboard=True)
    )

# Joylashuv olish
def get_location(update: Update, context: CallbackContext) -> None:
    location = update.message.location
    context.user_data["location"] = (location.latitude, location.longitude)
    update.message.reply_text("Rahmat! Endi buyurtma qilish uchun mahsulotlarni tanlang.")

def main() -> None:
    updater = Updater("7448843227:AAGQ4uimKtqdeVQt0qd-dpqhHumeULBe488")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, select_language))
    dispatcher.add_handler(MessageHandler(Filters.contact, get_phone))
    dispatcher.add_handler(MessageHandler(Filters.location, get_location))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
