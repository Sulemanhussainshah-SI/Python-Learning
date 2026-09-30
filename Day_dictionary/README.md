# ⭐ DICTIONARY :- ➡️
A dictionary is a data structure used to stored data, collection of unordered ,modifiable(mutable) paired (key:value) datatype.
- A dictionary store data using keys and values.
- Each key is connected to one value.
- keys are used to access values.
- Dictionary are mutable, so value can be changed.
- Dictionary keys must be unique .
- Dictionary are written using curly bracess { } .

#### Creating a dictionary:-
To create a dictionary we use curly bracket <kbd>{ }</kbd> or the <kbd>dict()</kbd> built-in function.
- Keys & values are seperated using a colon <kbd>:</kbd> .
- Each  pair is seperated using a comma <kbd>,</kbd>.
- The dictionary that a value could be any datatype :- string, boolean, list, tuple, set, or a dictionary.
```py
# Syntax:-
empty_dict={}

# dictinoary with data values
dict={'key1':'value1','key2':'value2','key3':'value3'}
```
###### Ex:-
```py
dict={
  'first_name':'Aman',
  'second_name':'kumar',
  'age':20,
  'country':'india',
  'skill':['js','hhtml','node','python'],
  'address':{
      'street':'mumbai',
      'zipcode':2453
    }
}
```
### Dictionary Properties Tables:-
| Property               |  Meaning              |    Ex:-           |
|------------------------|-----------------------|-------------------|
| Key value based        | Store data as pairs   | "name":"Aman"     |
| Mutable                | Can be changed        | student['age']=22 |
| Ordered                | keeps insertion order | python 3.7+       |
| Unique keys            | duplicate key are not allowed | last value replace old value |
| Fast lookup            | value are accessed using keys | student['name'] |
| Mixed value allowed    | values can be any datatype    | string,int,list,tuple,dict |

### Dictionary key & values:-➡️
- A key is used to identify a value.
- A value is the data stored against the key.
- Keys must be unique.
- Keys should be immutable type like string,numbers,or tuple.

###### Ex:-
```py
student={
  'name':'Aman',
  'age':20'
  'couurse':'Python'
}
print(student['name'])
```
### Key Rule Table:-
| Rule      | Allowed    | Ex:-       |
|-----------|------------|------------|
| String key| Yes        | 'name':'Aman'|
| Number key| Yes        | 1:'one'    |
| Tuple key | Yes        | (10,20):'point'|
| List key  | No         | [10,20]:'value'|
| Duplicate key | Not useful | Last value is kept |

#### Duplicate key :-➡️
###### Ex:-
```py
student={
    'name':'Aman',
    'name':'Suleman'
}
print(student)
```
###### Output:-
> [!NOTE]
> {'name':'Suleman' } :-  
> The second value replace the first value because dictionary key must be unique.

#### Dictionary length:-➡️
-  It checks the numbers of 'keys:value' are in the dictionary.
```py
Syntax:-
dict={
  'key1':'value1',
  'key2':'value2',
  'key3':'value3'
}
print(len(dict))
```
###### Ex:-
```py
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
```
### Different way to create dictionary:-
| Type      | Ex:- |
|-----------|------|
| Empty     | data={} |
| Normal    | student={'key1':'value1'} |
| Using dict()    | student={'name':'Aman','age':20} |
| Nested  | student={'s1':{'name':'Aman','age':20}} |
| dictionary with list value | data={'marks':[20,48,10]} |
|dictionary with tuple value | points={(10,30):'A'} |

### Accessing dictionary items:-➡️
- dictionary values are accessed using its key-name, inside square bracket.
- Unlike lists & tuples, dictionaries are not accessed mainly by index.
- if the key exists , Python returns the value.
- if the key does not exist,python gives keyError.
```py
# Syntax:-
dict_name=['key_name']
```

###### Ex:-
```py
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
print(student3['city']) # output:- # KeyError: 'city' :- because the key is not present in the dictionary.
```
###### Get() method:-
- <kbd>get()</kbd> avoids keyError.
- get() is used to access dictionary values safely.
- if the key exists,it returns the value .
- if the key does not exist,if returns None by default.
- we can also provide our own default value.
    
  ```py
  Syntax:-
  dict_name.get(key)
  dict_name.get('key','default_value')     
  ```
###### Ex:-
```py
student4={
  'name':'Aman',
  'age':20,
  'course':'Python'
}
print(student.get('name')) #'Aman'
print(student4.get('marks')) #None
print(student4.get('marks','not Available')) #not available
```
#### [ ] Vs get( ) Table:-
| Access method    | if key Exists   | if key Missing    |
|------------------|-----------------|-------------------|
| student['name']  | Return value    | gives keyError    |
| student.get('name') | Return value | Return None       |
| student.get('marks',0) | Return value | Return default value |


### Update/Modifying dictionary items:-➡️
- dictionary are mutable.
- Existing values can be updated using keys.
- if the key already exist,it's  value is updated.
- if the key does not exist,a new key-value pair is added.
```py
Syntax:-
dict={'key1':'value1','key2':'value2','key3':'value3'}
dict['key4']='value4'
```
###### Ex:-
```py
person3={
  'first_name':'suleman',
  'last_name':'hussain',
  'age':20,
  'country':'findland'
}
person3['last_name']='Shah'
person3['age']=21
print(person3)
```

### Checking key Membership in a dictionary items:-➡️
- In checks whether a key exists in the dictionary.
- it checks keys ,not values
- it returns True or False.
```py
Syntax:-
  dict={
           'key1':'value1',
           'key2':'value2',
           'key3':'value3'
      }
 print('key1' in dict )
print('key1' not in dict )
```
  
###### Ex:-
```py
dict={
           'key1':'value1',
           'key2':'value2',
           'key3':'value3'
      }
print('key1' in dict ) #True
print('key1' not in dict ) #false
```

### Removing dictionary items:-➡️
- <kbd>pop(key)</kbd> removes a specific key & return its value.
- <kbd>popitem()</kbd> removes the last inserted key value pair.
- <kbd>del</kbd> removes a specific key.
- <kbd>clear()</kbd> removes all items.
```py  
Syntax:-
      dict={
           'key1':'value1',
           'key2':'value2',
           'key3':'value3'
      }
      dict.pop('key1') #removes key1 items
      dict.popitem() #removes the last items
      dict.clear() # None
      del dict['key1']
```
###### Example:-
```py
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
print(person4('age')) # Type error
person4.popitem()
print(person4) # removes last item 'address'.
del person4['country']
print(person4)
person4.clear()
print(person4) # removes all items.
del person4['country']
print(person4) # key error because the above the person4 is clear and upper the clear than it working.
del person4
print(person4) # Name Error person4 is not defined.
```

### Merging two dictionaries:-➡️
- Merging means combining two or more dictionaries.
###### Ex:- Using <kbd>update()</kbd> method:-
```py
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
```
###### Ex:- Using <kbd>|</kbd>
```py
result=student|Extra
print(result)
```
###### In the same key during Merge:-
- if the both dictionaries have the same key,the second dictionary value wins.
###### Ex:-
```py
a={'name':'Aman','age':21}
b={'age':22,'course':'Python'}

result2=a|b
print(result2) #{'name':'Aman','age':22,'course':'Python'}
```
### Copying dictionaries:-➡️
- <kbd>Copy()</kbd> creates a shallow copy of a dictionary.
- Direct Assignment does not create a new dictionary.
- Direct Assignment make  both variables point to the same dictionary.
```py
Syntax:-
          new_dict=old_dict.copy() 
```
###### Example of Direct Assignment:-
```py
student5={'name':'Rahul','age':21}
student6=student5

student6['age']=22
print(student5) #{'name':'Rahul','age':21}
print(student6) #{'name':'Rahul','age':21}
```
###### Example of Real Copy:-
```py
student7={'name':'Ravi','age':21}
student8=student7.copy()

student8['age']=24
print(student7) #{'name':'Ravi','age':21}
print(student8) #{'name':'Ravi','age':24}
```
### Changing dictionary to a List of items:-➡️
- The <kbd>item()</kbd> method changes dictionary to a list of tuples.
##### Ex:-
```py
dict6={
   'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    "key4":"value4"
}
print(dict6.items()) #dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```
### Getting dictionary values as a list:- ➡️
- The <kbd>values()</kbd> method gives us all the value of a dictionary as a list.
###### Ex:-
```py
dict8={
  'key1':'value1',
      'key2':'value2',
      'key3':'value3',
      "key4":"value4"
} 
values=dict8.values()
print(values) #dict_values(['value1', 'value2', 'value3', 'value4'])
```

### Getting dictionary key as a list:-➡️
- The <kbd>keys()</kbd> method gives us all the keys of a dictionary as a list.
###### Ex:-
```py
dict9={
  'key1':'value1',
      'key2':'value2',
      'key3':'value3',
      "key4":"value4"
} 
keys=dict9.keys()
print(keys) #dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Nested dictionary:-➡️
- A nested dictionary means a dictionary inside another dictionary.
- It is useful for storing structured data.
- To access inner values, use multiple keys.
###### Ex:-
```py
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
```

##### updated nested:-
###### Ex:-
```py
class3={
  'student1':{
   'name':'ravi',
   'age':12
  }
}
class3['student1']['age']=13
print(class3) # {'student1': {'name': 'ravi', 'age': 13}}
```



 


