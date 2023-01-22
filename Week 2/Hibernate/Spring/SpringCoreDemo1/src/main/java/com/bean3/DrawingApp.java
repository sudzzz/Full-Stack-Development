package com.bean3;


import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class DrawingApp {

	public static void main(String[] args) {

		
		ApplicationContext context= new ClassPathXmlApplicationContext("spring2.xml");
		
		Traingle tg=(Traingle)context.getBean("t");
		tg.draw();

	}

}
