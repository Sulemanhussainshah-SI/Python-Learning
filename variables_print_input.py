""" Indentation Rule in python:-That means line ke shuru main thodi khali jagah (space) dena.
    - python is khaali jagah se samajhta hai ki kaun se code kis block ke ander hai.
    - :(colon) ka matlab - Jab bhi python mein : aata hai, uske baad indentation (4 space)deni hoti  hai.
    -In python, indentation is the block .other language use {} like C,C++,Java etc,but pthon use 4 space to show which statements belong together.
    """
# example 1  if age >=18: —> Ab jo code mere ander hoga , usko 4 space se likho.
age = 18
if age >= 18:
  print("you can vote") #if ke ander
  print("welcome")      #if ke ander
print("program End")  #if ke bahar 

'''example2:
age =18
if age>=18:
print("you can not vote") #indentation error :ecpected an indentation block '''

# Variables:- A variables is a name used to store data.
name ="Rahul"
age=20
height=5.8

# Python variables do not need type declaration.
x=10
print(x)
x="Python"
print(x) #in 24 line ,x store an integer,later x store a string. this is allowed because python  is dynamically typed.

# Multiple variable Assigement:-
a,b,c =10,20,30
print(a)
print(b)
print(c)

# Same value to multiple variables :-
x=y=z=100
print(x)
print(y)
print(z)

# Print statements:- The print() function is used to display on the screen.

# Basic print:-
print("hellow ishma")

#printing numbers:-
print(100)
print(23.5)

# print variables:-
name ="Ishma"
age= 16
print(name)
print(age)

#printing Text with variables :-
name= "suleman"
age = 20
print("Name :",name)
print("Age:",age)

#printing multiple values:-
a=10
b=49
print("A:",a,"B:",b)

#printing using f-string:-
name="Ishma"
age =16
print(f"My name  is {name} and I am {age} years old.")

product="Laptop"
price=55000
print(f"The price of {product} is ₹{price}.")

#printing with separator:-the sep parameter controls how multiple values are separated.
print("python","java", "suleman") #it is defaults saparator is a space.

print("suleman","ishma", sep="|")

# print with end parameters:- by defaults ,print() moves to a new line after printing.
print("hello")
print("suleman")

print("hellow",end=" ")
print("Ishma")

print("A",end="-")
print("B",end="-")
print("C")
  




