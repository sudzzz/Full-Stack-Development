---Question - 1
SELECT staff_name,CONCAT('$',staff_sal) staff_sal FROM staff_master

---Question - 2   (1 FOR Sun, .... , 7 FOR Sat)
SELECT student_name,DATE_FORMAT(student_dob,'%M, %d %Y') student_dob FROM student_master
WHERE DAYOFWEEK(student_dob) IN (1,7)

---Question - 3
SELECT staff_name,hiredate,ROUND((DATEDIFF(CURDATE(),hiredate)/30),0) 'Months Worked' FROM staff_master

---Question - 4
SELECT * FROM staff_master
WHERE MONTH(hiredate)=12 AND DAY(hiredate)<=15

---Question - 5
 SELECT staff_name,staff_sal,
 IF(staff_sal>=50000,'A',IF(staff_sal<50000 AND staff_sal>=25000,'B',
 IF(staff_sal<25000 AND staff_sal>=10000,'C','D'))) AS grade FROM staff_master
 
---Question - 6
SELECT staff_name,hiredate,DATE_FORMAT(hiredate,'%a') DAY FROM staff_master

---Question - 7
SELECT LOCATE("i","Mississippi",LOCATE("i","Mississippi",LOCATE("i","Mississippi",1)+1)+1) 3rd_pos

---Question - 8
SELECT DATE_FORMAT(STR_TO_DATE(LAST_DAY('2023-01-01') - ((7 + WEEKDAY(LAST_DAY('2023-01-01')) - 4) % 7),"%Y%m%d"),'%D of %M, %Y') 'Pay Date'

---Question - 8
SELECT student_code,student_name, 
 IF(dept_code=20,'Electricals',IF(dept_code=30,'Electronics','Others')) AS dept_name FROM student_master
 