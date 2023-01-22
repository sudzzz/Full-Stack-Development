package com.bean;
import org.hibernate.*;
import org.hibernate.cfg.*;
import java.util.*;

import javax.persistence.TypedQuery;

public class TestMain {

	public static void main(String[] args)
	{

		Configuration cfg = new Configuration();
		cfg.configure("hibernate.cfg.xml"); 

		SessionFactory factory = cfg.buildSessionFactory();
		Session session = factory.openSession();

		
		org.hibernate.query.Query qry = session.createQuery("from Employee p");
		
		List l =qry.list();
		System.out.println("Total Number Of Records : "+l.size());
		Iterator it = l.iterator();

		while(it.hasNext())
		{
			Object o = (Object)it.next();
			Product p = (Product)o;
			System.out.println("Product id : "+p.getProductId());
			System.out.println("Product Name : "+p.getProName());
			System.out.println("Product Price : "+p.getPrice());
			System.out.println("----------------------");
		}		
*/
	

/* Selecting all objects(records) end________________________ */		

/* Selecting partial objects(More than one object) start__________ */		
/*
org.hibernate.query.Query qry = session.createQuery("select p.productId,p.proName from Product p");

		List l =qry.list();
		System.out.println("Total Number Of Records : "+l.size());
		Iterator it = l.iterator();

		while(it.hasNext())
		{
			Object o[] = (Object[])it.next();

			System.out.println("Product id : "+o[0]+ "Product Name : "+o[1]);

			System.out.println("----------------");
		}			
*/
	
/* Selecting partial objects(More than one object)end_____________ */				

// Selecting single object start_____________

/*     org.hibernate.query.Query qry = session.createQuery("select p.productId from Product p");

		List l =qry.list();
		System.out.println("Total Number Of Records : "+l.size());
		Iterator it = l.iterator();

		while(it.hasNext())
		{
			Integer i = (Integer)it.next();
			System.out.println("Product id : "+i.intValue());
			System.out.println("---------------------------");

		}	
	*/	
		//=========================================TypedQuery
		
		TypedQuery<Product> qry1 = session.createQuery("from Product p");
       
		List<Product> li =qry1.getResultList();
		System.out.println("Total Number Of Records : "+li.size());
		for(Product p:li)
		{
			
			System.out.println("Product id : "+p.getProductId());
			System.out.println("Product Name : "+p.getProName());
			System.out.println("Product Price : "+p.getPrice());
			System.out.println("----------------------");
		}	
		factory.close();
	}
}
