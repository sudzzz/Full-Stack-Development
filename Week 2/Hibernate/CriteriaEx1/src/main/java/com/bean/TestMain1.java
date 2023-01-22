package com.bean;
import org.hibernate.*;
import org.hibernate.cfg.*;
import org.hibernate.criterion.Criterion;
import org.hibernate.criterion.Restrictions;

import java.util.*;

public class TestMain1 {

	
		@SuppressWarnings("unchecked")
		public static void main(String[] args)
		{

			Configuration cfg = new Configuration();
			cfg.configure("hibernate.cfg.xml"); 

			SessionFactory factory = cfg.buildSessionFactory();
			Session session = factory.openSession();

			
			org.hibernate.Criteria crit = session.createCriteria(Product.class);
			Criterion cn = Restrictions.gt("price",new Double(10));
			
			crit.add(cn);
			
			List l=crit.list();
			System.out.println("List total size..._"+l.size());
			Iterator it=l.iterator();

			while(it.hasNext())
			{
				Product p=(Product)it.next();
				System.out.println(p.getProductId());
				System.out.println(p.getProName());
				System.out.println(p.getPrice());
				System.out.println("-----------------");
			}

			session.close();
			factory.close();
		}


	}


