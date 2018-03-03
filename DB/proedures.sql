
DELIMITER //
CREATE FUNCTION add_user(user_id int(100),username varchar(50),first_name varchar(50),last_name varchar(50)) RETURNS Bool
BEGIN

    IF NOT EXISTS(SELECT * FROM User where User.id=user_id)
    THEN 
		INSERT INTO User(id,username,first_name,last_name) VALUES (user_id,username,first_name,last_name);
		RETURN true;
    ELSE
		RETURN false;
	END IF;
END;
DELIMITER // 

DELIMITER //
CREATE FUNCTION add_new_test(user_id INT) RETURNS Bool
BEGIN
	IF EXISTS(SELECT id FROM Test WHERE Test.User_id=user_id and result_id is  NULL)
    THEN
		RETURN false;
    ELSE 
		INSERT INTO Test(user_id,question_id,score,start_date) 
		VALUES (user_id,1,0,CURRENT_TIMESTAMP);
		RETURN true;
	END IF;
END;
	
DELIMITER //
CREATE FUNCTION get_question_id(user_id INT) RETURNS INT
BEGIN
    DECLARE question_id INT;
	set question_id=(SELECT Test.question_id FROM Test WHERE Test.User_id=user_id and result_id is  NULL);
    if question_id is  null then
		return 0;
	else
		return question_id;
	end if;
END;
DELIMITER //
select add_user(205449285,"Guardian_of_cookies","Алекс","Shulepov");
select add_new_test(205449285);	
select get_question_id(205449285);
select is_finish_test(205449285)
select make_answer(205449285,5)
select get_score(205449285);
DELIMITER //
CREATE FUNCTION is_finish_test(user_id int) RETURNS bool
BEGIN
	IF not EXISTS(SELECT id FROM Test WHERE Test.User_id=user_id and result_id is  NULL) then
    return true;
    else
    return false;
    end if;
END;

DELIMITER //
CREATE FUNCTION is_newby(user_id int) RETURNS bool
BEGIN
	IF (SELECT  Count(*) FROM Test WHERE Test.User_id=user_id)=0 then
    return true;
    else
    return false;
    end if;
END;

DELIMITER //
CREATE FUNCTION make_answer(user_id int,points int) RETURNS INT
BEGIN
	UPDATE Test SET score=score+points, question_id=question_id+1 where Test.user_id=user_id and Test.result_id is null;
    return (select question_id from Test where Test.user_id=user_id and Test.result_id is null);
END;


DELIMITER //
CREATE FUNCTION get_score (user_id int) RETURNS INT
BEGIN
	return (select score from Test where Test.user_id=user_id and Test.result_id is null);
END;


DELIMITER //
CREATE FUNCTION finish_test (user_id int,result_id int) RETURNS bool
BEGIN
	UPDATE Test SET Test.result_id=result_id where Test.user_id=user_id and Test.result_id is null;
    return True;
END;



DELIMITER //
CREATE FUNCTION get_result_id (user_id int) RETURNS int
BEGIN
	IF EXISTS(SELECT id FROM Test WHERE Test.User_id=user_id and result_id is  NULL) then
    return 0;
    else 
    return (select result_id from Test where Test.user_id=user_id and Test.result_id is not null order by Test.start_date DESC LIMIT 1);
    end if;
END;


DELIMITER //
CREATE FUNCTION make_reanswer(user_id int,old_points int,new_points int) RETURNS bool
BEGIN
	UPDATE Test SET score=score-old_points+new_points where Test.user_id=user_id and Test.result_id is null;
    return true;
END;



SELECT id FROM Test WHERE Test.User_id=205449285 and result_id is  NULL
select result_id from Test where Test.user_id=205449285 and Test.result_id is not null order by Test.start_date DESC LIMIT 1

DELIMITER //
select add_user(205449320,"Mali","Виктория","Бушевич");
select add_new_test(205449318);	
select get_question_id(205449285);
select is_finish_test(205449285);
select make_answer(205449285,5);
select get_score(205449285);
select finish_test(205449317,0);
select get_result_id(205449285);