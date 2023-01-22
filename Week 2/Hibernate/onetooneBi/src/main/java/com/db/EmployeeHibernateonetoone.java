package com.db;



	import java.util.Calendar;
	import java.util.Date;
	 
	import org.hibernate.Session;
	import org.hibernate.SessionFactory;
	import org.hibernate.Transaction;

import com.bean.Employee;
import com.bean.Employee_Address;

import com.util.HibernateUtil;
	 
	public class EmployeeHibernateonetoone {
	    public static void main(String[] args) {
	        // Get session factory using Hibernate Util class
	        SessionFactory sf = HibernateUtil.getSessionFactory();
	        // Get session from Sesson factory
	        Session session = sf.openSession();
	 
	        // Begin transaction
	        Transaction t = session.beginTransaction();
	     // Create a Employee object
	        Employee employee = new Employee();
	        employee.setEmpName("Employee  22");
	        
	        // Create a Employee_Address object
	        Employee_Address employeeAddress = new Employee_Address();
	        employeeAddress.setStreet("Street 22");
	        employeeAddress.setCity("City 22");
	        employeeAddress.setState("State 22");
	        employeeAddress.setCountry("Country 22");
	        
	        employee.setEmployeeAddress(employeeAddress);
	        employeeAddress.setEmployee(employee);
	     //   session.save(employee);
	        //Save the Employee_Address object
	        session.save(employeeAddress);
	        
	        //Commit the changes
	        session.getTransaction().commit();
	        
	        //Close the session
	        session.close();
	    }
	}