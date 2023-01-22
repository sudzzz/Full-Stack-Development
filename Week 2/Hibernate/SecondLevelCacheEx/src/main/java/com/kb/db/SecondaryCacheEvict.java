package com.kb.db;

import org.hibernate.Session;
import org.hibernate.SessionFactory;

import com.kb.model.Employee;
import com.kb.util.HibernateUtil;

public class SecondaryCacheEvict {
	public static void main(String[] args) {
		// Get session factory using Hibernate Util class
		SessionFactory sf = HibernateUtil.getSessionFactory();

		// Get session from Session factory
		Session session1 = sf.openSession();

		// Load the Employee details whose Id is 1
		Employee employee = (Employee) session1.load(Employee.class, new Integer(1));
		displayEmployeeDetails(employee);
		session1.close();

		sf.getCache().evictAll();

		Session session2 = sf.openSession();

		// Load the same Employee again within the same Session but after evict
		employee = (Employee) session2.load(Employee.class, new Integer(1));
		displayEmployeeDetails(employee);

		session2.close();
	}

	private static void displayEmployeeDetails(Employee employee) {
		System.out.println("ID: " + employee.getEmployeeId() + " Age: " + employee.getAge() + " Salary: " + 
                                   employee.getSalary());
	}

}