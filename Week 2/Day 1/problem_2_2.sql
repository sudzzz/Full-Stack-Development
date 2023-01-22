---Question - 1
SELECT dept_code,ROUND(MAX(staff_sal),0) maximum,
ROUND(MIN(staff_sal),0) Minimum,ROUND(SUM(staff_sal),0) Total,
ROUND(AVG(staff_sal),0) Average FROM staff_master
GROUP BY dept_code

---Question - 2
SELECT dept_code,COUNT(mgr_code) 'Total Number of Managers' FROM staff_master
GROUP BY dept_code

---Question - 3
SELECT dept_code,SUM(staff_sal) 'Total Salary' FROM staff_master
WHERE mgr_code IS NULL
GROUP BY dept_code HAVING SUM(staff_sal)>20000