# ➡️ Indentation Rule in python:-✅
That means line ke shuru main thodi khali jagah (space) dena.  
- python is khaali jagah se samajhta hai ki kaun se code kis block ke ander hai.
- :(colon) ka matlab - Jab bhi python mein : aata hai, uske baad indentation (4 space)deni hoti  hai.  
- In python, indentation is the block .other language use {} like C,C++,Java etc,but pthon use 4 space to show which statements belong together.
    
###### example 1:-
```py
if age >=18: —> Ab jo code mere ander hoga , usko 4 space se likho.

age = 18
if age >= 18:
  print("you can vote") #if ke ander
  print("welcome")      #if ke ander
print("program End")  #if ke bahar
``` 

###### example2:-
```py
age =18
if age>=18:
print("you can not vote") #indentation error :ecpected an indentation block
```

#### Variables:- 
A variables is a name used to store data.
```py
name ="Rahul"
age=20
height=5.8
```

##### Python variables do not need type declaration.
###### Ex:-
```py
x=10
print(x)
x="Python"
print(x) #in 24 line ,x store an integer,later x store a string. this is allowed because python  is dynamically typed.
```

#### Multiple variable Assigement:-
```py
a,b,c =10,20,30
print(a)
print(b)
print(c)
```

##### Same value to multiple variables :-
```py
x=y=z=100
print(x)
print(y)
print(z)
```

##### Print statements:- The <kbd>print()</kbd> function is used to display on the screen.

###### Basic print:-
```py
print("hellow ishma")
```

##### printing numbers:-
```py
print(100)
print(23.5)
```

##### print variables:-
```py
name ="Ishma"
age= 16
print(name)
print(age)
```

###### printing Text with variables :-
```py
name= "suleman"
age = 20
print("Name :",name)
print("Age:",age)
```

##### printing multiple values:-
```py
a=10
b=49
print("A:",a,"B:",b)
```

#### printing using f-string:-
```py
name="Ishma"
age =16
print(f"My name  is {name} and I am {age} years old.")
```
```py
product="Laptop"
price=55000
print(f"The price of {product} is ₹{price}.")
```

##### printing with separator:-
- The sep parameter controls how multiple values are separated.
```py
print("python","java", "suleman") #it is defaults saparator is a space.
```
```py
print("suleman","ishma", sep="|")
```

##### print with end parameters:-
- By defaults ,print() moves to a new line after printing.
```py
print("hello")
print("suleman")

print("hellow",end=" ")
print("Ishma")

print("A",end="-")
print("B",end="-")
print("C")
```
  
### ✅ Input from User:- ➡️
- The <kbd>input()</kbd> function is used to take input from the user.
###### Ex:-
```py
name = input("enter your Name: ")
print("hellow",name)
```
> [!IMPORTANT]
> the input() function always returns data as a string.
> ```py
> age = input("enter youur age:")
> print(age)
> print(type(age)) #Even though the user entered 21,python stores it as "21".

##### Taking integer input:- 
- To convert input into an integer,user <kbd>int()</kbd>.
###### Ex:-
```py
age = int(input("enter your age:"))
print("your age is :",age)
print(type(age))
``` 

###### Taking float input:- 
- To convert input into decimal number ,use <kbd>float()</kbd>.
###### Ex:-
```py
price=float(input("enter your money in float:"))
print("price is :",price)
print(type(price))
```

###### Example:-
```py
num1=int(input("enter first numbers:")) #20
num2=int(input("enter second numbers:")) #21

result=num1+num2

print("sum is :",result) # output sum is :41
```
> [!NOTE]
> WHAT happens without int():-
> ```py
> num1=input("enter first numbers:") # 10
> num2=input("enter second numbers:") #15
> result= num1+num2
> print("sum :",result) #output sum:1015
```
