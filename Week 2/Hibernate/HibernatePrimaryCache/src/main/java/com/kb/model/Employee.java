package com.kb.model;

import javax.persistence.Column;
/*
 * Primary cache is associated with Session and its enabled by default.

So we don’t need to configure anything to enable the Primary cache in our application.

Since it is associated with Session, primary cache will be available as long as hibernate session is alive.

Once the session is closed, all the objects in the cache will be lost.


Important points about Primary cache

Primary cache is always associated with “Hibernate Session”

Primary cache is enabled by default and we don’t need to do any additional settings to enable it.

Primary cache can not be disabled but can be cleared.

When we query for an entity , first time it loads from database and it will keep it in the First level cache associated with the Session.

If we request the same entity using same session again , then it will be loaded from cache and no database call will be made.

If we want to remove a specific entity from primary cache , we can use evict() method.

If we want to remove all the objects stored in the primary cache, then we can use clear() method.
 * 
 * 
 * */
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="Employee")
public class Employee {
	@Id
	@GeneratedValue(strategy = GenerationType.SEQUENCE)
	@Column(name = "Employee_Id")
	private int employeeId;
	
	@Column(name = "FirstName")
	private String firstName;
	
	@Column(name = "LastName")
	private String lastName;
	
	@Column(name = "Age")
	private int age;
	
	@Column(name = "Education")
	private String education;
	
	@Column(name = "Salary")
	private int salary;
	
	public int getEmployeeId() {
		return employeeId;
	}
	public void setEmployeeId(int employeeId) {
		this.employeeId = employeeId;
	}
	public String getFirstName() {
		return firstName;
	}
	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}
	public String getLastName() {
		return lastName;
	}
	public void setLastName(String lastName) {
		this.lastName = lastName;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getEducation() {
		return education;
	}
	public void setEducation(String education) {
		this.education = education;
	}
	public int getSalary() {
		return salary;
	}
	public void setSalary(int salary) {
		this.salary = salary;
	}
}