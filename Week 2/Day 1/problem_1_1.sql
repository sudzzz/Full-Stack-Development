---Question - 1
SELECT staff_name,design_code FROM staff_master
WHERE DATE_FORMAT(hiredate,'%y-%m-%d')<=DATE('2003-01-01')
AND (staff_sal>=12000 AND staff_sal<=25000)

---Question - 2
SELECT staff_code,staff_name,dept_code FROM staff_master
WHERE (DATEDIFF(CURDATE(),hiredate)/365)>=18
ORDER BY hiredate 

---Question - 3
SELECT * FROM staff_master WHERE mgr_code IS NULL

---Question - 4
SELECT * FROM book_master WHERE book_pub_year>=2001 AND book_pub_year<=2004

SELECT * FROM book_master WHERE book_name LIKE '%&%'

---Question - 5
SELECT * FROM staff_master WHERE staff_name LIKE '%_%'
