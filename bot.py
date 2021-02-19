import telebot;
from telebot import types;
bot = telebot.TeleBot('1682748377:AAHybTTBzwPszmTqE32pLb2hggEL9SkpXek');

name = '';
surname = '';
age = 0;

@bot.message_handler(content_types=['text'])
def start(message):
    if "ривет" in message.text :
        bot.send_message(message.from_user.id, "Здорова, чорт");
        bot.send_message(message.from_user.id, "Если хочешь побазарить, то чиркани /reg");
    elif  message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут, пидр?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg и не смей выебываться');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия,а?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id,'Ема смешная, а что не Пупкин?');
    bot.send_message(message.from_user.id,'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, блять');
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
    keyboard.add(key_yes); #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
    bot.send_message(message.from_user.id,'Не знаю, кому не похуй, но теперь я знаю о тебе все и расскажу федералам,какой ты пидарас');
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
         #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню. Или нет. Вообще ты нахуй мне не нужон, как и интернет ваш. Я бы выпилился из-за таких пидарасов как ты , но я сука бот. Пошли вы все нахуй');
    elif call.data == "no":
          bot.send_message(call.message.chat.id, 'Блять, опять с тобой переписываться : )');
        
bot.polling(none_stop=True, interval=0)