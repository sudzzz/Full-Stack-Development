package com.kb.db;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import com.kb.model.Employee;
import com.kb.util.HibernateUtil;

public class PopulateData {
public static void main(String[] args) {

	// Get session factory using Hibernate Util class
	SessionFactory sf = HibernateUtil.getSessionFactory();
	// Get session from Sesson factory
	Session session = sf.openSession();

	// Begin transaction
	Transaction t = session.beginTransaction();
	
	//Create Employee  data
	Employee employee1 = new Employee();
	employee1.setFirstName("John");
	employee1.setLastName("KC");
	employee1.setAge(28);
	employee1.setEducation("PG");
	employee1.setSalary(25000);
	
	Employee employee2 = new Employee();
	employee2.setFirstName("Jacob");
	employee2.setLastName("JC");
	employee2.setAge(30);
	employee2.setEducation("PG");
	employee2.setSalary(30000);
	
	Employee employee3 = new Employee();
	employee3.setFirstName("Martin");
	employee3.setLastName("A");
	employee3.setAge(24);
	employee3.setEducation("UG");
	employee3.setSalary(20000);
	
	Employee employee4 = new Employee();
	employee4.setFirstName("Peter");
	employee4.setLastName("M");
	employee4.setAge(25);
	employee4.setEducation("UG");
	employee4.setSalary(22000);
	
	Employee employee5 = new Employee();
	employee5.setFirstName("Roshan");
	employee5.setLastName("B");
	employee5.setAge(29);
	employee5.setEducation("PG");
	employee5.setSalary(45000);
	
	
	session.save(employee1);
	session.save(employee2);
	session.save(employee3);
	session.save(employee4);
	session.save(employee5);

	// Commit the transaction and close the session
	t.commit();
	
	session.close();
	System.out.println("successfully persisted Employee details");

 }
}