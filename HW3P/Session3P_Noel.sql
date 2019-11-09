
--Selects the schema ricegames
USE ricegames;
--Creates the table 'Payment'
CREATE TABLE Members (
	member_id int(2) NOT NULL AUTO_INCREMENT,
    name varchar(45),
    role varchar(45),
    PRIMARY KEY (member_id)
);
--Creates the table 'Payment'
CREATE TABLE Payment (
	payment_id int(3),
    member_id int(2) NOT NULL,
    payday DATE,
    recipient varchar(45),
    amount varchar(45),
    memo varchar(90),
    PRIMARY KEY (payment_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

--Inserts row into the Payment table
INSERT INTO PAYMENT 
VALUES (2,'2018-01-31','Emily',130,'Shu Final Render+ Expressions');
VALUES (4,'2018-01-31','Emily',130,'Shu Final Render+ Expressions');
VALUES (5,'2018-04-07','Jonas',72,'Backgrounds 1A');

--Inserts row into the Members table
INSERT INTO Members
VALUES(9,'Robert','Composer')

--Shows all the data in the Members table
SELECT*FROM Members;

--Updates the total column in the Members table with the sum of all the column 'amount' in the Payment table 

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=AUTO_INCREMENT);

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=1) WHERE member_id=1;

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=2) WHERE member_id=2;

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=3) WHERE member_id=3;

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=4) WHERE member_id=4;

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=5) WHERE member_id=5;

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=6) WHERE member_id=6;

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=7) WHERE member_id=7;

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=8) WHERE member_id=8;

UPDATE Members SET total =  (SELECT SUM(amount) FROM Payment 
WHERE member_id=9) WHERE member_id=9;


--Answer to Ma. 
SELECT  role, SUM(total) AS 'Total Paid'
FROM    Members
WHERE role='Artist'
GROUP   BY role


--Answer to Mb.
SELECT  role, SUM(total) AS 'Total Paid'
FROM    Members
WHERE role='Composer'
GROUP   BY role

--Answer to Mc.
SELECT  name, 
	CASE
		WHEN total <100 THEN 'Paid Lots'
        WHEN 100<total<120 THEN 'Paid Well'
        WHEN 120<total<150 THEN 'Needs More'
        WHEN total>=150 THEN 'Needs Way More'
        END AS 'Money Status'
FROM    Members

--Creates enemy table
 CREATE TABLE enemies
(
	id int(3) PRIMARY KEY NOT NULL,
	player_name varchar(15) UNIQUE,
	eng_name varchar(15) UNIQUE,
	hp int(3) NOT NULL,
	attack int(3) NOT NULL,
	weakness1 varchar(4) NOT NULL,
	weakness2 varchar(4) DEFAULT '',
	weakness3 varchar(4) DEFAULT '',
	weakness4 varchar(4) DEFAULT ''
	
);

--Inserts row into 'enemies' table
INSERT INTO enemies 
VALUES (1,'ari','ant',3,2,'a','ri',null, null);
 INSERT INTO enemies 
VALUES (3,'uzura','quail',6,1,'u','zu','ra',null);

--Answer to Q 
SELECT player_name, eng_name,
	CASE
		WHEN hp <=10 THEN 'ZAKO'
        WHEN hp >10 THEN 'BOSS'
       
        END AS 'type'
FROM    enemies;