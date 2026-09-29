# Creating a dictionary :-
""" - To create a dictionary we use curly bracket {} or the dict() built-in function.
    - Keys and values are seperated using a colon : .
    - Each pair is seperated using a comma , .
        """
# Syntax:-
empty_dict={}
# dictionary with data values
dict={
  'key1':'value1',
  'key2':'value2',
  'key3':'value3',
  "key4":"value4"
}
# Ex:-
person= {
  'first_name':'suleman',
  'second_name':'hussain shah',
  'age':20,
  'country':'india',
  'is_marred':False,
  'skills':['javascript','html','node','mongoDB','python'],
  'address':{
    "street":"jala",
    'pincode':827010
        }
}
print(person)

# Dictionary keys & values:-
''' - A key is used to identify a value.
    - A value is the data stored against the key.
    - keys must be unique.
    - keys should be immutable type like string , number , or tuple.
    '''
# Ex:-
student={
  'name':'Aman',
  "age":20,
  "course":'python'
}
print(student)

# Duplicate keys:-
student2={
  'name':'Aman',
  'name':'suleman' # output 'suleman' :-the second value replace the first value because dictionary key must be unique.
}
print(student2)

# Dictionary length:-
'''- it checks the numbers of 'keys:value' are in the dictionary.'''
#Syntax:-
dict={
  'key1':'value1',
  'key2':'value2',
  'key3':'value3'
}
print(len(dict))
# Ex:-
person2={
  'first_name':'suleman',
  'last_name':'hussain shah',
  "age":20,
  'country':'India',
  "address":{
    'vill':'jala',
    "pin": 827010
  }
}
print(person2)

# Accessing dictionary items:-

# Syntax:-
dict_name=['key_name']

# Ex:-
student3={
  'name':'Aman',
  'age':20,
  'course':'python',
  'country':'Finland',
  'is_marrid':False,
  'skills':['javascript','C','c++','html','node','mongoDB','python'],
  'address':{
    'street':'space street',
    'pincode':'827010'
  }
}
print(student3['name']) # output:- Aman
print(student3['age']) # output:- 20
print(student3['course']) # output:- python
print(student3['country']) # output:- Finland
print(student3['is_marrid']) # output:- False
print(student3['skills']) # output:- ['javascript', 'C', 'c++', 'html', 'node', 'mongoDB', 'python']
print(student3['address']) # output:- {'street': 'space street', 'pincode': '827010'}
print(student3['address']['street']) # output:- space street
print(student3['address']['pincode']) # output:- 827010
print(student3['skills'][0]) # output:- javascript
print(student3['skills'][3]) # output:- html
print(student3['skills'][-2]) # output:- mongoDB
# print(student3['city']) # output:- # KeyError: 'city' :- because the key is not present in the dictionary.

# Get() method:-
"""
    - get() avoids keyError.
    - get() is used to access dictionary values safely.
    - if the key exists,it returns the value .
    - if the key does not exist,if returns None by default.
    - we can also provide our own default value.
    
        Syntax:-
        dict_name.get(key)
        dict_name.get('key','default_value')     
  """
# Ex:-
student4={
  'name':'Aman',
  'age':20,
  'course':'Python'
}
print(student.get('name')) #'Aman'
print(student4.get('marks')) #None
print(student4.get('marks','not Available')) #not available


# Update/Modifying dictionary items:-
"""- dictionary are mutable.
   - Existing values can be updated using keys.
   - if the key already exist,it's  value is updated.
   - if the key does not exist,a new key-value pair is added.
      Syntax:-
         dict={'key1':'value1','key2':'value2','key3':'value3'}
         dict['key4']='value4'
         """
# Ex:-
person3={
  'first_name':'suleman',
  'last_name':'hussain',
  'age':20,
  'country':'findland'
}
person3['last_name']='Shah'
person3['age']=21
print(person3)

# Checking key Membership in a dictionary items:-
"""- In checks whether a key exists in the dictionary.
   - it checks keys ,not values
   - it returns True or False.
   Syntax:-
      dict={
           'key1':'value1',
           'key2':'value2',
           'key3':'value3'
      }
      print('key1' in dict )
      print('key1' not in dict )
   """

#Ex:-
dict={
           'key1':'value1',
           'key2':'value2',
           'key3':'value3'
      }
print('key1' in dict ) #True
print('key1' not in dict ) #false

# Removing dictionary items:-
""" - pop(key) removes a specific key & return its value.
    - popitem() removes the last inserted key value pair.
    - del removes a specific key.
    - clear() removes all items.
    
    Syntax:-
      dict={
           'key1':'value1',
           'key2':'value2',
           'key3':'value3'
      }
      dict.pop('key1') #removes key1 items
      dict.popitem() #removes the last items
      dict.clear() # None
      del dict['key1'] """
# Example:-
person4={
  'first_name':'suleman',
  'last_name':'hussain',
  'age':20,
  'country':'India',
  'skills':['javascript','node','c','c++','python'],
  'address':{
     'street':'bokaro',
     'zipcode':'2344'
  }
}
person4.pop('age')
print(person4) # removes age items.
# print(person4('age')) # Type error
person4.popitem()
print(person4) # removes last item 'address'.
del person4['country']
print(person4)
person4.clear()
print(person4) # removes all items.
# del person4['country']
# print(person4) # key error because the above the person4 is clear and upper the clear than it working.
del person4
# print(person4) # Name Error person4 is not defined.

#Merging two dictionaries:-
"""- Merging means combining two or more dictionaries."""
# Ex:- Using update() method:-
student={
  'name':'Aman',
  'age':21
}
Extra={
  'course':'Python',
  'city':'Delhi'
}
student.update(Extra) 
print(student)
# Ex:- Using |
result=student|Extra
print(result)
"""In the same key during Merge:-"""
'''if the both dictionaries have the same key,the second dictionary value wins.'''
# Ex:-
a={'name':'Aman','age':21}
b={'age':22,'course':'Python'}

result2=a|b
print(result2) #age 22

# Copying dictionaries:-
"""- Copy() creates a shallow copy of a dictionary.
   - Direct Assignment does not create a new dictionary.
   - Direct Assignment make  both variables point to the same dictionary.
       Syntax:-
          new_dict=old_dict.copy() 
"""
# Example of Direct Assignment:-
student5={'name':'Rahul','age':21}
student6=student5

student6['age']=22
print(student5) #{'name':'Rahul','age':21}
print(student6) #{'name':'Rahul','age':21}

# Example of Real Copy:-
student7={'name':'Ravi','age':21}
student8=student7.copy()

student8['age']=24
print(student7) #{'name':'Ravi','age':21}
print(student8) #{'name':'Ravi','age':24}

# Changing dictionary to a List of items:- The item() method changes dictionary to a list of tuples.
dict6={
   'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    "key4":"value4"
}
print(dict6.items()) #dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Getting dictionary values as a list:- The values() method gives us all the value of a dictionary as a list.
dict8={
  'key1':'value1',
      'key2':'value2',
      'key3':'value3',
      "key4":"value4"
} 
values=dict8.values()
print(values) #dict_values(['value1', 'value2', 'value3', 'value4'])

# Getting dictionary key as a list:- The keys() method gives us all the keys of a dictionary as a list.

dict9={
  'key1':'value1',
      'key2':'value2',
      'key3':'value3',
      "key4":"value4"
} 
keys=dict9.keys()
print(keys) #dict_keys(['key1', 'key2', 'key3', 'key4'])

# Nested dictionary:-

class9={
  'student1':{
    'name':'Aman',
    'age':21
  },
  'student2':{
     'name':'riya',
     'age':20
  }
}
print(class9['student1']['age']) #21
print(class9['student2']['name']) #riya

#updated nested:-
class3={
  'student1':{
   'name':'ravi',
   'age':12
  }
}
class3['student1']['age']=13
print(class3) # {'student1': {'name': 'ravi', 'age': 13}}

