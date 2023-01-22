package com.bean;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import jakarta.transaction.HeuristicMixedException;
import jakarta.transaction.HeuristicRollbackException;
import jakarta.transaction.RollbackException;
import jakarta.transaction.SystemException;
import jakarta.transaction.Transaction;

public class TestMain {

	@SuppressWarnings("deprecation")
	public static void main(String[] args) throws Exception, IllegalStateException, RollbackException, HeuristicMixedException, HeuristicRollbackException, SystemException {
		Configuration cfg=new Configuration();
	    cfg.configure("hibernate.cfg.xml");	        

	    SessionFactory factory = cfg.buildSessionFactory();
	    Session session = factory.openSession();

		Student  s = new Student();
		s.setsId(10);
		s.setsName("ss");

				org.hibernate.Transaction  tx = session.beginTransaction();
		session.save(s);
		
		tx.commit();
		session.close();
		System.out.println("One to One with annotations is done..!!!!");
		factory.close();
	}

}
