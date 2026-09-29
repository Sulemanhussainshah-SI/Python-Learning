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

### Dictionary key & values:-
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

#### Duplicate key :-
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

#### Dictionary length:-
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
#### Different way to create dictionary:-



