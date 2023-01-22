package com.bean;

public class notes {

	/* 
	 * Only change in this relationship( ManyToMany Bidirectional) and ManyToMany Unidirectional is that, in the Subject class we have added following property.

@ManyToMany(mappedBy="subjects")
private List<Student> students = new ArrayList<Student>();
Nothing else changes.We added this property in Subject class to make the relationship bidirectional.You can now navigate from Subject to Student.mappedBy attribute tells that this is the inverse side of relationship which is managed by “subjects” property of Student annotated with @JoinColumn.

If you prefer to recall (as in Unidirectional) , owner side of relationship is defined in Student class as follows

@ManyToMany(cascade = CascadeType.ALL)
@JoinTable(name = "STUDENT_SUBJECT", 
    joinColumns = { @JoinColumn(name = "STUDENT_ID") }, 
    inverseJoinColumns = { @JoinColumn(name = "SUBJECT_ID") })
private List<Subject> subjects = new ArrayList<Subject>();
@ManyToMany indicates that there is a Many-to-Many relationship between Student and subject. A Student can enroll for multiple subjects, and a subject can have multiple students enrolled.Notice cascade = CascadeType.ALL, with cascading while persisting (update/delete) Student tuples, subjects tuples will also be persisted (updated/deleted).

@JoinTable indicates that there is a link table which joins two tables via containing there keys.This annotation is mainly used on the owning side of the relationship.joinColumns refers to the column name of owning side(STUDENT_ID of STUDENT), and inverseJoinColumns refers to the column of inverse side of relationship(SUBJECT_ID of SUBJECT).Primary key of this joined table is combination of STUDENT_ID & SUBJECT_ID.

One important remark : In case of *Many* association, always override hashcode and equals method which are looked by hibernate when holding entities into collections.
	 * */
}
