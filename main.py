from gtoken.gtoken import g_token

# import logging

from goofs_bot import *

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
    CallbackContext,
)

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(g_token)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher


    start_handler = CommandHandler('start', start)
    # ttt_handler = CommandHandler('ttt', ttt_)
    # ttt_work_handler = CallbackQueryHandler(ttt_w)
    ttt_handler = ConversationHandler(                          # Filters.text, ttt)
        entry_points=[CommandHandler('ttt', ttt_start)],
        states={
            # START: [MessageHandler(Filters.text, ttt_playx)],
            PLAYO: [CallbackQueryHandler(ttt_playo)],
            PLAYX: [CallbackQueryHandler(ttt_playx)],            #  & ~Filters.command
            OUT:   [CallbackQueryHandler(ttt_fin)],
            # OUT:   [MessageHandler(Filters.update, ttt_fin)]       #  & ~Filters.command
        },
        fallbacks=[CommandHandler('cancel', cancel)], per_user=True
    )
    # Добавляем обработчики
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ttt_handler)
    # dispatcher.add_handler(ttt_work_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()