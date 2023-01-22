package com.bean;
import org.hibernate.*;
import org.hibernate.cfg.*;
import java.util.*;

import javax.persistence.TypedQuery;
public class TestMain2 {

	
	public static void main(String[] args) {
		Configuration cfg = new Configuration();
		cfg.configure("hibernate.cfg.xml"); 

		SessionFactory factory = cfg.buildSessionFactory();
		Session session = factory.openSession();
		Transaction t = session.beginTransaction();
		
        int res=0;
	        TypedQuery<Product> qry = session.createQuery("delete from Product p where p.productId= :x");
	        qry.setParameter("x",2);
	     
	       res = qry.executeUpdate();
	       t.commit();
	        
	      

	        System.out.println("Command successfully executed....");
	        System.out.println("Numer of records effected due to delete query"+res);

		session.close();
		factory.close();
	}


	}


