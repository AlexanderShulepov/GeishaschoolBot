import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='GeishaSchool',charset='utf8mb4',use_unicode=True)
db = conn.cursor()

def MyQuery(query):	#mysql
	db.execute(query)
	query_result=[x for x in db]
	conn.commit()
	return query_result
    
def add_user(username,first_name,last_name):
    return MyQuery('select add_user("{0}","{1}","{2}")'.format(username,first_name,last_name))[0][0]

def add_new_test(username):
    return MyQuery('select add_new_test("{0}")'.format(username))[0][0]

def get_question(username):
    #get q_json or null for call get_result
    return MyQuery('select get_question("{0}")'.format(username))[0][0]
#def get_result(username):
    #get json or false

#def make_keyboard(answers_json):
    