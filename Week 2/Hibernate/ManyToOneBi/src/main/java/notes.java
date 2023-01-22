
public class notes {

	/*
	 * @OneToMany(mappedBy = "university", cascade = CascadeType.ALL)
private List<Student> students;
@OneToMany on list property here denotes that one University can have multiple students.With students property defined in University class, we can now navigate from University to students. mappedBy says that it’s the inverse side of relationship.Also note the cascade attribute, which means the dependent object(Student) will be persisted/updated/deleted automatically on subsequent persist/update/delete on University object.No need to perform operation separately on Student.

On the other hand, we have following in Student

@ManyToOne(optional = false)
@JoinColumn(name = "UNIVERSITY_ID")
private University university;
@JoinColumn says that Student table will contain a separate column UNIVERSITY_ID which will eventually act as a foreign key reference to primary key of University table. @ManyToOne says that multiple Student tuples can refer to same University Tuples(Multiple students can register in same university).Additionally , with optional=false we make sure that no Student tuple can exist without a University tuple.
	 * 
	 * */

}
