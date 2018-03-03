import pymysql


def MyQuery(query):	#mysql
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='GeishaSchool',charset='utf8mb4',use_unicode=True)
	db = conn.cursor()
	db.execute(query)
	query_result=[x for x in db]
	conn.commit()
	conn.close()
	return query_result
    
def add_user(user_id,username,first_name,last_name):
    return MyQuery('select add_user({0},"{1}","{2}","{3}")'.format(user_id,username,first_name,last_name))[0][0]

def add_new_test(user_id):
    return MyQuery('select add_new_test({0})'.format(user_id))[0][0]

def get_question_id(user_id):
    return MyQuery('select get_question_id({0})'.format(user_id))[0][0]

def is_finished_test(user_id):
	return MyQuery('select is_finish_test({0})'.format(user_id))[0][0]

def is_newby(user_id):
	return MyQuery('select is_newby({0})'.format(user_id))[0][0]

def make_answer(user_id,points):
	return MyQuery('select make_answer({0},{1})'.format(user_id,points))[0][0]

def make_reanswer(user_id,old_points,new_points):
	return MyQuery('select make_reanswer({0},{1},{2})'.format(user_id,old_points,new_points))[0][0]

def make_answer(user_id,points):
	return MyQuery('select make_answer({0},{1})'.format(user_id,points))[0][0]
def get_score(user_id):
	return MyQuery('select get_score({0})'.format(user_id))[0][0]

def finish_test(user_id,result_id):
	return MyQuery('select finish_test({0},{1})'.format(user_id,result_id))[0][0]

def get_result_id(user_id):
	return MyQuery('select get_result_id({0})'.format(user_id))[0][0]
