package com.db;

import java.util.List;



import java.util.ArrayList;
import org.hibernate.Session;

import com.bean.Student;
import com.bean.University;
import com.util.HibernateUtil;

public class Main {
	 @SuppressWarnings("unchecked")
	    public static void main(String[] args) {
	 
	        Student student1 = new Student("Sam", "Disilva", "Maths");
	        Student student2 = new Student("Joshua", "Brill", "Science");
	        Student student3 = new Student("Peter", "Pan", "Physics");
	 
	        University university = new University("CAMBRIDGE", "ENGLAND");
	        List<Student> allStudents = new ArrayList<Student>();
	 
	        student1.setUniversity(university);
	        student2.setUniversity(university);
	        student3.setUniversity(university);
	 
	        allStudents.add(student1);
	        allStudents.add(student2);
	        allStudents.add(student3);
	 
	        university.setStudents(allStudents);
	 
	        Session session = HibernateUtil.getSessionFactory().openSession();
	        session.beginTransaction();
	 
	        session.persist(university);	 
	        List<Student> students = (List<Student>) session.createQuery("from Student").list();
	        for (Student s : students) {
	            System.out.println("Student Details : " + s);
	            System.out.println("Student University Details: "+ s.getUniversity());
	        }
	 
	        // Note that now you can also access the relationship from University to Student
	 
	        session.getTransaction().commit();
	        session.close();
	    }
	 

}
