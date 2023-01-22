package com.bean;

import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;

public class DrawingApp {

	public static void main(String[] args) {
		//Traingle t=new Traingle();
		
		
		BeanFactory factory=new XmlBeanFactory(new FileSystemResource("spring.xml"));
		Traingle tg=(Traingle) factory.getBean("t");
		tg.draw();

	}

}
