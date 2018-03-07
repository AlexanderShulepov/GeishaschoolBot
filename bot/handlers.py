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
					send_start_keyboard(c_id)
					add_new_test(c_id)
			send_question(c_id)

		elif message.text=="/result":
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
		data=call.data.split(':')

		if data[0]=='0':#promo inline
			#edit_prev_answ(c_id,call.message.message_id)
			send_promo(c_id,data[1])
			
	except Exception as e:
		pass

@bot.message_handler(content_types=["text"])
def text_messages(message):
	time.sleep(1)
	answs=["А","Б","В","Г"]
	c_id=message.chat.id
	q_id=get_question_id(c_id)
	print(q_id)
	if not is_finished_test(c_id):
		if get_question_id(c_id)<=count_of_questions:#answer
				answer=message.text.strip().upper()
				if message.text.strip().upper() in answs:
					answer_cost=get_cost_of_choice(q_id,answer)
					if make_answer(c_id, answer_cost)<=count_of_questions:#checking for answer on last question
						send_question(c_id)#not last
					else:
						score=get_score(c_id)
						result_id=count_result(score)
						finish_test(c_id,result_id)
						send_result(c_id)
				else:
					send_message(c_id,HELLO)
		else:#just trash
			pass
	else:
		send_message(c_id,WITH_FINISHED_TEST)
