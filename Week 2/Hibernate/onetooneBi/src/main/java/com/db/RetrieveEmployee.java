package com.db;

import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import com.bean.Employee;
import com.bean.Employee_Address;
import com.util.HibernateUtil;

public class RetrieveEmployee {

	
	public static void main(String[] args) {
        // Get session factory using Hibernate Util class
        SessionFactory sf = HibernateUtil.getSessionFactory();
        // Get session from Sesson factory
        Session session = sf.openSession();
 
        // Begin transaction
        Transaction t = session.beginTransaction();
        // Retrieving Employee 
        System.out.println("** Employee Address through Employee **");
        @SuppressWarnings("deprecation")
		List<Employee> empList = session.createQuery("from Employee1").list();
        for(Employee employee : empList)
        {
            System.out.println("** Employee Details **");
            System.out.println("Employee Id   : "+ employee.getEmpId());
            System.out.println("Employee Name : "+  employee.getEmpName());
            
            //Retrieving 
            System.out.println("** Employee Address Details **");
            Employee_Address employeeAddress = employee.getEmployeeAddress();
            System.out.println("Address ID  : " + employeeAddress.getAddrId());
            System.out.println("Street      : " + employeeAddress.getStreet());
            System.out.println("City        : " + employeeAddress.getCity());
            System.out.println("State       : " + employeeAddress.getState());
            System.out.println("Country     : " + employeeAddress.getCountry());
        }
        
        System.out.println("*** Retrieving Employee through Employee Address *** ");
        @SuppressWarnings("deprecation")
		List<Employee_Address> addrList = session.createQuery("from Employee_Address1").list();
        for(Employee_Address employeeAddress : addrList)
        {   
            System.out.println("** Employee Details **");
            Employee employee = employeeAddress.getEmployee();
            System.out.println("Employee Id   : "+ employee.getEmpId());
            System.out.println("Employee Name : "+  employee.getEmpName());
            
            //Retrieving 
            System.out.println("** Employee Address Details **");
            System.out.println("Address ID  : " + employeeAddress.getAddrId());
            System.out.println("Street      : " + employeeAddress.getStreet());
            System.out.println("City        : " + employeeAddress.getCity());
            System.out.println("State       : " + employeeAddress.getState());
            System.out.println("Country     : " + employeeAddress.getCountry());
        }
        //Close the session
        session.close();
}
}