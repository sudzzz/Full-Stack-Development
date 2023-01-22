package com.bean3;

public class Traingle {
	
	private String type,name;
	private int height;
	
	public Traingle(String type,int height,String name){
		this.type=type;
		this.height=height;
		this.name=name;
		
	}
	/*public Traingle(int height){
		this.height=height;
	}*/
	
	public int getHeight() {
		return height;
	}
	public void setHeight(int height) {
		this.height = height;
	}
	
	public String getType() {
		return type;
	}


	/*public void setType(String type) {
		this.type = type;
	}
*/

	public String getName(){return name;}
	
	public void draw()
	{
		System.out.println(getType()+"  "+getHeight()+"  Triangle drawn"+getName());
	}

}
