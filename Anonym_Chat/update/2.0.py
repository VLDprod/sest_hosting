from pickletools import read_float8
from turtle import pen
import aiogram
from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
import logging
import configparser
import markups as nav
import var as v
import time
import os
import random
import re

admin = '925356318'
ref_file_name = "referals.txt"
dref_file_name = "dreferals.txt"



config = configparser.ConfigParser()
config.read("config.ini")
API_TOKEN = config.items("BOT")[0][1]
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

start_dir = os.getcwd()

# @dp.message_handler(content_types=['text'])
# async def echo(message: types.Message):
#   await bot.send_message(message.chat.id, message.text)


# def create_instruction():
    # referals = open(TEMP_folder + "\\!!!.txt","w+")
    # referals.write("ref = ")  ############################################     ЗАПОЛНИТЬ

@dp.message_handler(commands=['start'])
async def startcom(message: types.Message):
	id_usera = message["from"]["id"]
	check_dir = os.getcwd()
	users_dir = "\\users\\"
	directoriya = str(check_dir) + str(users_dir)
	try:
		os.chdir(directoriya)
		os.mkdir(str(id_usera))
		os.chdir(str(id_usera))
		#
		directoriya_ref_user = directoriya + str(id_usera)
		randomizer = int(id_usera) * int(id_usera)
		randomizer2 = int(id_usera) * int(id_usera) + int(id_usera)
		ref_rand = str(random.randrange(randomizer, randomizer2))
		referals = open(directoriya_ref_user + "\\referals.txt","w+")
		referals.write("Ref_code = " + ref_rand + "_" + str(id_usera) +  "\nValue_referals = 0\nBonus = 0")
		referals.close()
		referals = open(directoriya_ref_user + "\\dreferals.txt","w+")
		referals.close()
		await message.answer("Только что был зарегистрирован")
		os.chdir(start_dir)
	except:
		os.chdir(directoriya)
		check_dir2 = os.getcwd()
		await message.answer("Ты уже был зареган")
		os.chdir(start_dir)

#------------------------------------------------------------------------------
		# directoriya_ref_user = directoriya + str(id_usera) + "\\"
		# with open(directoriya_ref_user + '\\referals.txt') as f:
		# 	lines = f.readlines()
		# 	lines2 = lines[0]
		# 	lines3 = lines2.replace('Ref_code = ', '')
		# 	lines4 = lines3.split("_")
		# 	lines3 = lines4[1]
		# 	lines3 = lines3.replace('\n', '') # - ID_USERА
		# 	lines4 = lines4[0] # - ReferalKA
#------------------------------------------------------------------------------

@dp.message_handler(commands=['ref'])
async def referalka(message: types.Message):
	usr_name_or_name = "@" + message.from_user.username if message.from_user.username is not None else message.from_user.full_name
	message_ref = message.text.replace('/ref ', '')
	id_usera_ref = message["from"]["id"]
	id_usera_new = id_usera_ref
	users_dir = "\\users\\"
	check_dir = os.getcwd()
	try:
		lines = message_ref
		lines4 = lines.split("_")
		lines3 = lines4[1]
		iddd = lines3 # - ID usera
		id_usera = lines3
		directoriya = str(check_dir) + str(users_dir)
		directoriya_ref_user = directoriya + str(id_usera) + "\\"
		lines4 = lines4[0] # - ReferalKA
		os.chdir(directoriya_ref_user)
		f = open(directoriya_ref_user + '\\' + ref_file_name, 'r')
		send_ref = lines4
		lines = f.readlines()
		lines2 = lines[0]
		lines3 = lines2.replace('Ref_code = ', '')
		lines4 = lines3.split("_")
		lines4 = lines4[0] # - ReferalKA
		my_ref = lines4 # - рефералка_usera_Nachalo
		# print(my_ref)
	
		f.close()
		#directoriyad = directoriya + lines6 + '\\'

		if my_ref == send_ref:
			f = open(directoriya_ref_user + dref_file_name, 'r')
			lineses = f.readlines()
			f.close()
			if lineses != []:
				for reslines in lineses:
					reslines = reslines.split("\n")
					if int(id_usera_new) == int(reslines[0]):
						await bot.send_message(id_usera_new, 'Вы уже использовали этот реферал')
					else:
						pass
			else:
				f = open(directoriya_ref_user + '\\' + ref_file_name, 'r')
				lines = f.readlines()
				Value_referals = lines[1]
				Bonus = lines[2]
				Bonus1 = Bonus.split(" ")
				Bonus1 = int(Bonus[-1]) + 1
				Value_referals1 = Value_referals.split(" ")
				Value_referals1 = int(Value_referals1[-1]) + 1
					#Value_referals1    ИНТОВОЕ ЧИСЛО БОНУСА
					#lines2  ПОЛНЫЙ РЕФЕРАЛ С реф_коде
				f.close()
				f = open(directoriya_ref_user + '\\' + ref_file_name, 'w')
				f.write(lines2 + "Value_referals = " + str(Value_referals1) + '\nBonus = ' + str(Bonus1))    #id_usera_ref
				await bot.send_message(iddd, usr_name_or_name + ', активировал вашу рефералку. У вас на счету: ' + str(Value_referals1) + ' реферал(ов)' + '. \n' + str(Bonus1))
				f.close()
				f = open(directoriya_ref_user + '\\' + dref_file_name, 'a')
				f.write(str(id_usera_new) + '\n')
				f.close()
				os.chdir(directoriya + str(id_usera_new))
				f = open(ref_file_name, 'r')
				lines = f.readlines()
				Value_referals = lines[1]
				Value_referals4 = lines[0]
				Bonus = lines[2]
				Bonus1 = Bonus.split(" ")
				Bonus1 = int(Bonus[-1]) + 1
				# Bonus1 = int(Bonus) + 
				Value_referals1 = Value_referals.split(" ")
				Value_referals1 = int(Value_referals1[-1]) + 1
				f.close()
				f = open(ref_file_name, 'w')
				f.write(str(Value_referals4) + "Value_referals = " + str(Value_referals1) + '\nBonus = ' + str(Bonus1)) 
				await bot.send_message(id_usera_new, 'Вы получили бонус . У вас на счету: ' + str(Bonus1) + ' бонус(ов)')
				f.close()    #id_usera_ref







		else:
			await message.answer("Такой рефералки нет")
	except aiogram.utils.exceptions.BotBlocked as fbn:


		pass
	except FileNotFoundError as exc:
		await message.answer("Введена не правильная рефералка")
	os.chdir(start_dir)


# my_st = "Например, строка Python"
# print(my_st.split("_"))





# n = (
#     "@" + message.from_user.username
#     if message.from_user.username is not None
#     else message.from_user.full_name
# )
# await bot.send_message(message.chat.id, "Добро пожаловать " + t + ". Я бот-консультант Компьтерных мастерова Влада и Вани. \nИспользуйте кнопки для взаимодействия со мной.", reply_markup = nav.MainMenu)

  #for result in os.list('users')
  #os.



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
    await bot.delete_message(message.chat.id, message.message_id+1)
    await bot.send_message(message.chat.id, 'Тепер я розмовляю Українською 💙💛', reply_markup = nav.MainMenu1)
  elif message.text == '🇷🇺 Перейти на Російську':
  	v.lang = 'ukr'
  	await bot.send_message(message.chat.id, 'Обрабатываю....', reply_markup=types.ReplyKeyboardRemove())
  	time.sleep(1)
  	await bot.delete_message(message.chat.id, message.message_id+1)
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
	  pass






if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=False)