from config import *
from models import *
import time

@bot.message_handler(commands=['start','result'])
def handle_commands(message):
		c_id=message.chat.id
		username=message.chat.username
		if message.text=="/start":
			result_of_add=add_user(c_id,username, message.chat.first_name, message.chat.last_name)
			if get_question_id(c_id)==0:
					add_new_test(c_id)
			send_question(c_id)

		elif message.text=="/result"
			if is_finished_test(c_id):
				if is_newby(c_id):
					send_message(c_id, NO_TESTS)
				else:
					send_result(c_id)
			else:
				question_id=get_question_id(c_id)
				if question_id>count_of_questions+1:
					score=get_score(c_id)
					result_id=count_result(score)
					finish_test(c_id,result_id)
					send_result(c_id)
				else:
					send_message(c_id,FINISH_THIS)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		c_id=call.message.chat.id
		q_id=get_question_id(c_id)
		data=call.data.split(":")# data=question_id:points:emblem:prev answer emblem 
		print(data)
		if data[0]=='0':
			send_promo(c_id,get_result_id(c_id))
		elif data[0]==str(q_id):#editing answer or giving new
				if make_answer(c_id, data[1])<=count_of_questions:#checking for answer is last question
					send_question(c_id)#not last
				else:#last
					score=get_score(c_id)
					result_id=count_result(score)
					finish_test(c_id,result_id)
					send_result(c_id)
				edit_prev_answ(c_id,call.message.message_id,q_id,data[2])#
		elif q_id-int(data[0])==1 and data[3]=='':
				send_message(c_id,SORRY)#error handler
		else:#reanswer
				make_reanswer(c_id,get_cost_of_choice(data[0],data[3]),data[1])
				edit_prev_answ(c_id,call.message.message_id,data[0],data[2])
	except Exception as e:
		print(e)
		send_message(c_id, DDOS)


@bot.message_handler(content_types=["text"])
def text_messages(message):
	pass
    #bot.send_message(message.chat.id, TEXT_REACTION)
