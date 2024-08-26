Accessing Values in Lists
To access values in lists, use the square brackets for slicing along with the index or indices to obtain value available at that index. For example −

 Live Demo
#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print "list1[0]: ", list1[0]
print "list2[1:5]: ",ist2[1:5]
When the above code is executed, it produces the following result −

list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]
Updating Lists
You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator, and you can add to elements in a list with the append() method. For example −

 Live Demo
#!/usr/bin/python

list = ['physics', 'chemistry', 1997, 2000];
print "Value available at index 2 : "
print list[2]
list[2] = 2001;
print "New value available at index 2 : "
print list[2]
Note − append() method is discussed in subsequent section.

When the above code is executed, it produces the following result −

Value available at index 2 :
1997
New value available at index 2 :
2001
Delete List Elements
To remove a list element, you can use either the del statement if you know exactly which element(s) you are deleting or the remove() method if you do not know. For example −

 Live Demo
#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000];
print list1
del list1[2];
print "After deleting value at index 2 : "
print list1
When the above code is executed, it produces following result −

['physics', 'chemistry', 1997, 2000]
After deleting value at index 2 :
['physics', 'chemistry', 2000]
Note − remove() method is discussed in subsequent section.

Basic List Operations
Lists respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new list, not a string.

In fact, lists respond to all of the general sequence operations we used on strings in the prior chapter.

Python Expression	Results	Description
len([1, 2, 3])	3	Length
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	Concatenation
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
3 in [1, 2, 3]	True	Membership
for x in [1, 2, 3]: print x,	1 2 3	Iteration
Indexing, Slicing, and Matrixes
Because lists are sequences, indexing and slicing work the same way for lists as they do for strings.

Assuming following input −

L = ['spam', 'Spam', 'SPAM!']
Python Expression	Results	Description
L[2]	SPAM!	Offsets start at zero
L[-2]	Spam	Negative: count from the right
L[1:]	['Spam', 'SPAM!']	Slicing fetches sections
Built-in List Functions & Methods
Python includes the following list functions −

Sr.No.	Function with Description
1	cmp(list1, list2)
Compares elements of both lists.

2	len(list)
Gives the total length of the list.

3	max(list)
Returns item from the list with max value.

4	min(list)
Returns item from the list with min value.

5	list(seq)
Converts a tuple into list.

Python includes following list methods

Sr.No.	Methods with Description
1	list.append(obj)
Appends object obj to list

2	list.count(obj)
Returns count of how many times obj occurs in list

3	list.extend(seq)
Appends the contents of seq to list

4	list.index(obj)
Returns the lowest index in list that obj appears

5	list.insert(index, obj)
Inserts object obj into list at offset index

6	list.pop(obj=list[-1])
Removes and returns last object or obj from list

7	list.remove(obj)
Removes object obj from list

8	list.reverse()
Reverses objects of list in place

9	list.sort([func])
Sorts objects of list, use compare func if given

#tuple
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
# The differences between tuples and lists are,
#the tuples cannot be changed unlike lists and tuples use parentheses, 
#whereas lists use square brackets.
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];
#tup1[0]:  physics
#tup2[1:5]:  [2, 3, 4, 5]

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3;


tup = ('physics', 'chemistry', 1997, 2000);
print tup;
del tup;
print "After deleting tup : ";
print tup;
#This produces the following result. Note an exception raised,
#this is because after del tup tuple does not exist any more −

('physics', 'chemistry', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
   File "test.py", line 9, in <module>
      print tup;
NameError: name 'tup' is not defined
Basic Tuples Operations:

Python Expression 	       Results                	Description
len((1, 2, 3))	             3	                                  Length
(1, 2, 3) + (4, 5, 6)	    (1, 2, 3, 4, 5, 6)	                  Concatenation
('Hi!',) * 4	         ('Hi!', 'Hi!', 'Hi!', 'Hi!')              	Repetition
3 in (1, 2, 3)	                 True	                                           Membership
for x in (1, 2, 3): print x,	    1 2 3                              	Iteration

Any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples, as indicated in these short examples −

 Live Demo
#!/usr/bin/python

print 'abc', -4.24e93, 18+6.6j, 'xyz';
x, y = 1, 2;
print "Value of x , y : ", x,y;
When the above code is executed, it produces the following result −

abc -4.24e+93 (18+6.6j) xyz
Value of x , y : 1 2

Built-in Tuple Functions
Python includes the following tuple functions −

Sr.No.	Function with Description
1	cmp(tuple1, tuple2)
Compares elements of both tuples.

2	len(tuple)
Gives the total length of the tuple.

3	max(tuple)
Returns item from the tuple with max value.

4	min(tuple)
Returns item from the tuple with min value.

5	tuple(seq)
Converts a list into tuple.
