import random

from telebot.async_telebot import *
from telebot import types
from config import TOKEN
from server import *
from data import art_idea

token = TOKEN
bot = AsyncTeleBot(TOKEN)
API_URL = 'http://127.0.0.5:5050/'

username = None
user_id = None

@bot.message_handler(commands=['start'])
async def main_menu(message):
    global username, user_id
    username = message.from_user.first_name
    user_id = message.from_user.id
    chat_id = message.chat.id

    markup = types.InlineKeyboardMarkup()

    btn_random_idea = types.InlineKeyboardButton(text='🎲 Рандомный рисунок', callback_data='idea')
    btn_random_color = types.InlineKeyboardButton(text='🎨 Рандомный цвет', callback_data='color')
    btn_challenge = types.InlineKeyboardButton(text='🎯 Челлендж', callback_data='challenge')
    btn_channel = types.InlineKeyboardButton(text='📱 Наш канал', callback_data='channel', url='https://t.me/artistbot_FS')
    btn_profil = types.InlineKeyboardButton(text='👤 Профиль', callback_data='profil')

    markup.row(btn_random_idea)
    markup.row(btn_random_color)
    markup.row(btn_challenge, btn_channel)
    markup.row(btn_profil)

    await bot.send_message(chat_id, text=f'<b>👋 Привет {username}\n Добро пожаловать в artist!\n'
                                         f'⬇️ Вот мои возможности ⬇️</b>'
                                         f'<blockquote>'
                                         f'🎲 Генерировать идеи для рисунка\n'
                                         f'🎨 Предлогать цвета для рисунка\n'
                                         f'🎯 Генерировать интересные челленджы\n'
                                         f'</blockquote>', reply_markup=markup, parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: True)
async def button_check(call):
    chat_id = call.message.chat.id

    if call.data == 'idea':
        idea = random.choice(art_idea)
        await bot.send_message(chat_id, text=f'🎲 Ваша идея: <blockquote>{idea}</blockquote>', parse_mode='HTML')

    elif call.data == 'color':
        color = random.choice(colors)
        await bot.send_message(chat_id, text=f'🎨 Ваш цвет: <blockquote>{color}</blockquote>', parse_mode='HTML')

    elif call.data == 'challenge':
        colors_numbers = random.randint(1, 3)

        if colors_numbers == 1:
            idea = random.choice(art_idea)

            color = random.choice(colors)

            await bot.send_message(chat_id, text=f'🎲 Идея <blockquote>{idea}</blockquote>\n 🔢 Кол-во цветов <blockquote>1</blockquote>\n 🎨 Цвет <blockquote>{color}</blockquote>', parse_mode='HTML')

        elif colors_numbers == 2:
            idea2 = random.choice(art_idea)

            color1 = random.choice(colors)
            color2 = random.choice(colors)

            await bot.send_message(chat_id, f'🎲 Идея <blockquote>{idea2}</blockquote>\n 🔢 Кол-во цветов <blockquote>2</blockquote>\n 🎨 Цвета <blockquote>{color1}, {color2}</blockquote>', parse_mode='HTML')

        elif colors_numbers == 3:
            idea3 = random.choice(art_idea)

            color1 = random.choice(colors)
            color2 = random.choice(colors)
            color3 = random.choice(colors)

            await bot.send_message(chat_id, text=f'🎲 Идея <blockquote>{idea3}</blockquote>\n 🔢 Кол-во цветов <blockquote>3</blockquote>\n 🎨 Цвета <blockquote>{color1}, {color2}, {color3}</blockquote>', parse_mode='HTML')

    elif call.data == 'profil':
        global username, user_id
        await bot.send_message(chat_id, text=f'👤 <blockquote>{username}\n</blockquote>'
                                             f'🆔 <blockquote>{user_id}\n</blockquote>', parse_mode='HTML')






async def main():
    await bot.infinity_polling(timeout=0)

if __name__ == "__main__":
    asyncio.run(main())