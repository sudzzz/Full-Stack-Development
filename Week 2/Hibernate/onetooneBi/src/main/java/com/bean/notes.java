package com.bean;

public class notes {

	/*
 
JPA - Bidirectional OneToOne relationship
[Updated: May 31, 2017, Created: Apr 9, 2017]
Custom Search

A quick overview of bidirectional one-to-one relation in JPA
Just as with unidirectional one-to-one relationship, bidirectional one-to-one relationship has a single target object reference in the source entity, but additionally target entity has a reference back to the source entity as well.
The annotation @OneToOne is used in both source and target classes.
We must use 'mappedBy' element with one of the @OneToOne annotations.
The value of 'mappedBy' element should be the name of the reference variable used in the other class's back reference.
The element 'mappedBy' is needed to specify which side will have the corresponding parent table. Also without 'mappedBy', hibernate will generate the foreign key columns in the both tables. 'mappedBy' must be used to avoid that.
The side which has 'mappedBy' specified, will become the target of the relationship and corresponding table will be the parent of the relationship .
The side which doesn't have 'mappedBy' element will become the source (owner) and the corresponding table will be the child of the relationship, i.e. it will have the foreign key column.
On the owner side, we can also use @JoinColumn, whose one of the purposes is to specify a foreign key column name instead of relying on the default name.
From database perspective, there's no difference, between unidirectional and bidirectional one-to-one relationships, because we can always use the queries to get data in the other direction
	 * 
	 * 
	 * */
}
