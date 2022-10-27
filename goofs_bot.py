import logging
from tictac import TicTac #!

from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    # filename='bot_logs.csv'
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
GENDER, PHOTO, LOCATION, BIO = range(4)

# функция обратного вызова точки входа в разговор
def start(update, _):
    # Список кнопок для ответа
    # user = update.message.from_user.first_name
    update.message.reply_text(f'Добро пожаловать {update.message.from_user.first_name}!\nК сожалению в данный момент бот умеет\
 только играть в Крестики-Нолики для двоих игроков %))\nЗапуск командой /ttt')

# Обрабатываем команду /skip для фото
def skip_photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        'Держу пари, ты выглядишь великолепно! А теперь пришлите мне'
        ' свое местоположение, или /skip если параноик.'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END

PLAYX, PLAYO, OUT, NEXT, START = range(5)
game = TicTac()

def ttt_cancel(update, c):
    return ConversationHandler.END

def ttt_start(update, c):
    # print(c)
    # print(update)
    # global game
    update.message.reply_text(game.rules())# 3x3 keyboard
    reply_keyboard = reNewtttKeyboard()
    reply_markup = InlineKeyboardMarkup(reply_keyboard)                 # Создаем Inline клавиатуру для ответа
    update.message.reply_text(game.pmove(), reply_markup=reply_markup)  # Пишем текущего игрока
    return PLAYO

def ttt_playx(update, c):
    query = update.callback_query
    query.answer()
    pos = int(query.data)
    # print(pos)
    query.edit_message_text(text = game.pmove() + f"\nSelected option: {pos+1}")
    if game.possible_moves[pos]:
        game.possible_moves[pos] = 0
        game.move(pos)
        game.fd[pos] = game.player
        if game.finished() or sum(game.possible_moves) == 0:
            query.edit_message_text(text = "Игра завершена")
            return OUT
        else:
            game.cplayer()
            reply_keyboard = reNewtttKeyboard()
            reply_markup = InlineKeyboardMarkup(reply_keyboard)              # Создаем Inline клавиатуру для ответа
            query.edit_message_text(game.pmove(), reply_markup=reply_markup) # Пишем текущего игрока
    else:
        update.message.reply_text(game.fu)
        return PLAYX
    return PLAYO

def ttt_playo(update, c):
    query = update.callback_query
    query.answer()
    pos = int(query.data)
    # print(pos)
    query.edit_message_text(text = game.pmove() + f"\nSelected option: {pos+1}")
    if game.possible_moves[pos]:
        game.possible_moves[pos] = 0
        game.move(pos)
        game.fd[pos] = game.player
        if game.finished() or sum(game.possible_moves) == 0:
            query.edit_message_text(text = "Игра завершена")
            return OUT
        else:
            game.cplayer()
            reply_keyboard = reNewtttKeyboard() 
            reply_markup = InlineKeyboardMarkup(reply_keyboard)              # Создаем Inline клавиатуру для ответа
            query.edit_message_text(game.pmove(), reply_markup=reply_markup) # Пишем текущего игрока
    else:
        update.message.reply_text(game.fu)
        return PLAYO
    return PLAYX

def ttt_fin(update, c):
    # update.message.reply_text(game)
    winner = game.finished()
    print(winner)
    if winner:
        update.message.reply_text(game.win())
    else:
        update.message.reply_text(game.draw)
    game.__init__()
    return ConversationHandler.END

def reNewtttKeyboard():
    return [[
            InlineKeyboardButton(game.fd[0], callback_data='0'),
            InlineKeyboardButton(game.fd[1], callback_data='1'),
            InlineKeyboardButton(game.fd[2], callback_data='2'),
        ],[ InlineKeyboardButton(game.fd[3], callback_data='3'),
            InlineKeyboardButton(game.fd[4], callback_data='4'),
            InlineKeyboardButton(game.fd[5], callback_data='5'),
        ],[ InlineKeyboardButton(game.fd[6], callback_data='6'),
            InlineKeyboardButton(game.fd[7], callback_data='7'),
            InlineKeyboardButton(game.fd[8], callback_data='8'),]]