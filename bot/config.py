####################
##TELEGRAM API
####################
import telebot
from telebot import types
TOKEN = '485895216:AAGvTEx3m9Nzl4jeUwCh8qq5bOnujGB8jD4'
bot = telebot.TeleBot(TOKEN)
####################
##MODULES
####################
import json
####################
##CONSTS
####################
HELLO_NEWBY="Welcome /test"
HELLO_AGAIN="Welcome back! /test"
FINISH_THIS="Honey, finish this test before"
####################
##METHODS
####################
def send_message(id,mgs):
	bot.send_message(id, mgs)

def send_question(id,question):
		mass=["А","Б","В","Г",]
		keyboard = types.InlineKeyboardMarkup()
		question=json.loads(question)
			
		answers=question["answers"]
		TEXT=question["question"]+"\n"
		for idx in range(0,len(answers)):
			TEXT=TEXT+mass[idx]+") "+answers[idx]["answer"]+"\n"
			callback_button = types.InlineKeyboardButton(text=mass[idx],callback_data=str(idx))
			keyboard.add(callback_button)
		print(keyboard)
		bot.send_message(id,text=TEXT, reply_markup=keyboard)
  	#question["answers"][idx]["answer"]