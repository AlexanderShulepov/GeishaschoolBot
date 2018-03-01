
DELIMITER //
CREATE FUNCTION add_user(username varchar(50),first_name varchar(50),last_name varchar(50)) RETURNS Bool
BEGIN

    IF NOT EXISTS(SELECT * FROM User where User.username=username)
    THEN 
		INSERT INTO User(username,first_name,last_name) VALUES (username,first_name,last_name);
		RETURN true;
    ELSE
		RETURN false;
	END IF;
END
DELIMITER // 
select add_user("'Guardian_of_cookies'","Алекс","Shulepov");

DELIMITER //
CREATE FUNCTION add_new_test(username varchar(50)) RETURNS Bool
BEGIN
	DECLARE user_id INT;
    set user_id=(SELECT id FROM User where User.username=username);
	IF EXISTS(SELECT id FROM Test WHERE Test.User_id=user_id and result_id is  NULL)
    THEN
		RETURN false;
    ELSE 
		INSERT INTO Test(user_id,question_id,score,start_date) 
		VALUES (user_id,1,0,CURRENT_TIMESTAMP);
		RETURN true;
	END IF;
END;
#select add_new_test('Reivenorr');		
DELIMITER //
CREATE FUNCTION get_question(username varchar(50)) RETURNS JSON
BEGIN
	DECLARE user_id INT;
    DECLARE question_id INT;
    set user_id=(SELECT id FROM User where User.username=username);
	set question_id=(SELECT Test.question_id FROM Test WHERE Test.User_id=user_id and result_id is  NULL);
    if question_id is  null then
		return null;
	else
		return (select info from Question where Question.id=question_id);
	end if;
END;

DELIMITER //
select add_new_test('Guardian_of_cookies');	
select get_question('Guardian_of_cookies');

SELECT  JSON_EXTRACT(info, "$.question") as info FROM Question
    
    
    
    
    
    
    
    