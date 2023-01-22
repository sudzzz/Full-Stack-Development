package com.bean;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name="EMPLOYEE1")
public class Employee
{
    @Id
    @GeneratedValue
    @Column(name="EMP_ID")
    private int empId;
    
    @Column(name="NAME")
    private String empName;

    @OneToOne(mappedBy="employee")
    private Employee_Address employeeAddress;
    /* annotation on the employeeAddress property of the Employee class indicates
     *  that there exist one to one association between Employee_Address Entity. 
     *  We have also used the mappedBy attribute as “employee” 
     * this indicates that this side is not the owner of the relationship.*/

    public Employee()
    {
        super();
    }

    public Employee(int empId, String empName, Employee_Address employeeAddress)
    {
        super();
        this.empId = empId;
        this.empName = empName;
        this.employeeAddress = employeeAddress;
    }

    public int getEmpId()
    {
        return empId;
    }

    public void setEmpId(int empId)
    {
        this.empId = empId;
    }

    public String getEmpName()
    {
        return empName;
    }

    public void setEmpName(String empName)
    {
        this.empName = empName;
    }

    public Employee_Address getEmployeeAddress()
    {
        return employeeAddress;
    }

    public void setEmployeeAddress(Employee_Address employeeAddress)
    {
        this.employeeAddress = employeeAddress;
    }

    @Override
    public String toString()
    {
        return "Employee [empId=" + empId + ", empName=" + empName + ", employeeAddress=" + employeeAddress + "]";
    }
}