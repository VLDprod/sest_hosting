from pickletools import read_float8
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
from datetime import date


admin = ['925356318']
ref_file_name = "referals.txt"
dref_file_name = "dreferals.txt"

gender = ''
onl_txt = 'online.txt'
is_in_online = 0
checr = 0
hjh = 0
yty = 0



iam_onl = 0
friend = 0


config = configparser.ConfigParser()
config.read("config.ini")
API_TOKEN = config.items("BOT")[0][1]
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


#===========================================NOT LOCAL VARIBLES===================================================
start_dir = os.getcwd()

comment_bons = 'бонусы не были зачислены.'
regas = 0
reg = 0

help_admin = """
/accept id;comments    -    /accept 925356318;Ок, я вас понял, в ближайшее время напишу.
/deny id;comments;yes/no-amount     -    /deny 925356318;Ок, я вас понял, в ближайшее время напишу.;yes-8 
/orders id     -    /orders 925356318  -   Возвращает все заказы пользователя
/active   -   Возвращает активные заказы которые принял админ, удалить можно в тхт файле
/bonuses   -    /bonuses 925356318;+/-/=;кол-во
"""
# @dp.message_handler(content_types=['text'])
# async def echo(message: types.Message):
#   await bot.send_message(message.chat.id, message.text)


# def create_instruction():
    # referals = open(TEMP_folder + "\\!!!.txt","w+")
    # referals.write("ref = ")  ############################################     ЗАПОЛНИТЬ

def auth(func):
	async def wrapper(message):
		if message["from"]["id"] == 925356318:
			return await func(message)
	return wrapper


buy_val = 0

@dp.message_handler(commands=['start'])
async def startcom(message: types.Message):
	global regas
	global reg
	id_usera = message["from"]["id"]
	check_dir = os.getcwd()
	users_dir = "\\users\\"
	
	directoriya = str(check_dir) + str(users_dir)
	usr_name_or_name = "@" + message.from_user.username if message.from_user.username is not None else message.from_user.full_name
	await message.answer("Добро пожаловать " + usr_name_or_name + ". Я бот-консультант Компьтерных мастерова Влада и Вани. \nИспользуйте кнопки для взаимодействия со мной.", reply_markup = nav.MainMenu)

	try:
		os.chdir(directoriya)
		os.chdir(str(id_usera))	
		os.chdir(start_dir)
		await message.answer("Вы уже зарегестрированы", reply_markup = nav.MainMenu)
		
	
	except:
		await bot.send_message(message.chat.id, 'Выберите ваш пол. Снизу есть две кнопки, нажмите на ту на которой указан ваш пол.', reply_markup = nav.StateMenu)
		reg = 1
	#await message.answer("Вы успешно зарегестрировались в системе. Вы можете получить бонус (скидку), для этого снизу на кнопках нажмите \"Получить реферал\" после чего он будет скопирован в ваш буфер обмена, отправте скопированый текст другу или знакомому и скажите что бы ввёл этот текст после старта бота")
	


	


@dp.message_handler(commands=['helpadmin'])
@auth
async def deny_buy(message: types.Message):
	#await bot.send_message(admin, help_admin)
	os.chdir(start_dir)
	id_usera = message["from"]["id"]
	check_dir = os.getcwd()
	users_dir = "\\users\\"
	os.chdir(check_dir + users_dir)
	check333 = os.getcwd()
	lol = os.listdir(path=check333)
	print(str(lol[0]))


@dp.message_handler()
async def bot_msg(message: types.Message):
	global hjh, yty, iam_onl, friend, admin, checr, is_in_online, onl_txt, regas, reg, gender
	id_usera = message["from"]["id"]
	os.chdir(start_dir)
	check_dir = os.getcwd()
	users_dir = "\\users\\"
	directoriya1 = str(check_dir) + str(users_dir)
	msg = message.text
	if reg == 1:
		if msg == 'Парень👨🏼':
			gender = 'boy'
			reg = 0
		elif msg == 'Девушка👩🏼‍🦱':
			gender = 'girl'
			reg = 0
		else:
			await bot.send_message(message.chat.id, 'Вы указали неверный пол, напишите /start и выберите правильный вариант')
		if gender == 'boy' or gender == 'girl':
			try:
				os.chdir(directoriya1)
				os.mkdir(str(id_usera))
				os.chdir(str(id_usera))
				directoriya_ref_user = directoriya1 + str(id_usera)
				referals = open(directoriya_ref_user + "\\about_user.txt","w+")
				referals.write("Gender = " + gender)
				referals.close()
				frn = open(directoriya_ref_user + "\\friend.txt","w+")
				frn.write()
				frn.close()
				os.chdir(start_dir)
				await message.answer("Вы успешно зарегестрировались в системе. Вы можете получить бонус (скидку), для этого снизу на кнопках нажмите \"Получить реферал\" после чего он будет скопирован в ваш буфер обмена, отправте скопированый текст другу или знакомому и скажите что бы ввёл этот текст после старта бота", reply_markup = nav.MainMenu)
				regas = 1

			except:
				pass
				# if regas == 0:
				# 	os.chdir(check_dir)
				# 	check_dir2 = os.getcwd()
				# 	await message.answer("Ты уже был зарестрирован")
				# 	os.chdir(start_dir)

			
	if msg == 'Начать поиск собеседника🔍':	
		id_usera = message["from"]["id"]
		check_dir = os.getcwd()
		users_dir = "\\users\\"
		online_dir = "\\online\\"
		dir_us = check_dir + users_dir
		dir_onl = check_dir + online_dir
		dir_us1 = dir_us + str(id_usera)
		lol = os.listdir(path=dir_us)
		
		for check in lol:
			if int(check) == int(id_usera):
				checr = 1
				os.chdir(dir_onl)
				f = open(dir_onl + "\\" + onl_txt, 'r')
				lines = f.readlines()
				f.close()
				#print(lines)
				amount = 0
				for ch in lines:
					amount += 1
					ch = ch.replace("\n", "")
					ch = int(ch)
					if ch == int(id_usera):
						is_in_online = 1
						#print("is_is_onl")
				#print(str(is_in_online) + "    " + str(id_usera))
				if is_in_online == 1:
					n = 0
					q = open(dir_onl + "\\" + onl_txt, 'r')
					w = q.readlines()
					q.close()
					for tst in w:
						n += 1
						#print(n)
					if n < 1:
						await bot.send_message(message.chat.id, "Извините, но в чате нету людей, мы не можем соиденить вас. Подождите пока появится онлайн. Как появится собеседник мы соиденим вас с ним")
						c = open(dir_onl + "\\" + onl_txt, 'r')
						e = c.readlines()
						c.close()
						for p in e:
							if int(p) == int(id_usera):
								yty = 1
								
						if yty == 0:
							onln = open(dir_onl + "\\" + onl_txt, "a")
							onln.write(str(id_usera) + "\n")
							onln.close()
					else:
						await bot.send_message(message.chat.id, "Вы уже начали поиск собеседника, дождитесь пока собеседник подключиться")
				elif is_in_online == 0:
					await bot.send_message(message.chat.id, "Поиск собеседника начался... Для остановки нажмите кнопку 'Остановить поиск🔍❌'")
					onln = open(dir_onl + "\\" + onl_txt, "a")
					onln.write(str(id_usera) + "\n")
					onln.close()
					t = 0
					for tst in lines:
						t += 1
					if t < 1:
						await bot.send_message(message.chat.id, "Извините555, но в чате нету людей, мы не можем соиденить вас. Подождите пока появится онлайн Подождите пока появится онлайн. Как появится собеседник мы соиденим вас с ним")
					else:
						result_rand = random.randint(0, t - 1)
						arr_e = []
						l = open(dir_onl + "\\" + onl_txt, 'r')
						k = l.readlines()
						l.close()
						x = 0

						id_usr = str(message.chat.id) + '\n'
						for lik in k:	
							if lik == id_usr:
								k.remove(id_usr)
						for lok in k:
							if int(lok) == int(lines[result_rand]):
								ghg = lines[result_rand]#.replace("\n", '')
								k.remove(ghg)
							
							
						#print(k)
						h = open(dir_onl + "\\" + onl_txt, 'w')
						h.write('')
						h.close
						for hj in k:
							h = open(dir_onl + "\\" + onl_txt, 'a')
							h.write(hj)
							h.close

					#print(lines[result_rand])
						for i in admin:
							if int(id_usera) == int(i):   #ЕСЛИ ПИШЕТ АДМИН
								lns = lines[result_rand].replace("\n", "")
								os.chdir(dir_us + "\\" + lns)
								g = open(dir_us + "\\" + lns + "\\about_user.txt", "r")
								gr = g.read()
								g.close()
								gen_s = gr.replace("Gender = ", "")
								if gen_s == "boy":
									state_g = "парня👨🏼"
								elif gen_s == "girl":
									state_g = "девушку👩🏼‍🦱"
								await bot.send_message(message.chat.id, "Мы нашли вам " + state_g + ", приятного общения!")
							else:
								await bot.send_message(message.chat.id, "Мы нашли вам собеседника, приятного общения!")	
						for i in admin:
							if int(lines[result_rand]) == int(i):   #ЕСЛИ ПИШЕТ АДМИН
								lns = lines[result_rand].replace("\n", "")
								os.chdir(dir_us + "\\" + lns)
								g = open(dir_us + "\\" + lns + "\\about_user.txt", "r")
								gr = g.read()
								g.close()
								gen_s = gr.replace("Gender = ", "")
								if gen_s == "boy":
									state_g = "парня👨🏼"
								elif gen_s == "girl":
									state_g = "девушку👩🏼‍🦱"
								await bot.send_message(int(lines[result_rand]), "Мы нашли вам " + state_g + ", приятного общения!")
							else:	
								await bot.send_message(int(lines[result_rand]), "Мы нашли вам собеседника, приятного общения!")

		if int(check) != int(id_usera) and checr == 0:
			await bot.send_message(message.chat.id, "Вы ещё не зарегестрированы для поиска собеседника. Напишите /start и следуйте инструкциям")

				

	elif msg == 'Остановить поиск🔍❌':
		await bot.send_message(message.chat.id, "Поиск собеседника начался... Для остановки нажмите кнопку 'Остановить поиск🔍❌'")
		id_usera = message["from"]["id"]
		check_dir = os.getcwd()
		users_dir = "\\users\\"
		online_dir = "\\online\\"
		dir_us = check_dir + users_dir
		dir_onl = check_dir + online_dir
		os.chdir(dir_onl)
		f = open(dir_onl + "\\" + onl_txt, 'r')
		lines = f.readlines()
		f.close()
		i = 0
		for ch in lines:
			i += 1
			if ch == id_usera:
				pass
	
	else:
	  pass






if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=False)