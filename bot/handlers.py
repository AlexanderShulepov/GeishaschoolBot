from config import *
from models import *


@bot.message_handler(commands=['start','test','result'])
def handle_commands(message):
		c_id=message.chat.id
		username=message.chat.username
		if message.text=="/start":
			result_of_add=add_user(c_id,username, message.chat.first_name, message.chat.last_name)
			if result_of_add:
				send_message(c_id, HELLO_NEWBY)
			else:
				send_message(c_id, HELLO_AGAIN)


		elif message.text=="/test":
			if get_question_id(c_id):
				send_message(c_id, FINISH_THIS)
			else:
				if is_newby(c_id):
					send_message(c_id,LETS_START)
				else:
					send_message(c_id,LETS_START_AGAIN )
			add_new_test(c_id)
			send_question(c_id,username)


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
	c_id=call.message.chat.id
	q_id=get_question_id(c_id)
	data=call.data.split(":")
	if data[0]==str(q_id):
		if q_id<=count_of_questions and q_id>0:
			if make_answer(c_id, data[1])<=count_of_questions:
				#bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
				send_question(c_id,call.message.chat.username)
			else:
				score=get_score(c_id)
				result_id=count_result(score)
				finish_test(c_id,result_id)
				send_result(c_id)
		edit_inline(c_id,call.message.message_id,data[2])

@bot.message_handler(content_types=["text"])
def text_messages(message):
    bot.send_message(message.chat.id, TEXT_REACTION)
