package com.bean;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name="EMPLOYEE_ADDRESS1")
public class Employee_Address
{
    @Id
    @Column(name = "ADDR_ID")
    @GeneratedValue
    private int addrId;
    
    @Column(name="STREET")
    private String street;
    @Column(name="CITY")
    private String city;
    @Column(name="STATE")
    private String state;
    @Column(name="COUNTRY")
    private String country;
    
    @OneToOne(cascade= CascadeType.ALL)
    @JoinColumn(name ="EMP_ID")
    private Employee employee;
    
    /*@JoinColumn annotation indicates that this entity will act as the owner of 
     * the relationship 
     * (This table has a column with a foreign key to the referenced table)*/

    public Employee_Address()
    {
        super();
    }

    public Employee_Address(int addrId, String street, String city, String state, String country, Employee employee)
    {
        super();
        this.addrId = addrId;
        this.street = street;
        this.city = city;
        this.state = state;
        this.country = country;
        this.employee = employee;
    }

    public int getAddrId()
    {
        return addrId;
    }

    public void setAddrId(int addrId)
    {
        this.addrId = addrId;
    }

    public String getStreet()
    {
        return street;
    }

    public void setStreet(String street)
    {
        this.street = street;
    }

    public String getCity()
    {
        return city;
    }

    public void setCity(String city)
    {
        this.city = city;
    }

    public String getState()
    {
        return state;
    }

    public void setState(String state)
    {
        this.state = state;
    }

    public String getCountry()
    {
        return country;
    }

    public void setCountry(String country)
    {
        this.country = country;
    }

    public Employee getEmployee()
    {
        return employee;
    }

    public void setEmployee(Employee employee)
    {
        this.employee = employee;
    }

    @Override
    public String toString()
    {
        return "Employee_Address [addrId=" + addrId + ", street=" + street + ", city=" + city + ", state=" + state
                + ", country=" + country + ", employee=" + employee + "]";
    }
}