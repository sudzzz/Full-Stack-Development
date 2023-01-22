package com.bean5;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp {

	public static void main(String[] args) {
		/*ApplicationContext context=new ClassPathXmlApplicationContext("spring5.xml");
		
		Triangle tg=(Triangle) context.getBean("t");
		tg.setType("right");
		tg.setHeight(12);
		tg.draw();
		
		Triangle tg1=(Triangle) context.getBean("t");
		tg1.draw();
		*/
		//@componenet
		
		
		ApplicationContext context1=new ClassPathXmlApplicationContext("spring5compnenet.xml");
		Triangle tg2=(Triangle) context1.getBean("triangle");
		tg2.setType("right");
		tg2.setHeight(12);
		tg2.draw();
		
		
	}

}
