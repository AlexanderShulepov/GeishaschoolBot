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
LETS_START="Давай начнем"
NO_TEST="Рано вам!Пройдите хотя бы один"
LETS_START_AGAIN="Ммм,давай повторим"
TEXT_REACTION="I'm alive!"
CAPTION_FOR_URL="Наше предложение"
CHOICE_OF_USER='Вы выбрали: '

####################
##METHODS
####################
def questions():#get list of questions
	with open('../JSON/questions.json') as json_data:
		j = json.load(json_data)
		return j


def answers():#get list of answers
	with open('../JSON/results.json') as json_data:
		j = json.load(json_data)
		return j

question_json=questions()
answers_json=answers()
count_of_questions=len(question_json)

def send_message(id,mgs):
	bot.send_message(id, mgs)



def send_question(user_id,username):
		question_id=get_question_id(user_id)#get user's question_id
		question=question_json[question_id-1] #and there get question
		emblems=["А","Б","В","Г"]
		keyboard = types.InlineKeyboardMarkup()		
		answers=question["answers"]
		QUESTION="Вопрос {0}/{1}:\n {2}\n".format(question_id,count_of_questions,question["question"])
		btns=[]
		for idx in range(0,len(answers)):
			QUESTION="{0}{1}) {2}\n".format(QUESTION,emblems[idx], answers[idx]["answer"])	
			callback_button = types.InlineKeyboardButton(emblems[idx], callback_data="{0}:{1}:{2}".format(question_id,answers[idx]["points"],emblems[idx]))##callback_data=points for answer
			btns.append(callback_button)
		keyboard.add(*btns)
		bot.send_message(user_id,text=QUESTION, reply_markup=keyboard,parse_mode= 'Markdown')

def count_result(score):
	Answers=answers_json
	for idx in range(0,len(Answers)):
		Range=Answers[idx]["range"]
		if score>Range[0] and score<Range[1]:
			return idx
	return -1

def edit_inline(c_id,m_id,emblem):
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(types.InlineKeyboardButton(CHOICE_OF_USER+emblem, callback_data='none'))
	bot.edit_message_reply_markup(chat_id=c_id, message_id = m_id, reply_markup=keyboard)
def send_result(user_id):
	result_id=get_result_id(user_id)
	result=answers()[result_id]

	keyboard = types.InlineKeyboardMarkup()	
	callback_button = types.InlineKeyboardButton(text=CAPTION_FOR_URL, url=result["url"])
	keyboard.add(callback_button)
	bot.send_message(user_id,text=result["result"], reply_markup=keyboard)
