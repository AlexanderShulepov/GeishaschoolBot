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
from models import *
####################
##CONSTS
####################
HELLO_NEWBY="Welcome /test"
HELLO_AGAIN="Welcome back! /test"
FINISH_THIS="Honey, finish this test before"
NO_TEST="Рано вам!Пройдите хотя бы один"
####################
##METHODS
####################
def questions():
	with open('../JSON/questions.json') as json_data:
		j = json.load(json_data)
		return j


def answers():
	with open('../JSON/answers.json') as json_data:
		j = json.load(json_data)
		return j


def send_message(id,mgs):
	bot.send_message(id, mgs)



def send_question(user_id,username):
		question_id=get_question_id(user_id)
		question=questions()[question_id-1]#get user's question_id and there get question
		emblems=["А","Б","В","Г"]
		keyboard = types.InlineKeyboardMarkup()		
		answers=question["answers"]
		QUESTION="Вопрос {0}: {1}\n".format(question_id,question["question"])
		for idx in range(0,len(answers)):
			QUESTION="{0}{1}) {2}\n".format(QUESTION,emblems[idx],answers[idx]["answer"])
			##callback_data=points for answer
			callback_button = types.InlineKeyboardButton(text=emblems[idx],callback_data=str(answers[idx]["points"]))
			keyboard.add(callback_button)
		bot.send_message(user_id,text=QUESTION, reply_markup=keyboard)


def count_result(score):
	answers=answers()
	for idx in range(0,len(answers)):
		range=answers[idx]["range"]
		if score>range[0] and score<range[1]:
			return idx
	return -1


def send_result(user_id):
	result_id=get_result_id(user_id)
	result=answers()[result_id]

	keyboard = types.InlineKeyboardMarkup()	
	callback_button = types.InlineKeyboardButton(text="Наше предложение",url=result["url"])
	keyboard.add(callback_button)
	bot.send_message(user_id,text=result["result"], reply_markup=keyboard)
