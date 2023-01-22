package com.bean1;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import javax.persistence.PrimaryKeyJoinColumn;
import javax.persistence.Table;

@Entity
@Table(name="EMPLOYEE12")
public class Employee10
{
    @Id
    @GeneratedValue
    @Column(name="EMP_ID")
    private int empId;
    
    @Column(name="NAME")
    private String empName;

    @OneToOne(cascade = CascadeType.ALL)
    @PrimaryKeyJoinColumn
   // @JoinColumn(name ="addrId")
    private Employee_Address10 employeeAddress;
    
    /* @OneToOne – This annotation on the employeeAddress property of the 
     * Employee class indicates that there exist one to one association 
     * between Employee_Address Entity and Employee Entity. We have also used
     *  “cascade = CascadeType.ALL” since the Employee_Address Entity cannot
     *   exist without Employee Entity. If we used this setting whenever the
     *    Employee is updated Employee_Address also will be updated.
@PrimaryKeyJoinColum – This annotation indicates that the primary key of the
 Employee Entity will act as the foreign key for the Employee_Address Entity..*/

    public Employee10()
    {
        super();
    }

    public Employee10(int empId, String empName, Employee_Address10 employeeAddress)
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

    public Employee_Address10 getEmployeeAddress()
    {
        return employeeAddress;
    }

    public void setEmployeeAddress(Employee_Address10 employeeAddress)
    {
        this.employeeAddress = employeeAddress;
    }

    @Override
    public String toString()
    {
        return "Employee [empId=" + empId + ", empName=" + empName + ", employeeAddress=" + employeeAddress + "]";
    }
}
