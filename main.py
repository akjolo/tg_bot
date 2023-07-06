from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CommandHandler
)
from cred import TOKEN
from menu import main_menu_keyboard, course_menu_keyboard
from key_buttons import tele_button,button

def start(update:Update, context: CallbackContext):
    update.message.reply_text(
        f"Welcome {update.effective_user.username}",
        reply_markup=main_menu_keyboard()
    )
def where_are_we(update:Update, context: CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of OGOGO'
    )
    update.message.repl(
        # 42.873650773294, 74.619995927444
        longitude=74.619995927444,
        latitude=42.873650773294,
        reply_to_message_id=msg.message_id
    )
def about_us(update:Update, context: CallbackContext):
    update.message.reply_text(
        f"Академия OGOGO Лицензированный Образовательный центр №1 в Бишкеке! OGOGO - это трамплин в будущее!Только самые востребованные курсы в городе: программирование и английский язык.Мы придерживаемся политики 20% теории и 80% практики. Наши менторы являются опытными специалистами в сфере IT. Молодой и Дружелюбный коллектив. Крутая атмосфера каждый день! Для менторов академии доступна бесплатная коворкинг зона, рабочее место и Wi-Fi. Лучших менторов мы всегда поощряем ценными подарками. Загляни к нам в Instagram, чтобы прочувствовать атмосферу академии! Академия OGOGO -Окунись в мир будущего вместе с нами!",
    )
def resive_course_menu(update:Update, context: CallbackContext):
    update.message.reply_text(
        f"Выберите курс",
        reply_markup=course_menu_keyboard()
    )
def back(update:Update, context: CallbackContext):
    update.message.reply_text(

        reply_markup=main_menu_keyboard()
    )
COURSE_MENU = tele_button[1]    
WHERE_ARE_WE = tele_button[2]
ABOUT_US = tele_button[0]
BACK = button[3]

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    back

))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_MENU),
    resive_course_menu
))
updater.dispatcher.add_handler(MessageHandler(  
    Filters.regex(WHERE_ARE_WE),
    where_are_we
))

updater.dispatcher.add_handler(MessageHandler(  
    Filters.regex(ABOUT_US),
    about_us
))

updater.start_polling()
updater.idle()