CREATE DATABASE hs_capgemini

USE hs_capgemini

CREATE TABLE emp (
empno INT(4) NOT NULL,
ename	VARCHAR(10),
job 	VARCHAR(9),
mgr	INT(4),
hiredate	DATE,
sal	INT(7.2),
comm	INT(7.2),
deptno	INT(2)
)

CREATE TABLE designation_master (
design_code INT(3) NOT NULL,
design_name	VARCHAR(50)
)

CREATE TABLE department_master (
dept_code INT(2) NOT NULL,
dept_name	VARCHAR(50)
)

CREATE TABLE student_master (
student_code INT(6) NOT NULL,
student_name	VARCHAR(50) NOT NULL,
dept_code	INT(2),
student_dob	DATE,
student_address	VARCHAR(240)
)

INSERT INTO student_master VALUES ('1','Aman',1,'2002-03-15','Delhi')
INSERT INTO student_master VALUES ('2','Babita',2,'2004-05-15','Delhi')
INSERT INTO student_master VALUES ('3','Chunni',1,'2006-07-05','Delhi')
INSERT INTO student_master VALUES ('4','Dhiman',20,'2006-07-05','Delhi')
INSERT INTO student_master VALUES ('5','Eshan',30,'2006-07-05','Delhi')

CREATE TABLE student_marks (
student_code INT(6),
student_year	INT NOT NULL,
subject1	INT(3),
subject2	INT(3),
subject3	INT(3)
)

CREATE TABLE staff_master (
staff_code	INT(8) NOT NULL,
staff_name	VARCHAR(50) NOT NULL,
design_code	INT,
dept_code	INT,
hiredate	DATE,
staff_dob	DATE,
staff_address	VARCHAR(240),
mgr_code	INT(8),
staff_sal	INT(10.2)
)

INSERT INTO staff_master VALUES ('1','Ramesh Kumar','1','1','2002-03-15','1980-05-15','Delhi',NULL,21000)
INSERT INTO staff_master VALUES ('2','Rohan_Kumar','1','2','2002-12-15','1982-05-15','Delhi',NULL,23000)
INSERT INTO staff_master VALUES ('3','Rakesh','2','2','2000-12-15','1967-05-15','Delhi',1,33000)


CREATE TABLE book_master (
book_code INT(10) NOT NULL,
book_name	VARCHAR(50) NOT NULL,
book_pub_year	INT,
book_pub_author	VARCHAR(50) NOT NULL
)

INSERT INTO book_master VALUES (1,'JPH Hindi Course A',2002,'Urmila')
INSERT INTO book_master VALUES (2,'Chemistry Practice & Theory',2003,'Gaorekar')


CREATE TABLE book_transactions (
book_code 	INT,
student_code	INT,
staff_code	INT,
book_issue_date	DATE NOT NULL,
book_expected_return_date	DATE NOT NULL,
book_actual_return_date	DATE
)