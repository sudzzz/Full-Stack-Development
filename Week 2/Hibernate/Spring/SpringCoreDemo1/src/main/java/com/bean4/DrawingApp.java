 package com.bean4;


import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.context.support.FileSystemXmlApplicationContext;


public class DrawingApp {

	public static void main(String[] args) {

		ApplicationContext context = new FileSystemXmlApplicationContext
				("F:\\ducatBathes\\Eclipsworkspace\\SpringDemo1\\src\\spring4.xml") ;
		/*FileSystemXmlApplicationContext to create the factory bean after
		 *  loading the bean configuration file from the given path.
		 * takes care of creating and initializing all the objects 
		 * ie. beans mentioned in the XML bean configuration file.
		 * */
		Traingle tg=(Traingle)context.getBean("t");
		/* getBean() method of the created context.
		 *  This method uses bean ID to return a generic object, 
		 *  which finally can be casted to the actual object.
		 *  Once you have an object, you can use this object to call any class method.
		 * 
		 * */
		tg.draw();

	//	Traingle tg1=(Traingle)context.getBean("t1");
	//	tg1.draw();
		

	}

}
