package com.kb.db;

import java.util.Iterator;
import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.criterion.Criterion;
import org.hibernate.criterion.Projection;
import org.hibernate.criterion.ProjectionList;
import org.hibernate.criterion.Projections;
import org.hibernate.criterion.Restrictions;

import com.kb.model.Employee;
import com.kb.util.HibernateUtil;

public class CriteriaMain {

	public CriteriaMain() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// Get session factory using Hibernate Util class
		SessionFactory sf = HibernateUtil.getSessionFactory();

		// Get session from Sesson factory
		Session session = sf.openSession();
		
		org.hibernate.Criteria crit = session.createCriteria(Employee.class);
         
		Projection projections1=Projections.property("id");
		
		Projection projections2=Projections.property("name");
		
		ProjectionList projectionList=Projections.projectionList();
		projectionList.add(projections1);
		projectionList.add(projections2);
		
		crit.setProjection(projectionList);
		
		
		List list=crit.list();
		
		

		List l=crit.list();
		System.out.println("List total size..._"+l.size());
		Iterator it=l.iterator();
		

	}

}
