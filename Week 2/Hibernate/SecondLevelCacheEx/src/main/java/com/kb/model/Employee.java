package com.kb.model;

import javax.persistence.Column;
/*Secondary cache is associated with the SessionFactory and hence its available to the entire application.

So objects kept in the secondary cache are available across multiple sessions.

Once the session factory is closed, secondary cache is cleared.


How secondary cache works ?

Whenever we try to load an entity , Hibernate first looks at a primary cache associated with a particular session.

If cached entity is found in the primary cache itself then it will be returned.

If requested entity is not found in primary cache,then hibernate looks at the second level cache.

If requested entity is found in second level cache,then it will be returned.

If requested entity is not found in secondary cache then database call is made to get the entity and it will be kept in both primary and secondary cache and then it will be returned.


How to enable secondary cache ?

We just need to follow 3 simple steps to enable secondary cache.

1) Add below configuration setting in hibernate.cfg.xml file

< property name=”cache.provider_class” >org.hibernate.cache.EhCacheProvider< /property >

< property name=”hibernate.cache.use_second_level_cache” >true< /property >

2) Add cache usage setting in hbm file or annotated class as below

XML file – < cache usage="read-only" / >

Annotated class – @Cache(usage=CacheConcurrencyStrategy.READ_ONLY, region=”employeeCache”)

3) Create ehcache.xml file to configure the cache region

 * 
 * */
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import org.hibernate.annotations.Cache;
import org.hibernate.annotations.CacheConcurrencyStrategy;

@Entity
@Table(name="Employee")
@Cache(usage=CacheConcurrencyStrategy.READ_ONLY, region="employeeCache")
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