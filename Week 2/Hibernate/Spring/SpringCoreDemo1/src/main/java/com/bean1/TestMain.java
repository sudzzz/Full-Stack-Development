package com.bean1;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class TestMain {

	public static void main(String[] args) {
		ApplicationContext context=new ClassPathXmlApplicationContext("Springstudent.xml");
        Student st=(Student)context.getBean("s");
        st.sayHello();
	}

}
