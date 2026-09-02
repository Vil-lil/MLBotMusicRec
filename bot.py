import telebot
from telebot import types
from ClassOfRecomad import RecommendationsInterface
class Bot:
    RI = RecommendationsInterface()

    def __int__(self, token: str, pull: bool) -> None:

        '''
        :param token:
        :param pull:
        :return: None

        Документация:
        Функция отвечает за создание экзепляра класса.
        Грубо говоря - этот класс сформерованный бот для упрощения понимания создания бота на уровне абстракции.
        '''

        self.TOKEN = token
        self.PULL = pull

    def START_BOT(self) -> bool:

        try:
            self.BOT = telebot.TeleBot(self.TOKEN)
            return True

        except:

            raise "Ошибка на уровне создаия бота. Ошибка токена"

    def run(self):
        @self.BOT.massage_halder(comands=["start"])
        def start(self, massage):
            self.BOT.send_message(massage.from_user.id, text="Это бот по рекомендации музыки. Воспользуйтесь командой /play, чтобы начать.")





a = []
def clear():
    a.pop()
    a.pop()
    a.pop()
bot = telebot.TeleBot('6096982087:AAEpuOABIe8Q6UMHzxLxY1Wx-QXiIECFyqk')
RI = RecommendationsInterface()
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, text='Это бот по рекомендации музыки. Воспользуйтесь командой /play, чтобы начать.')
@bot.message_handler(content_types=['text'])
def get_genre(message):
    if message.text == '/play':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        rock = types.InlineKeyboardButton(text='рок', callback_data='rock');  # кнопка «Да»
        keyboard.add(rock)  # добавляем кнопку в клавиатуру
        pop = types.InlineKeyboardButton(text='поп', callback_data='pop');
        keyboard.add(pop)
        classic = types.InlineKeyboardButton(text='классика', callback_data='classic');  # кнопка «Да»
        keyboard.add(classic)  # добавляем кнопку в клавиатуру
        rap = types.InlineKeyboardButton(text='рэп', callback_data='rap');
        keyboard.add(rap)
        question = 'Какой жанр вы хотите послушать?';
        metal = types.InlineKeyboardButton(text='метал', callback_data='metal');  # кнопка «Да»
        keyboard.add(metal)  # добавляем кнопку в клавиатуру
        indie = types.InlineKeyboardButton(text='инди', callback_data='indie');
        keyboard.add(indie)
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
def get_act(id):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    sleep = types.InlineKeyboardButton(text='засыпаю', callback_data='sleep')  # кнопка «Да»
    keyboard.add(sleep) # добавляем кнопку в клавиатуру
    wu = types.InlineKeyboardButton(text='просыпаюсь', callback_data='wu');
    keyboard.add(wu)
    sport= types.InlineKeyboardButton(text='тренируюсь', callback_data='sport');  # кнопка «Да»
    keyboard.add(sport)  # добавляем кнопку в клавиатуру
    driving = types.InlineKeyboardButton(text='вожу авто', callback_data='driving');
    keyboard.add(driving)
    question = 'Чем вы сейчас занимаетесь?'
    working = types.InlineKeyboardButton(text='работаю', callback_data='working');  # кнопка «Да»
    keyboard.add(working)  # добавляем кнопку в клавиатуру
    bot.send_message(id, text=question, reply_markup=keyboard)
def get_mood(id):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    cheerful= types.InlineKeyboardButton(text='бодрое', callback_data='cheerful')  # кнопка «Да»
    keyboard.add(cheerful)  # добавляем кнопку в клавиатуру
    sad = types.InlineKeyboardButton(text='грустное', callback_data='sad')
    keyboard.add(sad)
    calm = types.InlineKeyboardButton(text='спокойное', callback_data='calm') # кнопка «Да»
    keyboard.add(calm) # добавляем кнопку в клавиатуру
    question = 'Какое у вас сейчас настроение?'
    bot.send_message(id, text=question, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "rock" and len(a) == 0:
        a.append('рок')
        get_act(call.message.chat.id)
    elif call.data == "pop" and len(a) == 0:
        a.append('поп')
        get_act(call.message.chat.id)
    elif call.data == "classic" and len(a) == 0:
        a.append('классика')
        get_act(call.message.chat.id)
    elif call.data == "rap" and len(a) == 0:
        genre = 'реп'
        get_act(call.message.chat.id)
    elif call.data == "metal" and len(a) == 0:
        a.append('металл')
        get_act(call.message.chat.id)
    elif call.data == "indie" and len(a) == 0:
        a.append('инди')
        get_act(call.message.chat.id)
    elif call.data == "pop" and len(a) == 0:
        a.append('поп')
        get_act(call.message.chat.id)
    elif call.data == "sleep" and len(a) == 1:
        a.append('засыпаю')
        get_mood(call.message.chat.id)
    elif call.data == "wu" and len(a) == 1:
        a.append('просыпаюсь')
        get_mood(call.message.chat.id)
    elif call.data == "sport" and len(a) == 1:
        a.append('тренируюсь')
        get_mood(call.message.chat.id)
    elif call.data == "driving" and len(a) == 1:
        a.append('в дороге')
        get_mood(call.message.chat.id)
    elif call.data == "working" and len(a) == 1:
        a.append('работаю')
        get_mood(call.message.chat.id)
    elif call.data == 'cheerful' and len(a) == 2:
        a.append('бодрое')
        bot.send_message(call.message.chat.id, text=RI.NewMlModel(a)+'\n'+'Чтобы найти снова, впишите команду /play')
        clear()
    elif call.data == 'sad' and len(a) == 2:
        a.append('грустное')
        bot.send_message(call.message.chat.id, text=RI.NewMlModel(a)+'\n'+'Чтобы найти снова, впишите команду /play')
        clear()
    elif call.data == 'calm' and len(a) == 2:
        a.append('спокойное')
        bot.send_message(call.message.chat.id, text=RI.NewMlModel(a)+'\n'+'Чтобы найти снова, впишите команду /play')
        clear()
bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть