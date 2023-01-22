package com.bean6;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class Circle {

	
	Point center;

	public Point getCenter() {
		return center;
	}

	@Autowired
	@Qualifier("circleratlated")
	public void setCenter(Point center) {
		this.center = center;
	}
	
	
}
