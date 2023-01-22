package com.bean2;


import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class DrawingApp {

	public static void main(String[] args) {
		
		ApplicationContext context= new ClassPathXmlApplicationContext("spring1.xml");
		/*ClassPathXmlApplicationContext − This container loads the
		 * definitions of the beans from an XML file.
		 *  Here you do not need to provide the full path of
		 *   the XML file but you need to set CLASSPATH properly because 
		 *  this container will look like bean configuration XML file in CLASSPATH.*/
		
		Traingle tg=(Traingle)context.getBean("t");
		tg.draw();

	}

}
