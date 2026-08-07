'''A datatype tells python what kind of value a variable is storing.
- datatype = type/category of data stored in a variable.'''

name ="rahul"
age = 39
price=49.9
is_active=True

#Numbers:- Numbers are used to store numeric value .it is three types :- int,float,complex.

# int :-int means integer.integer are whole numbers .they do not have decimal point.

age = 34
marks=78
temperature=-4
zero_value=0

# float:- float means floating-point number.float values contain decimal point.

price=88.50
height=5.8
temperature=-2.4
percentage=78.54

# Complex:- Complex numbers are numbers with two parts : Real part + Imaginary part.

'''In maths, complex numbers are usually written like this:- 3+4i, but in python ,we use j instead of i mean Python mein complex number ke liye i nahi, j use hota hai.
'''
number=3+2j
print(number)
print(type(number))

# a = 2+6i :- error output dega
# you can access real and imaginary part like this:- 
a=2+6j
print (a.real) #2.0
print(a.imag) #6.0


# Boolean :- Boolean is a datatypes that has only two possible values. that is True and False.
is_active=True 
is_deleted=False
print(is_active)
print(is_deleted)
print(type(is_active))

# True:-true represents yes,correct,active,available,or enabled.
# True must start with capital T.
# python will not understand true because python uses True.

# Also same as False:-

#None type :- none  means no values or empty value.

'''- It is used when a variable exists,but it does not currently store any actual value.
-None is not 0.None is not an empty string.
-None is not false .None means no value.'''

result=None
print(result)
print(type(result))

# Mutable  and Immutable datatype in python:-

# Mutable :- it is can be changed after creation .Some mutable datatypes in python are :-List , dictionary,Set.

# Immutable:-Immutable datatypes cannot be changed directly after they are created.

age =39
age=21
print (age) #21

'''Type = mutable/immutable
  int = immutable
  float = immutable
  str  = immutable
  bool = immutable
  complex = immutable
  Nonetype = immutable
  List    = mutable
  dict = mutable
  set = mutable    '''


# Last dattypes is String that is another files:-