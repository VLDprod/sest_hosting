import aiogram
from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import var as v
import time



admin = '925356318'
API_TOKEN = "5395001959:AAGdeDJgz9Qk2HhwwqaRk6MMjdrvhnkEUWk"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)






# @dp.message_handler(content_types=['text'])
# async def echo(message: types.Message):
#   await bot.send_message(message.chat.id, message.text)

@dp.message_handler(commands=['start'])
async def startcom(message: types.Message):
  t = "@" + message.from_user.username if message.from_user.username is not None else message.from_user.full_name
  await bot.send_message(message.chat.id, "Добро пожаловать " + t + ". Я бот-консультант Компьтерных мастерова Влада и Вани. \nИспользуйте кнопки для взаимодействия со мной.", reply_markup = nav.MainMenu)

@dp.message_handler(commands=['buy'])
async def buy_srvc(message: types.Message):
	msgs = message.text.replace('/buy ', '')
	await bot.send_message(message.chat.id, 'Ваш запрос отправлен, ожидайте ответа')
	t = "@" + message.from_user.username if message.from_user.username is not None else message.from_user.full_name
	await bot.send_message(admin, 'Пользователь ' + t + ' написал: ' + msgs + '   Ответь на сообщение /accept или /deny')
	await bot.send_message(admin, '/accept ' + str(message.chat.id))
	await bot.send_message(admin, '/deny ' + str(message.chat.id))






@dp.message_handler(commands=['accept'])
async def accept_buy(message: types.Message):
	msgi = message.text
	msgi = msgi.replace('/accept ', '')
	#t = "@" + message.from_user.username if message.from_user.username is not None else message.from_user.full_name
	await bot.send_message(admin, 'Напишите пользователю или по айди: ' + str(msgi))
	await bot.send_message(msgi, 'Ваш запрос был принят. ожидайте.... С вами свяжутся.')



@dp.message_handler(commands=['deny'])
async def deny_buy(message: types.Message):
	msgi = message.text
	msgi = msgi.replace('/deny ', '')
	await bot.send_message(msgi, 'Ваш запрос был Отклонён. Попробуйте снова')


@dp.message_handler()
async def bot_msg(message: types.Message):
  if message.text == '🇺🇦 Перейти на Украинский':
    v.lang = 'ukr'
    await bot.send_message(message.chat.id, 'Обробляю....', reply_markup=types.ReplyKeyboardRemove())
    time.sleep(1)
    await bot.send_message(message.chat.id, 'Тепер я розмовляю Українською 💙💛', reply_markup = nav.MainMenu1)
  elif message.text == '🇷🇺 Перейти на Російську':
  	v.lang = 'ukr'
  	await bot.send_message(message.chat.id, 'Обрабатываю....', reply_markup=types.ReplyKeyboardRemove())
  	time.sleep(1)
  	await bot.send_message(message.chat.id, 'Теперь я разговариваю на русском 💙💛', reply_markup = nav.MainMenu)

  elif message.text == '🔸 О нас':
  	await bot.send_message(message.chat.id, v.about_us)
  elif message.text == '🔸 Про нас':
  	await bot.send_message(message.chat.id, v.about_us_u)

  elif message.text == '❔ Вопросы/Ответы':
  	await bot.send_message(message.chat.id, '❔ Вопросы/Ответы', reply_markup = nav.OtherMenu)

  elif message.text == '❔ Питання/Відповіді':
  	await bot.send_message(message.chat.id, '❔ Питання/Відповіді', reply_markup = nav.OtherMenu1)

  elif message.text == 'Главное меню':
  	await bot.send_message(message.chat.id, 'Главное меню', reply_markup = nav.MainMenu)
  elif message.text == 'Головне меню':
  	await bot.send_message(message.chat.id, 'Головне меню', reply_markup = nav.MainMenu1)

  #-0-----------0-0-0--0---Заказать услугу-----0---0-0-0--0-0-0-0-
  elif message.text == '🛒 Заказать услугу/услуги':
  	await bot.send_message(message.chat.id, 'Напишите /buy и какую работу нужно выполнить, в конце укажите адрес и номер телефона. Желательно что бы у вас был ЮЗЕРНЭЙМ например: @VLD_prod. В течении не определённого времени вам прийдёт ответ (сюда) ', reply_markup=types.ReplyKeyboardRemove())

  else:
  	await bot.send_message(message.chat.id, 'no found')





if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)