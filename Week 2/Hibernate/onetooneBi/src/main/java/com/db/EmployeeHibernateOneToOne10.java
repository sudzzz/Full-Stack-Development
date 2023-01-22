package com.db;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import com.bean1.Employee10;
import com.bean1.Employee_Address10;
import com.util.HibernateUtil;

public class EmployeeHibernateOneToOne10 {

	
	public static void main(String[] args) {
		// Get session factory using Hibernate Util class
        SessionFactory sf = HibernateUtil.getSessionFactory();
        // Get session from Sesson factory
        Session session = sf.openSession();
 
        // Begin transaction
        Transaction t = session.beginTransaction();
        Employee10 employee = new Employee10();
        employee.setEmpName("Employee 111");
        
        Employee_Address10 employeeAddress = new Employee_Address10();
        employeeAddress.setStreet("Street 111");
        employeeAddress.setCity("City 111");
        employeeAddress.setCountry("Country 111");
        employeeAddress.setState("State 111");

        //Setting Bi directional association
        employee.setEmployeeAddress(employeeAddress);
        employeeAddress.setEmployee(employee);
        
        //Save the Employee object
        session.save(employee);
        //Commit the changes
        session.getTransaction().commit();
        //Close the session
        session.close();

	}

}
