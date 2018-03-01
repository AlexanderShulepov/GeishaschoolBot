from config import *
from models import *


@bot.message_handler(commands=['start','test','result'])
def handle_commands(message):
		question=get_question(message.chat.username)
		if message.text=="/start":
			result_of_add=add_user(message.chat.username, message.chat.first_name, message.chat.last_name)
			if result_of_add:
				add_new_test(message.chat.username)
				send_message(message.chat.id, HELLO_NEWBY)
			else:
				send_message(message.chat.id, HELLO_AGAIN)

		elif message.text=="/test":
			
			if question:
				send_message(message.chat.id, FINISH_THIS)
			else:
				send_message(message.chat.id, "Ммм,давай повторим")
				add_new_test(message.chat.username)
				
			question=get_question(message.chat.username)	
			send_question(message.chat.id,question)

		elif message.text=="/result":
			if not question:
				send_message(message.chat.id, "Тип результат")
			else:
				send_message(message.chat.id, FINISH_THIS)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        send_message(call.message.chat.id, call.data)

@bot.message_handler(content_types=["text"])
def text_messages(message):
    bot.send_message(message.chat.id, "I'm alive!")
