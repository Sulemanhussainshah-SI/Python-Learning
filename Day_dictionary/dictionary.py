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