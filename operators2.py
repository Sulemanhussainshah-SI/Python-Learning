# Arrithematic operators

a = 10
b = 4

print(a+b) # add
print(a-b) #subtract
print(a*b) #multiply
print(a/b) #division
print(a**b) #exponent
print(a//b) #floor division
print(a%b) #remainder

# Comparision Operator :- always return value in boolean 

x = 5
y = 7
 
print(x==y) # false 
print(x!=y) #true
print(x<y)  #true
print(x>y)  #false
print(x<=y) #true
print(x>=y) #false

#Assignment operator : used for jab kisi variable ko value assign karna ho ya value dena ho

i = 5 #assign 5
print(i)

i +=5 # i = i+5=5+5=10
print(i)

i -= 5 #i = i-5=10-5=5 ya per upper wala i ka output 10 tha isilya i = 10 then subtract (10-5)=5
print(i)

""" same isi terha ya sab ka v hoga like *=,/=,%=,//=,**="""

# LOGICAL Operator :-used for combine condition

"""And :-true if both condition are true
OR:-true if at least one condition is true
NOT:- reveses the result"""

p = 10 
q = 5

print (p>5 and q<10) #true
print (p<5 or q<10)# true
print (not (p>5)) #false

# MEMBERSHIP OPERATORS:- check wheather a value exists in a sequence.

"""in:- 'a' in "apple"
  not in:- 'x' not in "apple" """

fruits=["apple", "banana", "mango"]

print("apple" in fruits)
print("orange" not in fruits)


# Identity Operators:- check wheather two variables refers to the same object

""" ==:- value same ? content compare :-value dekho 
   is :- same object? same memory/object :- object( memory reference dekho)
  is not :- different object? alag memory/object :- check karo ki object alag hai ya nahi """

a="apple"
b="apple"

print (a==b) #true

# sirf value dekho

p=[1,8]
q=p

print(p is q)

w=[1,8]
r=[1,8]

print(w==r)
print(w is r)

t=[1,0]
y=[1,0]

print (t is not y ) #q ki dono alag object hain





