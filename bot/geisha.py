from handlers import *

if __name__ == '__main__':

	while True:
		try:
			bot.polling(none_stop=False)
		except Exception as e:
			with open('c_crashlog.txt', 'w') as f:
				f.write(str(e))
		time.sleep(17)
