# type () function :- 
a="67"

print(a)
print(type(a)) #a is assign to string datatype value <class 'str'>
 
b = 38
print(type(b)) # b is assign to integer datatype value <class 'int'>

print(type(True)) #<class 'bool'>
print(type((1,2,3,4))) #<class'tuple'>
print(type({1,2,3})) #<class 'set'>
print(type({"a":1}))  #<class 'dist'>
print(type(None))    #<class 'Nonetype'>

"""Boolean datatype is actually integer datatype  of subclasses """
print(type(True)) #<class 'bool'>
print(type(True)==int) #false because bool is another class .
print(isinstance(True,int))  #true because bool ,int is inherit the bool.
'''Isiliye jab bhi inherintance matter kara ,type () ki jagah isinstance() use karo'''

"""isinstance() vs type()"""

x=5
print(type(x)==int) #true
print(isinstance(x,int)) #true fark tab aata hai jab inheritance involved ho.

class Animal:
  pass
class Dog(Animal):
  pass
d=Dog()
print(type(d)==Animal)  #false because type (d) is exact class return - Dog, not equal to Animal that is false
print(isinstance(d,Animal)) # true because isinstance (d,Animal) check d and animal is subclass - dog inherit the animal , that is true


# typecasting:- datatype convert to another datatype .

age="50" 
print (type(age))
print(int(age))




c ="20.7"
c = int (float(c)) # value error because it is a string that  convert first float and  then after that  int . it is called  typecasting 
print (c)
print(type(c))



