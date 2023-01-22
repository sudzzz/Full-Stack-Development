package com.kb.db;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import com.kb.model.Employee;
import com.kb.util.HibernateUtil;

public class Main {
	public static void main(String[] args) {
		Transaction tx = null;
		
			// Get session factory using Hibernate Util class
			SessionFactory sf = HibernateUtil.getSessionFactory();

			// Get session from Sesson factory
			Session session = sf.openSession();

			// Begin transaction
			tx = session.beginTransaction();

			// Creating Employee record
			Employee employee = new Employee();
			employee.setName("John");
			employee.setCity("Newyork");

			session.save(employee);
			
			// Creating Employee1 record
						Employee employee1 = new Employee();
						employee1.setName("John1");
						employee1.setCity("Newyork1");

						session.save(employee1);
						// Creating Employee2 record
						Employee employee2 = new Employee();
						employee2.setName("John2");
						employee2.setCity("Newyork2");

						session.save(employee2);
			
			tx.commit();
			
	}
}