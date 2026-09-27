"""Set in python :-A set is a data structure used to store multiple unique values.
-sets are written using curly braces {}.
-set items are separaated by commas.
-sets store only uniques values .
-sets are unorderd,so items do not have fixed positions.
-sets are mutable,so we can add or remove items.
-sets elements must be immutable /hashable values.
-sets are unindexed that means no indexing/slicing not allowed.
-set mixed datatypes allowed but can store different immutable type .
-it is possible to find the union,intersection,difference,aymmetric difference,subset,superset,and disjoint set among sets. """

'''Syntax:-
      * Creating an empty set
           st= set()
       * Creating a set with initial items
           st={'item1','items2','items3'}    '''

#Getting sets length :-we can use len() method to find the length of a set.
fruits ={'banana','apple','mango','lemon'}
print(len(fruits))

numbers={10,20,30,40,50,60,70,}
print(numbers) #the output order may look differnt because set are unordered.

"""Creating sets:-
    - sets can store numbers ,strings,booleans,& tuples.
    - sets can not store mutable values like lists or dictionaries.
    - Empty set must be created using set() .{} creates an empty dictonary,not an empty set."""

a={}
b=set()
print(type(a)) #<class 'dict'>
print(type(b)) #<class 'set'>

numberses={10,20,30,40,50,}
name={'suleman','abhi','rahul','roy'}
mixed={"python",'suleman',10,33.33,True}
empty_set=set()
print(numberses)        
print(name)        
print(mixed)        
print(empty_set)        

"""Unique values:- 
   - sets automatically removes duplicates value .
   - Each value appers only once.
   -This makes sets useful for removing duplicates from data.
   - set check uniqueness  using the value ,not position.
   
   Syntax:- set_name={'val1','val2',}  """
numbers={10,20,50,20,60,30,20,}
print(numbers)

numberses={10,20,30,10,40,50,10,}
unique_no=set(numberses)
print(unique_no)

"""Set Elements must be Immutable:- Set element must be hashable.
    - immutable values like numbers,strings ,& tuples can be stored in a set.
    - mutable values like list,dictionaries,& sets cannot be stored in a set.
    -this is because sets internally need stable values to check uniquness."""
valid_set={10,'python',"suleman",(1,2)}
print(valid_set)
# invalid_set={[1,2],[3,4]}
# print(invalid_set) {type error:unhashabl type}

'''Accessing Set values:- set mein indexing nahi hoti ,isliye
     num={10,20,30,40}
     print(num)
     output:-Error
     because set unordered hota hai,set ka values access karna ke liya for loop use karte hain:-'''
num1={10,20,30,40,}
for num1 in num1:
  print(num1)

num2={20,30,60,10}
# print(30 in num1) error aaye ga .

fruits={'apple','banana','mango'}
for fruits in fruits:
  print(fruits)

'''Checking Membership:-
  Syntax:- value in set_name
           value not in set_name '''
numbers2={10,20,30,40,50,670,80}
print(20 in numbers2)    
print(20 not in numbers2)    
print(100 in numbers2)    
print(100 not in numbers2)    

"""Adding set items:- 
- once a set is created we cannot change any items & we can also add items.if an added value exists ,it is not added again."""
# Add one item using add()method:-
''' syntax:- st=('item1','item2','items3')
           st.add('item4')
           print(st)'''
fruits3={'banana','apple','mango','lemon'}
fruits3.add('lime')
print(fruits3)
# Add multiple items using Update()method:-the update () allows to add multiple items to a set.the update() takes a list arguments.
'''syntax:-  st={'items1','items2','items3'}
              st.update(['item4','item5','items6'])'''
fr={'apple','banana'}
fr.update(['orange','lime','lemon'])
print(fr)

num4={10,20,30}
num4.add(40)
num4.update([50,60,20])
print(num4)

"""Removing items from a sets:-
    - remove() remove a specific item ,it give keyerror.
    - discard() also remove a specific item.
    - pop() remove a random item because set are unordered.
    - clear() remove all items.
  syntax:- set_name.remove(value)
           set_name.discard(value)
           set_name.pop()
           set_name.clear() """
numbers4={10,20,30,40,50,60,}
numbers4.remove(20)
print(numbers4)
numbers4.discard(30)
print(numbers4)
numbers4.pop()
print(numbers4)
numbers4.clear()
print(numbers4)

#Deleting a set:- if we want to delete the set itself we use del operator.
fr3={'apple','banana','mango'}
del fr3
# print(fr3)  nameError: fr3 is not defined.

'''Converting list to set:- we can convert a list to a set using set & set to list .converting list to set is useful to remove duplicates from a list.'''
fruits5=['apple','banana','mango','lemom']
fruits_set=set(fruits5)
print(fruits_set)

"""Set Operaions:- Set operations are used to compare or combine sets.
 manin set operations:-Union,Intersection, difference,symmetric difference,Subset,Superset,disjoint."""

#Union:-we can join two sets using the union() or Update() methods or | symbols. the union method returns a new set.
'''syntax:- str1={'item1','item2','item3'}
            str2={'item4','item5','item6'}
            str3=str1.union(str2)'''
fru={'apple','banana','mango'}
vega={'cabage','tomato','potato'}
print(fru.union(vega)) #or using:-print(fru|vega)

#Update():-this methods inserts a set  into a given set.
''' syntax:- str1={'item1','item2','item3'}
            str2={'item4','items5'}
            str1.update(str2) {str2 content are added to str1}'''

fruitses={'apple','banana','oranges'}
vegat={'potato','tomato','onion'}
fruitses.update(vegat)
print(fruitses)

a={1,2,3}
b={3,4,5}
result=a.union(b)
print(result)

# Intersection:- intersection returns only common values.
'''syntax:- str1={'item1','item2',}
            str2={'item2','item3}
            str1.intersection(str2)  or using: str1 & str2 # {'item2'}'''
whole_no={0,1,2,3,4,5}
even_no={2,4,6}
print(whole_no.intersection(even_no)) 

python={'p','y','t','h','o','n'}
dragon={'d','r','a','g','o','n'}
print(python.intersection(dragon)) # or python & dragon.

a={1,2,3,4}
b={4,5,6,7,}
result=a.intersection(b)
print(result)

'''Difference:- difference returns values present inthe first set but not in the second set.
    - a-b and b-a can give different  results.
      syntax:- 1:- set1 - set2
               2:- set1.difference(set2) '''
whole_no={0,1,2,3,4,5,6,7,8,9,10}
even_no={0,2,4,6,8,10}
print(whole_no.difference(even_no))

python={'p','y','t','h','o','n'}
dragon={'d','r','a','g','o','n'}
print(python.difference(dragon))
print(dragon.difference(python))

'''Symmetric difference:- symmetric difference returns values that are not common.
   Syntax:- 1:- set1 ^ set2
            2:- set1.symmetric_difference(set2) '''

whole_no={0,1,2,3,4,5,6,7,8,9,10}
even_no={0,2,4,6,8}
print(whole_no.symmetric_difference(even_no))

python={'p','y','t','h','o','n'}
dragon={'d','r','a','g','o','n'}
print(python.symmetric_difference(dragon))

"""Superset,Subset & Disjoint:-
    superset: issuperset()
    subset: issubset()
    disjoint: isdisjont()
    
    -A subset means all values of one set exist inside another set.
    -A superset means one set containts all values of another set.
    -Disjoint sets have no common values.
    
     syntax:- set1.issubset()
              set1.issuperset()
              set1.isdisjoint() """

whole_no={0,1,2,3,4,5,6,7,8,9,10}
even_no={0,2,4,6,8,10}
print(whole_no.issubset(even_no)) #false,because it is super set.
print(whole_no.issuperset(even_no)) #True

python={'p','y','t','h','o','n'}
dragon={'d','r','a','g','o','n'}
print(python.issubset(dragon))

even_no={0,2,4,6,8}
odd_no={1,3,5,7,9}
print(even_no.isdisjoint(odd_no)) #True ,because no common items.

python={'p','y','t','h','o','n'}
dragon={'d','r','a','g','o','n'}
print(python.isdisjoint(dragon)) #false, because there are commen item{'o','n'}

a={1,2}
b={1,2,3,4}
c={5,6}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(c))

