package com.bean4;



public class Traingle {
	
	private String type;
	private int height;
	
	public Traingle(String type){
		this.type=type;
	}
	public Traingle(int height){
		this.height=height;
	}
	
	/*public Traingle(String type,int height){
		this.type=type;
		this.height=height;
	}*/
	
	public String getType() {
		return type;
	}


	public int getHeight() {
		return height;
	}

	public void draw()
	{
		System.out.println(getType()+" Triangle drawn "+getHeight());
	}

}
