from config import *
from handlers import *



if __name__ == '__main__':
		try:
			bot.polling(none_stop=True)
		except Exception as e:
			with open('c_crashlog.txt', 'w') as f:
				f.write(str(e))