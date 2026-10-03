# If condition/statement:-
"""- The if statements is used when we want to run some code only when a condition is True.
   - if the condition is True , Python executes the indented block. 
   -If the condition is False , Python skips the indented block.
     Syntax:-
       if condition:
         statement code."""
#Ex:-
age=20
if age>=20:
  print("Eligible to vote")

a=30
if a>0:
  print("A is positive numbers")

age=16
if age>=18:
  print("Apply the voter card")
print("fill the form")  

# If-else
"""- The if else statement is used when we want to run one block  if    the condition is True & another block if the condition is False.
- only one block runs.
    - If the condition is True , the if block runs. 
    - If the condition is False , the else block runs.
        Syntax:-
            if condition:
                statement
            else:
                 statement       """

age=20
if age>=18:
  print("eligible to vote")
else:
  print("Not eligible to vote")


a=6
if a<0:
  print("A is negative numbers")
else:
  print("A is a positive numbers")  

# elif statement:-
"""- elif means else if .
   - it is used when we need to check multiple conditions.
   - Python checks conditions from Top to buttom.the first condition that becomes true getsexecuted after that ,Python skips remaining conditions.
  - the else block runs only when all perivious conditions are false.
          Syntax:-
             if condition1:
               statement1
             elif condition2:
                  statement2
             elif condition3:
                   statement3
            else:
              default statement  """
marks=78
if marks>=90:
  print("Grade A")
elif marks>=75:
  print("Grade B")  
elif marks>=45:  
  print("Grade C")  
else:
  print("You are fail")

# Nested conditionals:-
"""- Nested  condition means writing one conditional statement inside another conditional statement.
    - The inner conditional statement is checks only when the outer conditional statement is True.
    this is useful when one decision depends on another decision.
        Syntax:-
            if condition1:
                if condition2:
                    statement
                else:
                    statement
            else:
                statement  """  
#Ex:-
a=20
if a>0:
  if a%2==0:
    print("A is positive even number")
  else:
    print("A is positive odd number")
elif a==0:
  print("A is zero")
else:
  print("A is negative number")

age=45
has_id=True
if age>=18:
  if has_id:
    print("Entry allowed")
  else:
    print("ID is required")
else:
  print("Entry not allowed")  

#Ternary operator:-
""" Syntax:-
   value_if_true if condition else value_if_false"""
#common usage:-
# variable=value_if_true if condition else value_if_false
age=20
status="Adult" if age>=18 else "Minor"
print(status)

#Match-case statement:-
"""- match_case is used to compare one value with multiple cases.
   - it is similar to checking many fixed options.
   - The - case works like a default case.
   - It runs when no other case matches.
   - Match-case was introduced in Python 3.10.
     Syntax:-
     match value:
        case value1:
            statement1
        case value2:
            statement2
        case value3:
            statement3
        case _:
            default statement            
"""
command="start"
match command:
    case "start":
        print("Starting the application")
    case "stop":
        print("Stopping the application")
    case "restart":
        print("Restarting the application")
    case _:
        print("Invalid command")

day=3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")        

# if conditions AND logical operators:-
""" Syntax:
   if condition and condition:
       statement""" 
#Ex:-
a=0
if a>0 and a%2==0:
  print("A is positive even number")  
elif a>0 and a%2!=0:
  print("A is positive odd number")
elif a==0:
  print("A is zero")  
else:
  print("A is negative number")

#if conditions OR logical operators:-
""" Syntax:
   if condition or condition:
       statement""" 
#Ex:-
user="james"
access_level=3
if user=="james" or access_level>=5:
  print("Access granted")               