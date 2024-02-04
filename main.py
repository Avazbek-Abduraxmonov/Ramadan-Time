import telebot

bot = telebot.TeleBot(token = 'TELEGRAM_BOT_API_TOKEN', parse_mode = 'HTML')

users = []

@bot.message_handler(commands = ['start'])
def start(message):
  markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
  day = telebot.types.KeyboardButton('☪ Roza kunlari')
  dev = telebot.types.KeyboardButton('🧑‍💻 Dasturchi')
  status = telebot.types.KeyboardButton('📊 Statistika')
  docs = telebot.types.KeyboardButton('📄 Docs')
  markup.add(day)
  markup.add(dev,docs)
  markup.add(status)

  user_id = message.from_user.id
  if user_id not in users:
      users.append(user_id)

  bot.send_message(message.chat.id, "Assalomu Alaykum va Rahmatullohu va Barokatuh\nSizga<b> Paxtakor taqvimini korsatib beramiz</b>", reply_markup = markup)



@bot.message_handler(func=lambda message: message.text == '🧑‍💻 Dasturchi')
def developer(msg):
  markup = telebot.types.InlineKeyboardMarkup()
  button = telebot.types.InlineKeyboardButton('Blog', url='https://t.me/AvazbekDev')
  markup.add(button)
  bot.send_message(msg.chat.id, 'Dasturchi: @avazbek_dev', reply_markup = markup)


    # Yangi obunachini qo'shish

@bot.message_handler(func= lambda message: message.text == '📊 Statistika')
def send_stats(message):
    # Statistika ko'rish
    total_users = len(users)
    bot.send_message(message.chat.id, f"@Ramazontimeuzbot ni obunachilari\n\n📊Subscribes: {total_users} ta")


@bot.message_handler(func = lambda message: message.text == '📄 Docs')
def docs(message):
  bot.send_message(message.chat.id, "Docs: https://t.me/Ramazontimeuzbot/1")


@bot.message_handler(func=lambda message: message.text == '☪ Roza kunlari')
def ramadan(message):
    bot.send_message(message.chat.id, 'Kun kiriting\n\nMasalan: 11 mart')




@bot.message_handler(func=lambda message: True)
def handle_date(message):
  try:
    user_msg = message.text
    if user_msg == '11 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '12 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '13 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '14 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '15 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '16 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '17 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '18 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '19 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '20 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '21 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '22 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '23 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '24 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '25 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '26 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '27 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '28 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '29 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '30 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '31 mart':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..')
    elif user_msg == '1 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '2 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '3 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '4 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '5 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '6 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '7 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '8 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '9 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '10 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    elif user_msg == '11 aprel':
      bot.send_message(message.chat.id, 'Yopish vaqti: ..:..\n\nOchish vaqti: ..:..')
    else:
        bot.send_message(message.chat.id, 'Gapingizni tushunmadim')
  except:
    bot.send_message(message.chat.id, 'Xatolik boldi oziroq kutib turing\n\nAdmin: @avazbek_dev')
if __name__ == '__main__':
  bot.polling(none_stop = True)
