# ⭐ String:- ➡️
A strings is a sequences of character .
  - Character can be : Letter , Numbers,Symbols , Spaces.  

```py
name="suleman"
city ="delhi"
message="hellow python"
phone="79678678654"
```

- Even though the phone contain numbers it inside quotes,so it is a string.
```pyphone = "689960990"
print(type(phone)) #<class 'str'>
```

## String Creation:-➡️ 
String can be created using quotes.

##### Using single qutes:-
```py
name1='aman'
print(name1)
```

##### Using double qutes:-
```py
name2="Aman"
print(name2)
```
###### Example:-
```py
a="Aman"
b='rahul'
print(a) #Aman
print(b) #rahul
print(type(a)) #<class 'str'>
print(type(b)) #<class 'str'>
```

##### Both are Correct.

##### Using Triple double qutes:- triple qutes are used for multi-line strings.
###### Ex:-
```py
message="""python is simple
           python is powerful
           python is beginner friendly."""
print(message)
```
##### You can also use triple single qutes :-
###### Ex:-
```py
   message= '''hellow
             wellcom to python.'''
print(message)
# output same aaya ga.
```

## Empty String :- ➡️ 
A strings can also be empty.
###### Ex:-
 ```py
a= " "
print(a) # That is no visible text in the first output because the string is empty.
print(type(a),"\n")
```

## Sting  Indexing:-➡️ 
Index means accessing a single character from a string.  
- Every character in a string has a position number.
- This position number is called an index.
- Python indexing start from 0.
```py
index diagram:-
     string: p  y  t  h  o  n
     index:  0  1  2  3  4  5
  
  ```
###### Ex:-
```py
word= "python"
print(word[0]) #p
print(word[1]) #y
print(word[2]) #t
print(word[3]) #h
print(word[4]) #o
print(word[5]) #n
```

#### Positive indexing:-
Positive index starts from the Last side.  
```py
      S  u  l  e  m  a  n
      0  1  2  3  4  5  6
```
###### Ex:-
```py
name = "suleman"
print(name[3]) 
print(name[0]) 
print(name[4])
```

#### Negative indexing:-
Negative indexing starts from the Right side.
```py
    string: s   u   l   e   m   a   n
  pos ind : 0   1   2   3   4   5   6
  neg ind :-7  -6  -5  -4  -3  -2  -1
```
##### Ex:-
```py
name3= "suleman"
print(name3[-1])
print(name3[-4])
print(name3[-2])
print(name3[-7])
```

#### Index Error:-
if you try to access an index that does not exist, python gives an error.
###### Ex:-
```py
word3="hellow"
print(word3[7]) #index error : string index out of range.
```
- python has indexs from 0 to 5 only ,index 7 does not exist.
  
## String Slicing:-➡️
Slicing means taking part of a string.
```py
Syntax:-

string_name[start:end]
words1="python"
print(words1[0:2])
```

###### Explanation:- 
```markdown
words1[0:2] means -> start from  index 0 and stop before index 2.  
       string: p y t h o n  
       index:  0 1 2 3 4 5  
  woords1[0:2]:- gives character from index 0 to before 2.  
  results: py
```
  
###### Ex:-
```py
words2="suleman"
print(words2[0:6])
print(words2[0:3])
print(words2[2:5])
print(words2[1:4])
```

#### Leaving start empty:-  
if start is empty python start from begining.
###### Ex:-
```py
words3="python"
print(words3[:3])
print(words3[:2])
print(words3[:5],"\n") #start from begining stop before indexes.
```

#### Leaving End empty:-  
if end is empty ,python goes till end
###### Ex:-
```py
words4="python"
print(words4[2:])
print(words4[4:])
print(words4[1:],"\n") #start from index and go till end.
```

#### Full slice:-
###### Ex:-
```py
words5="suleman"
print(words5[:],"\n") #This returns the full string.
```

#### slicing with negstive index:- 
##### Ex:-
```py
words6="python"
print(words6[-3:])
print(words6[-1:],"\n")
```

###### Explanation:-
```markdown
   string:  p  y  t  h  o  n
negi ind : -6 -5 -4 -3 -2 -1
 words6[-3:] means start from -3 and go till end 
 result: hon
```

#### Slicing with step:-
```py
Syntax:-
    string_name[start:end:step]
```
###### Ex:-
```py
words7="python"
print(words7[0:3:1])
print(words7[3:5:2])
print(words7[2:4:2],"\n")
```
###### Explanation:-
```markdown
start at index 0,3,2, go before index -> 3,5,4 and pick every -> 1,2,2 characters.
```
#### Reverse string using slicing:-
```py
words8="python"
print(words8[::-1])
```
###### Explanation:-
```
markdown
[::-1] -> means read the string fron right to left
```
#### String Immutability:-➡️ String in Python are immutable.
- means once created ,it cannot be change directly.
```py
c1="ravi"
print(c1)
```
Suppose we want to change r to k.this will not work
  string: r a v i
  index:  0 1 2 3
  
 ```py
 c1="ravi" 
  c1[o]="k" :- output type error,why because string cannot be changed character by character.
```
 - correct way :- you can create a new string and store it again.
```py
     c2="ravi"
     c3="kavi"
         print(c3) #output kavi
```
> [!IMPORTANT]   
> old string =ravi  
> new string = kavi ,python does not modify the old string ,it create a new string.
 

## String Formatting:-➡️
String formatting means placing values inside a string in a clean way.
- This is better then manually joining many values.
- Python has three main ways to format string:
     - f-string
     - format()
     - old % formatting.

#### F-string:- 
- f-string are the most readable and modern way.  
- write f before the string & place variables inside {}.
###### Ex:-
```py
stud="suleman"
age=12
print(f"My name is {stud}","\n",f"and I am {age} years old.")
```
```py
stud1="Aman"
age = 34
print(f"My name is {stud1} and i am {age} years old.")
```
```py
a=34
b=76
print(f"sum is : {a+b}")
```

#### Format():-
- The <kbd>format()</kbd> method inserts values into place holders.
###### Ex:-
```py
stud2="Abhi"
age=23
print("my name is {} & i am {} years old.".format(stud2,age))
```

#### Old % formatting:-
- this is old style of formatting.
###### Ex:-
```py
stude1="rahul"
age =34
print("my name is %s and i am %d years ."%(stude1,age)) #%s is used for string ,%d is used for  integer.
```


## String Concatenation:-➡️
Contatenation means joining string together.
   - the + operator is used for 
   - only string can be joined directly.
###### Ex:-
```py
first="python"
second="programming"
print(first +" "+ second)
```

## Raw string:-➡️
Means string treat backslashs as normal charactors.
- write r before string.
###### Ex:-
```py
path=r"c:\new_folder\test"
```

## String multiplication:-➡️
A string can be repeated using the * operator.
```py
text="I love you "
print(text*2,"\n")
```

## String Methods:-➡️
String methods are built-in function that work on string .
- Common string methods are used for cleaning ,checking ,changing case ,finding text,  and replacing text.


#### <kbd>lower()</kbd>:- Convert string to lowercase.
###### Ex:-
```py
text2="PythOn"
print(text2.lower())
```

#### <kbd>Upper()</kbd>:- Convert strings to uppercase.
###### Ex:-
```py
text3="python"
print(text3.upper())
```
#### <kbd>swapcase()</kbd>:- means convert uppercase to lowercase and lowercase to uppercase.
###### Ex:-
```py
text7="Aman is good Boy"
print(text7.swapcase())
```

#### <kbd>title()</kbd>:- Capitalize the first character of each words in the strings.
###### Ex:-
```py
city1="this world is circle, it is facts."
print(city1.title())
```
#### <kbd>strip()</kbd>:-Removes extra spaces from the begining and end.
- it is two types 
   - <kbd>.lstrip()</kbd>:-  means removes spaces from left side.
   - <kbd>.rstrip()</kbd>:- means removes spaces from right side.
###### Ex:-
```py
text4="  python  "
print(text4.strip())

text5="  suleman"
print(text5.lstrip())

text6="python  " 
print(text6.rstrip())
```

#### <kbd>replace()</kbd>:- replace one part of a string with anothers.
###### Ex:-
```py
city3="i like java"
print(city3.replace("i","I"))
print(city3.replace("java","Java"))
```

#### <kbd>split()</kbd>:-splits a strings into a list of parts using a separator.
###### Ex:-
```py
text8="apple,banana,oranges,mango"
print(text8.split(","))
```

##### <kbd>find()</kbd>:- finds the positions of a substring.
###### Ex:-
```py
city9="python"
print(city9.find("t"))
print(city9.find("p"))
print(city9.find("n"))
```
#### <kbd>count()</kbd>:- counts how many times a character or substrings appears.
###### Ex:-
```py
city4="banana"
print(city4.count("a"))
```

#### <kbd>startswith()</kbd> & <kbd>endwith()</kbd>:-
###### Ex:-
```py
city5="suleman"
print(city5.startswith("su"))
print(city5.endswith("an"))
print(city5.startswith("anf"))
print(city5.endswith("sl"))
```
#### <kbd>len()</kbd>:-
###### Ex:-
```py
city6="suleman hussain shah"
print(len(city6))
a="python"
print(len(a))
```

#### <kbd>expandtabs()</kbd>:- Replaces tab character with spaces, default tab size is 8. It takes tab size argument
###### Ex:-
```py
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```
#### <kbd>index()</kbd>:- Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
###### Ex:-
```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error
```
#### <kbd>rindex()</kbd>:- Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
###### Ex:-
```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19
```

#### <kbd>isalnum()</kbd>:- Checks alphanumeric character
###### Ex:-
```py
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
```

#### <kbd>isalpha()</kbd>:- Checks if all string elements are alphabet characters (a-z and A-Z)
###### Ex:-
```py
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
```

#### <kbd>isdecimal()</kbd>:- Checks if all characters in a string are decimal (0-9)
###### Ex:-
```py
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True 
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
```

#### <kbd>isdigit()</kbd>:- Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
###### Ex:-
```py
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
```

#### <kbd>isnumeric()</kbd>:- Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
###### Ex:-
```py
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```
#### <kbd>isidentifier()</kbd>:- Checks for a valid identifier - it checks if a string is a valid variable name
###### Ex:-
```py
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
```
#### <kbd>islower()</kbd>:- Checks if all alphabet characters in the string are lowercase
###### Ex:-
```py
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```

#### <kbd>isupper()</kbd>:- Checks if all alphabet characters in the string are uppercase
###### Ex:-
```py
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```
