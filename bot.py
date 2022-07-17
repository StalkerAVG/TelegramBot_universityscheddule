import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)

def groups_button(chat_id):

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

    for name_grp in config.lstgrps:
        group = types.KeyboardButton(name_grp)
        markup.add(group)

    bot.send_message(chat_id, 'Виберіть номер групи.', reply_markup = markup)

@bot.message_handler(commands = ['start','help'])
def welcome_msg(message):

    bot.send_message(message.chat.id,"Привіт я допоможу тобі дізнатися твій розклад занять.\n"
                                     "Щоб розпочати надішли  команду - /schedule")

@bot.message_handler(commands = ['schedule'])
def button_msg(message):

    groups_button(message.chat.id)

@bot.message_handler(content_types=["text"])
def msg_reply(message):

    if message.text in config.lstgrps:

        config.groups[message.chat.id] = message.text
        print(config.groups)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        reset_btn = types.KeyboardButton("Назад")
        markup.add(reset_btn)

        for name_d in config.days:
            day = types.KeyboardButton(name_d)
            markup.add(day)

        bot.send_message(message.chat.id, 'Виберіть день.', reply_markup=markup)

    elif message.text in config.days:

        try:
            photo_path = f'groups/{config.groups[message.chat.id]}/{message.text}.png'

            bot.send_photo(message.chat.id, photo=open(photo_path,'rb'))

            bot.send_message(message.chat.id, f'Розклад на {message.text}')

        except FileNotFoundError:
            bot.send_message(message.chat.id, f'Нажаль на цей день поки що розкладу нема')

    elif message.text == 'Назад':
        groups_button(message.chat.id)

if __name__ == "__main__":
    bot.infinity_polling()