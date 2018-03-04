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
DDOS="Извините,технические неполадки,попробуйте продолжить через одну минуту "
SORRY="Извините,технические неполадки,попробуйте получить текущий вопрос заново:/test"
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


def get_keyboard(q_id,question,old_choice=""):
		
		emblems=["А","Б","В","Г"]
		keyboard = types.InlineKeyboardMarkup()	
		row=[]
		for emblem in emblems:
			callback_button = types.InlineKeyboardButton(emblem, 
				callback_data="{0}:{1}:{2}:{3}".format(q_id,question[emblem][1], emblem, old_choice))
			row.append(callback_button)
		keyboard.row(*row)
		return keyboard

def send_question(user_id,old_choice=""):
		emblems=["А","Б","В","Г"]
		question_id=get_question_id(user_id)#get user's question_id
		body=get_question_body(question_id,old_choice)
		
		QUESTION_TEXT="_Вопрос {0}/{1}_:\n*{2}*\n".format(question_id,count_of_questions,body.pop("question"))
		for emblem in emblems:
			QUESTION_TEXT="{0}{1}) {2}\n".format(QUESTION_TEXT,emblem, body[emblem][0])
		keyboard=get_keyboard(question_id,body,old_choice)
		bot.send_message(user_id,text=QUESTION_TEXT,reply_markup=keyboard, parse_mode= 'Markdown')


def count_result(score):
	Answers=answers_json
	for idx in range(0,len(Answers)):
		Range=Answers[idx]["range"]
		if score>Range[0] and score<Range[1]:
			return idx
	return -1

def edit_prev_answ(c_id,m_id,q_id,prev_answ):
	emblems=["А","Б","В","Г"]
	body=get_question_body(int(q_id),prev_answ)
	QUESTION_TEXT="_Вопрос {0}/{1}_:\n*{2}*\n".format(q_id,count_of_questions,body.pop("question"))
	for emblem in emblems:
		QUESTION_TEXT="{0}{1}) {2}\n".format(QUESTION_TEXT,emblem, body[emblem][0])

	keyboard=get_keyboard(q_id,body,prev_answ)
	bot.edit_message_text(chat_id=c_id, message_id=m_id, text=QUESTION_TEXT,parse_mode= 'Markdown')
	bot.edit_message_reply_markup(chat_id=c_id, message_id = m_id, reply_markup=keyboard)

def send_result(user_id):
	result_id=get_result_id(user_id)
	result=answers()[result_id]

	keyboard = types.InlineKeyboardMarkup()	
	callback_button = types.InlineKeyboardButton(text=CAPTION_FOR_URL, url=result["url"])
	keyboard.add(callback_button)
	bot.send_message(user_id,text=result["result"], reply_markup=keyboard)

def get_cost_of_choice(q_id,position_num):
		emblems={"А":1,"Б":2,"В":3,"Г":4}
		position=emblems[position_num]-1
		question=question_json[int(q_id)-1]
		cost=question["answers"][position]["points"]
		return cost

def get_question_body(q_id,old_choice=""):
	emblems=["А","Б","В","Г"]
	answers=question_json[q_id-1]
	body={"question":answers["question"]}
	for e,answer in zip(emblems,answers["answers"]):
		body.update({e:[answer["answer"], answer["points"]]})
	if old_choice:
		body[old_choice][0]="*"+body[old_choice][0]+"*"
	return body


