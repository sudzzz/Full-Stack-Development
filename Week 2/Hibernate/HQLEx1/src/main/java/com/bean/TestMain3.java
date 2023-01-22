package com.bean;
import org.hibernate.*;
import org.hibernate.cfg.*;
import java.util.*;

public class TestMain3 {



	public static void main(String[] args) {
		Configuration cfg = new Configuration();
		cfg.configure("hibernate.cfg.xml"); 

		SessionFactory factory = cfg.buildSessionFactory();
		Session session = factory.openSession();
		Transaction t = session.beginTransaction();

		org.hibernate.query.Query qry = session.createQuery("insert into Product(productId,proName,price)"
				+ "select i.itemId,i.itemName,i.itemPrice from Items i where i.itemId= ?");
	        qry.setParameter(0,600);
	        int res = qry.executeUpdate();
	        t.commit();

	        System.out.println("Command successfully executed....");
	        System.out.println("Numer of records effected...,"+res);

		session.close();
		factory.close();

	}

}
