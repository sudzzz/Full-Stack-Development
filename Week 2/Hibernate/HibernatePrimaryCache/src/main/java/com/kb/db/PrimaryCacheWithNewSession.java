package com.kb.db;

import org.hibernate.Session;
import org.hibernate.SessionFactory;

import com.kb.model.Employee;
import com.kb.util.HibernateUtil;

public class PrimaryCacheWithNewSession {
	@SuppressWarnings("deprecation")
	public static void main(String[] args) {
		
		// Get session factory using Hibernate Util class
		SessionFactory sf = HibernateUtil.getSessionFactory();
		
		// Get session from Session factory
		Session session1 = sf.openSession();

		// Load the Employee details whose Id is 1
		Employee employee = (Employee) session1.load(Employee.class, new Integer(1));
		displayEmployeeDetails(employee);

		//Create a new Session
		Session session2 = sf.openSession();
		// Load the same Employee again with new Session
		employee = (Employee) session2.load(Employee.class, new Integer(1));
		displayEmployeeDetails(employee);
		session1.close();
		session2.close();
	}
	private static void displayEmployeeDetails(Employee employee) {
		System.out.println(
				"ID: " + employee.getEmployeeId() + " Age: " + employee.getAge() + " Salary: " + employee.getSalary());
	}

}