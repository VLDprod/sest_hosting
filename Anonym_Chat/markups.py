from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove




btn_boy = KeyboardButton('Парень👨🏼')
btn_girl = KeyboardButton('Девушка👩🏼‍🦱')

btn_start = KeyboardButton('Начать поиск собеседника🔍')
btn_next = KeyboardButton('Следующий собеседник👉')
btn_stop = KeyboardButton('Остановить поиск🔍❌')


StateMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_boy, btn_girl)

MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_start, btn_next, btn_stop)


#---------------lang----------------------





