package com.bean;
import org.hibernate.*;
import org.hibernate.cfg.*;
import java.util.*;

import javax.persistence.TypedQuery;

public class TestMain1 {

	

	public static void main(String[] args) {
		

				Configuration cfg = new Configuration();
				cfg.configure("hibernate.cfg.xml"); 

				SessionFactory factory = cfg.buildSessionFactory();
 				Session session = factory.openSession();		

		// Using label...............

	 /*      org.hibernate.query.Query qry = session.createQuery("from Product p where p.productId= :jaya");
		       qry.setParameter("jaya",1);

				List l =qry.list();
				System.out.println("Total Number Of Records : "+l.size());
				Iterator it = l.iterator();

				while(it.hasNext())
				{
					Object o = (Object) it.next();
					Product p = (Product)o;
					System.out.println("Product Name : "+p.getProductId());
					System.out.println("Product Name : "+p.getProName());
					System.out.println("Product Price : "+p.getPrice());
					System.out.println("---------------------------");

				}	

		*/	

		/* Using Question Mark  */

		/*		org.hibernate.query.Query qry = session.createQuery("from Product p where p.productId= ?");
			        qry.setParameter(0,1);

					List l =qry.list();
					System.out.println("Total Number Of Records : "+l.size());
					Iterator it = l.iterator();

					while(it.hasNext())
					{
						Object o = (Object) it.next();
						Product p = (Product)o;
						System.out.println("Product Name : "+p.getProName());
						System.out.println("Product Price : "+p.getPrice());
						System.out.println("---------------------------");

					}		
				*/
				//----------------TypedQuery
				
				TypedQuery<Product> qry = session.createQuery("from Product p where p.productId= :x");
			       qry.setParameter("x", 1);
				List<Product> l =qry.getResultList();
				System.out.println("Total Number Of Records : "+l.size());
				for(Product p:l)
				{
					
					System.out.println("Product id : "+p.getProductId());
					System.out.println("Product Name : "+p.getProName());
					System.out.println("Product Price : "+p.getPrice());
					System.out.println("----------------------");
				}
				session.close();
				factory.close();
			}


}
