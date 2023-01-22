package com.bean6;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.bean6.Triangle;


public class DrawingApp {

	public static void main(String[] args) {

		ApplicationContext context1=new ClassPathXmlApplicationContext("spring6.xml");
		Triangle tg=(Triangle) context1.getBean("t");
		
		tg.draw();
		
		ApplicationContext context2=new ClassPathXmlApplicationContext("spring6Autowire.xml");
	Circle c=(Circle) context2.getBean("circle");
		
		System.out.println(c.getCenter().getX()+", "+c.getCenter().getY());
		

	}

}
