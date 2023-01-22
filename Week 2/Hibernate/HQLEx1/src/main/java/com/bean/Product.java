package com.bean;

import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;

//@Entity
public class Product {
	//@Id
	//@GeneratedValue(strategy=GenerationType.IDENTITY)
	private int productId;
	private String proName;
	private double price;

	public void setProductId(int productId)
	{
	    this.productId = productId;
	}
	public int getProductId()
	{
	    return productId;
	}

	public void setProName(String proName)
	{
	    this.proName = proName;
	}
	public String getProName()
	{
	    return proName;
	}

	public void setPrice(double price)
	{
	    this.price = price;
	}
	public double getPrice()
	{
	    return price;
	}

}
