"""Tuples in python:- A Tuples is a data structure used to store multiple values in one variables./ A tuples is a collection of different datatypes which is ordered & unchangeable(immutable).
  - Tuples are written using Parentheses ().
  - tuples items are separated by commas.
  - tuples are ordered ,so items have index position.
  - tuples allows duplicate values .
  - tuples can store different datatypes.
  - We can not use add,insert, remove,methods in a tuples,because it is not modifiable (mutable)."""

'''Syntax:- 
         * Empty tuple:- Creating an empty tuple.
            student=()  #empty tuple
            student=tuple()   #using the tuples constructor.
            
         * Tuple with initial values:-
            tpl=('items1','items2','items3',)   '''

#Tuple Length:- we use the len() method to get length of a tuple
tpl=('rahul','abhi',10,200,24.4,"Aman",True)
print(tpl)
print(len(tpl))

'''Single-item tuple:-
     - A single-item tuple must contain a comma.
     - Without the comma,Python does not treat it as a tuple.
     - Parentheses alone are not enough.
       - Syntax:- tuple_name=(value)
           '''
a=('python',)
b=('python')
print(type(a))
print(type(b))

#Accessing Tuple values /items:-
students=('rahul','aman','riya','kabir','abhi')
first_stud=students[0]
print(first_stud)
last_stud=len(students)-1
last_stud=students[last_stud]
print(last_stud)
print(students[2])
print(students[-1])
print(students[-4])

"""Slicing Tuples:- We can slice out a sub-tuple byspecifying a range of index where to start & where to end & step in the tuple.The return value will be a new tuple with the specified items.
    Syntax:- tpl=('item1','item','item','item')
             all_item=tpl[0:3]
             all_item=tpl[0:]
             middle_item=tpl[1:4:2]
            """

numbers=(10,20,30,40,50,60,70,80,90,100)
all_numbers=numbers[0:10]
print(all_numbers)
all_items=numbers[0:]
print(all_items)
print(numbers[1:10])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])
print(numbers[::-1])
print(numbers[-4:])
print(numbers[-3:-8])
print(numbers[:])
print(numbers[1:10:2])


"""Changing Tuples to Lists:-We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
 Syntax
     tpl = ('item1', 'item2', 'item3','item4')
     lst = list(tpl)"""
fruits=('banana','orange','apple','lemon','guava')
fruitses=list(fruits)
print(fruitses)
fruitses[0]='mango'
print(fruitses)
fruits=tuple(fruitses)
print(fruits)

"""Checking an Item in a Tuple:-We can check if an item exists or not in a tuple using in, it returns a boolean.
     Syntax
       tpl = ('item1', 'item2', 'item3','item4')
       print('item2' in tpl) # True
       print('item2' not in tpl) #fales"""
fruits=('mango','banana','apple','orange','guava')
print('orange' in fruits)
print('orange' not in fruits)

"""Joining Tuples:-We can join two or more tuples using + operator
 syntax
     tpl1 = ('item1', 'item2', 'item3')
     tpl2 = ('item4', 'item5','item6')
     tpl3 = tpl1 + tpl2"""
fruits=('mango','banana','apple','orange','guava')
veg=('potato','tomato','onion')
veg_fru=fruits+veg
print(veg_fru)

"""Deleting Tuples:-
 It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del."""
    
tpl1 = ('item1', 'item2', 'item3')
del tpl1
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits