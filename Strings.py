'''A strings is a sequences of character .
  - Character can be : Letter , Numbers,Symbols , Spaces.  '''

name="suleman"
city ="delhi"
message="hellow python"
phone="79678678654"

#Even though the phone contain numbers it inside quotes,so it is a string.
phone = "689960990"
print(type(phone)) #<class 'str'>

# String Creation:- String can be created using quotes.

#Using single qutes:-
name1='aman'
print(name1)

#Using double qutes:-
name2="Aman"
print(name2)

#Example:-
a="Aman"
b='rahul'
print(a) #Aman
print(b) #rahul
print(type(a)) #<class 'str'>
print(type(b)) #<class 'str'>

# Both are Correct.

# Using Triple qutes:-triple qutes are used for multi-line strings.
message="""python is simple
           python is powerful
           python is beginner friendly."""
print(message)
"""You can also use triple single qutes :-
   message= '''hellow
             wellcom to python.'''
print(message)
output same aaya ga. """

# Empty String :-A strings can also be empty.
 
a= " "
print(a) # That is no visible text in the first output because the string is empty.
print(type(a),"\n")

# Sting  Indexing:- Index means accessing a single character from a string.
"""- Every character in a string has a position number.
   - This position number is called an index.
   - Python indexing start from 0.

   index diagram:-
     string: p y t h o n
     index:  0 1 2 3 4 5
  
  """
word= "python"
print(word[0]) #p
print(word[1]) #y
print(word[2]) #t
print(word[3]) #h
print(word[4]) #o
print(word[5]) #n

# Positive indexing:-Positive index starts from the Last side.
''' S u l e m a n
    0 1 2 3 4 5 6 '''
name = "suleman"
print(name[3]) 
print(name[0]) 
print(name[4])

# Negative indexing:-Negative indexing starts from the Right side.
''' string: s  u  l  e  m  a  n
  pos ind : 0  1  2  3  4  5  6
  neg ind :-7 -6 -5 -4 -3 -2 -1'''

name3= "suleman"
print(name3[-1])
print(name3[-4])
print(name3[-2])
print(name3[-7])

# Index Error:-if you try to access an index that does not exist, python gives an error.
"""word3="hellow"
print(word3[7]) #index error : string index out of range."""

#python has indexs from 0 to 4 only ,index 7 does not exist.
  
#String Slicing:-slicing means taking part of a string.
#  Syntax:-string_name[start:end]
words1="python"
print(words1[0:2])

'''explanation:-words1[0:2] means - start from  index 0 and stop before index 2.
    string: p y t h o n
    index:  0 1 2 3 4 5
  woords1[0:2]:-gives character from index 0 to before 2.
  results: py.'''
# ex:-
words2="suleman"
print(words2[0:6])
print(words2[0:3])
print(words2[2:5])
print(words2[1:4])

#Leaving start empty:-if start is empty python start from begining.
words3="python"
print(words3[:3])
print(words3[:2])
print(words3[:5],"\n") #start from begining stop before indexes.

#Leaving End empty:-if end is empty ,python goes till end
words4="python"
print(words4[2:])
print(words4[4:])
print(words4[1:],"\n") #start from index and go till end.

#Full slice:-
words5="suleman"
print(words5[:],"\n") #This returns the full string.

#slicing with negstive index:- 
words6="python"
print(words6[-3:])
print(words6[-1:],"\n") #explanation:-
'''string:  p  y  t  h  o  n
negi ind : -6 -5 -4 -3 -2 -1
 words6[-3:] means start from -3 and go till end 
 result: hon'''

#Slicing with step:-
#syntax:- string_name[start:end:step]
words7="python"
print(words7[0:3:1])
print(words7[3:5:2])
print(words7[2:4:2],"\n") #explanation:-
'''start at index 0,3,2,go before index 3,5,4 and pick every 1,2,2 characters.'''

# Reverse string using slicing:-
words8="python"
print(words8[::-1]) #explanation:-
'''[::-1] means read the string fron right to left.'''

#String Immutability:- means once created ,it cannot be change directly.
c1="ravi"
print(c1)
'''suppose we want to change r to k.this will not work
  string: r a v i
  index:  0 1 2 3
  
  c1="ravi" 
  c1[o]="k" :- output type error,why because string cannot be changed character by character.
   
  correct way :- you can create a new string and store it again.
       c2="ravi"
        c3="kavi"
         print(c3) output kavi  '''
"""important:- old string =ravi
              new string = kavi ,python does not modify the old string ,it create a new string.""" 

"""String Formatting:-string formatting means placing values inside a string in a clean way.
  -this is better then manually joining many values.
  -python has three main ways to format string:
     - f-string
     - format()
     - old % formatting."""

# F-string:- f-string are the most readable and modern way.write f before the string & place variables inside {}.
stud="suleman"
age=12
print(f"My name is {stud}","\n",f"and I am {age} years old.") 
stud1="Aman"
age = 34
print(f"My name is {stud1} and i am {age} years old.")
a=34
b=76
print(f"sum is : {a+b}")

#Format():-The format () method inserts values into place holders.
stud2="Abhi"
age=23
print("my name is {} & i am {} years old.".format(stud2,age))

# Old % formatting:-this is old style of formatting.
stude1="rahul"
age =34
print("my name is %s and i am %d years ."%(stude1,age)) #%s is used for string ,%d is used for  integer.


"""String Concatenation:- contatenation means joining string together.
   - the + operator is used for 
   - only string can be joined directly."""
first="python"
second="programming"
print(first +" "+ second)

'''Raw string:-means string treat backslashs as normal charactors.write r before string.
path=r"c:\new_folder\test" '''

#String multiplication:- A string can be repeated using the * operator.
text="I love you "
print(text*2,"\n")

"""String Methods:- string methods are built-in function that work on string .
  - common string methods are used for cleaning ,checking ,changing case ,finding text,  and replacing text."""

# lower():- convert string to lowercase.
text2="PythOn"
print(text2.lower())

#Upper():- Convert strings to uppercase.
text3="python"
print(text3.upper())

# Swapcase():- means convert uppercase to lowercase and lowercase to uppercase.
text7="Aman is good Boy"
print(text7.swapcase())

# Title():- Capitalize the first character of each words in the strings.
city1="this world is circle, it is facts."
print(city1.title())


''' Strip():-Removes extra spaces from the begining and end.it is two types 
      1.lstrip():-  means removes spaces from left side.
      2.rstrip():- means removes spaces from right side.'''
text4="  python  "
print(text4.strip())
text5="  suleman"
print(text5.lstrip())
text6="python  " 
print(text6.rstrip())

# Replace():- replace one part of a string with anothers.
city3="i like java"
print(city3.replace("i","I"))
print(city3.replace("java","Java"))

# Split():-splits a strings into a list of parts using a separator.
text8="apple,banana,oranges,mango"
print(text8.split(","))

# Find():- finds the positions of a substring.
city9="python"
print(city9.find("t"))
print(city9.find("p"))
print(city9.find("n"))

# Count():- counts how many times a character or substrings appears.
city4="banana"
print(city4.count("a"))

#Startswith() & endwith():-
city5="suleman"
print(city5.startswith("su"))
print(city5.endswith("an"))
print(city5.startswith("anf"))
print(city5.endswith("sl"))

city6="suleman hussain shah"
print(len(city6))
a="python"
print(len(a))


#Expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

#Index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error


#Rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19

#isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

#isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

#isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True 
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

#isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

#isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

#isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

#islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

#isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True