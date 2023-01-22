---Question - 1
SELECT a.staff_name,a.dept_code,b.dept_name,a.staff_sal FROM staff_master a
JOIN department_master b ON a.dept_code=b.dept_code
WHERE a.staff_sal>20000


---Question - 2
SELECT a.staff_code 'staff#',a.staff_name staff,a.mgr_code 'mgr#',b.staff_name manager FROM staff_master a
JOIN staff_master b ON a.mgr_code=b.staff_code


---Question - 3
SELECT b.student_code,b.student_name,a.book_code,c.book_name FROM book_transactions a 
JOIN student_master b ON a.student_code=b.student_code
JOIN book_master c ON c.book_code=a.book_code
WHERE book_expected_return_date='2023-01-08'

---Question - 4
SELECT b.staff_code,b.staff_name,d.dept_name,e.design_name,a.book_code,c.book_name,a.book_issue_date FROM book_transactions a 
JOIN staff_master b ON a.staff_code=b.staff_code
JOIN book_master c ON c.book_code=a.book_code
JOIN department_master d ON d.dept_code=b.dept_code
JOIN designation_master e ON e.design_code=b.design_code
WHERE DATEDIFF(CURDATE(),a.book_issue_date)>=30


---Question - 5
SELECT b.staff_code,b.staff_name,d.dept_name,e.design_name,
a.book_code,c.book_name,c.book_pub_author,(DATEDIFF(CURDATE(),a.book_expected_return_date) * 5) fine FROM book_transactions a 
JOIN staff_master b ON a.staff_code=b.staff_code
JOIN book_master c ON c.book_code=a.book_code
JOIN department_master d ON d.dept_code=b.dept_code
JOIN designation_master e ON e.design_code=b.design_code
WHERE a.book_expected_return_date<CURDATE()

---Question - 6
SELECT a.staff_code,a.staff_name,a.staff_sal FROM staff_master a
JOIN (SELECT AVG(staff_sal) avg_sal FROM staff_master) b 
WHERE a.staff_sal<=b.avg_sal

---Question - 7
SELECT a.staff_code,a.staff_name,a.staff_sal FROM book_master a
JOIN (SELECT AVG(staff_sal) avg_sal FROM staff_master) b 
WHERE a.staff_sal<=b.avg_sal


---Question - 8
SELECT b.staff_code,MAX(b.staff_name) staff_name,MAX(d.dept_name) dept_name,COUNT(a.book_code) totbook FROM book_transactions a 
JOIN staff_master b ON a.staff_code=b.staff_code
JOIN department_master d ON d.dept_code=b.dept_code
GROUP BY b.staff_code
HAVING COUNT(a.book_code)>1

---Question - 9
SELECT a.student_code,a.student_name, b.dept_name FROM student_master a 
JOIN department_master b ON b.dept_code=a.dept_code
WHERE a.dept_code IN (SELECT dept_code FROM student_master GROUP BY dept_code LIMIT 1)

---Question - 10
SELECT a.staff_code,a.staff_name,b.dept_name,c.design_name FROM staff_master a 
LEFT JOIN department_master b ON b.dept_code=a.dept_code
LEFT JOIN designation_master c ON a.design_code=c.design_code
WHERE DATEDIFF(CURDATE(),hiredate)<=90

---Question - 11
SELECT a.mgr_code,MAX(b.staff_name) manager,COUNT(a.staff_code) 'total strength' FROM staff_master a 
LEFT JOIN staff_master b ON b.staff_code=a.mgr_code
WHERE a.mgr_code IS NOT NULL
GROUP BY a.mgr_code

---Question - 12
SELECT a.book_code,b.book_name FROM book_transactions a 
LEFT JOIN book_master b ON b.book_code=a.book_code
WHERE a.book_expected_return_date<='2023-01-08' AND a.book_actual_return_date IS NULL;

---Question - 13
SELECT a.dept_code,MAX(b.dept_name) department,COUNT(a.staff_code) 'Number of People' FROM staff_master a 
LEFT JOIN department_master b ON b.dept_code=a.dept_code
GROUP BY a.dept_code

