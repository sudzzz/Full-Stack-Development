package com.bean6;

public class Triangle {
	
	Point pointA;
	Point pointB;
	Point pointC;
	public Point getPointA() {
		return pointA;
	}
	public void setPointA(Point pointA) {
		this.pointA = pointA;
	}
	public Point getPointB() {
		return pointB;
	}
	public void setPointB(Point pointB) {
		this.pointB = pointB;
	}
	public Point getPointC() {
		return pointC;
	}
	public void setPointC(Point pointC) {
		this.pointC = pointC;
	}
	
	public void draw()
	{
		System.out.println("PointA "+getPointA().getX()+" , "+getPointA().getY());
		System.out.println("PointB "+getPointB().getX()+" , "+getPointB().getY());
		System.out.println("PointC "+getPointC().getX()+" , "+getPointC().getY());
		
	}
	

}
