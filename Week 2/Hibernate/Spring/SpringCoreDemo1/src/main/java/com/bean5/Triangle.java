package com.bean5;

import org.springframework.stereotype.Component;

@Component
public class Triangle {

	String type;
	int height;
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public int getHeight() {
		return height;
	}
	public void setHeight(int height) {
		this.height = height;
	}
	
	public void draw()
	{
		System.out.println("Triangle's name "+getType()+"and height "+getHeight());
	}
	
	
}
