""" Lists :- A lists is a data structure used to store multiple values in one variables.
        -  A lists is collections of different datatypes stored in one variables.
        - lists are written using square bracket ()
        - lists items are seperated by commas (,).
        - lists are orderd,so every items has an index.
        - lists are mutable ,means we can change then after creation.
        - lists can store different datatypes together.
        - lists are allow duplicates items."""

# how to create a lists:- in pythons we can create lists in two ways:-

'''Using list built-in functions:-
   syntax:- 
            fist=list()'''
#ex:-
fist1=list() #this is an empty list ,no items in the list.
print(len(fist1)) #0

'''Using Square Bracket []:-
    syntax:-
          fist2=[]'''
#ex:-
fist2=[] #this is an empty lists ,no items in the list.
print(len(fist2)) #0

# Lists with initial values .we use len() to find the length of a lists.

fruits=['banana','oranges','mango','lemaon']
vegetables=["tomato","potato","cabbage","onion","carrot"]
animals=['dog','monkey','cat','elephant','cow']
web_tech=["html","css","c","js","python","java","node"]
country=['india','finland','denmark',]

print('Fruits:',fruits)
print('Nubers of Fruits:',len(fruits))
print("Animals:",animals)
print("Numbers os Animals:",len(animals))
print('Vegetables:',vegetables)
print('Nubers of Vegetables:',len(vegetables))
print("Web technology:",web_tech)
print("Numbers of Web tech:",len(web_tech))

# List can have items of different datatypes :-

list_name =["sulema",20,True, 39.5,{'country:' 'finland','city:''halki'}]
print(list_name) 

""" Accessing List items : we access each items in a list using their index.
   - lists items are accessed using index numbers.
   - Python indexing starts from 0.
   - Positive index starts from the left.
   - Negative index starts from the right & it's starts from -1.
 
   lists      : [ "aman","rahul","kabir","abhi","jeet"]
   posi index :     0       1       2       3      4  
   nega index :    -5      -4      -3      -2     -1  """

#ex:-
fruits=['mango','orange','apple','banana','guava']
print(fruits[0])
print(fruits[3])
print(fruits[2])
print(fruits[1])
print(fruits[-5])
print(fruits[-1])
print(fruits[-4])
#last index
last_index=len(fruits)-1
print("last_fruits:",fruits[last_index])


""" Unpacking lists items:- means agar list ke ander multiple value hain aur hum   un values ko alag-alag variables main nikalna chata ho, usko unpacking kehta hain.
 """

numbers=[19,48,39]
a,b,c=numbers
print(a)
print(b)
print(c)

'''numbers=[34,63,73,78,]
a,b,c=numbers
print(a)
print(b)
print(c)
print(a) #value error ,q ki 4 values hain lekin variables sirf 3 hain.
'''
""" * ka use karke multiple value lena:- ager tum chahte ho ki ek variables baki ki saari values ko lists ke form mein le le, tho * use karte hain. """

numberss=[10,20,30,40,50]
a,b,*c=numberss
print(a) #10 
print(b) #20
print(c) #[30,40,50]

#Yaadi beech main(*):-
numberses=[10,20,30,40,50,60,70,80,90]
a,b,*c,d=numberses
print(a) #10
print(b) #20
print(c) #[30,40,50,60,70,80]
print(d) #90

'''Another way:-
   - *rest= jo value bach jaayein,sab mujhe de do.
   - rest koi special python keywords nahi hai, tum iska name kuch bhi rakh sakte ho.
     ex:-
         a,*b=numbers
         a,*remaining=numbers
    - Ek unpacking mein normally sirf ek starred variables ho sakti hai.
          ex: 
               a,*b,*c=numbers # that is wrong     '''
numbers=[10,20,30,40,50,60]
a,*rest=numbers
print(a)
print(rest)
'''Another way:-  *scandic,es=fruits
-scandic ko tum kuch bhi valid variable name de sakte ho and es=fruits ,this is always  store last items. 
       Ex:-m,o,*rest,sul=fruits
           m,o,*middle,var=list_name'''
fruits=['mango','orange','apple','grapes','guava','banana','almods']
m,o,*middle,sul=fruits
print(m)
print(o)
print(middle)
print(sul,"\n")
"""Agar hum chate hai ke last variable ek sa jada items store kara:-
  m,o,*middle,sul=fruits:- lakin python mein ye allowed nahi hai--ek unpacking assignment main 2starred variables nahi ho sakte
    Tho tumhera desired result kaise milega?
     tab Slicing use karo:- exple-"""
m,o=fruits[:2]
middle=fruits[2:5]
sul=fruits[5:]
print(m)
print(o)
print(middle)
print(sul)

"""Slicing items from a lists:-"""
#positive:-
numbers =[10,20,30,40,50,60,70,80,90]
all_number=numbers[0:9]
print(numbers[0:9])
print(numbers[0:])
print(numbers[1:6])
print(numbers[:9])
print(numbers[2:6])
print(numbers[2:6:2])
print(numbers[1:8:3],"\n")
all_numbers=numbers[-10:]
print(all_numbers)
print(all_numbers[-3:-1])
print(all_numbers[:-6])
print(all_numbers[-2:-6])
print(all_numbers[:-6])
print(all_numbers[-2:-8:-1])
print(all_numbers[::-1]) #reverse
print(all_numbers[:]) #fully slicing


"""Adding items to a list:- To add items to the end of an existing lists we use the method append().
 syntax :- number=list()
           number.append(items) { end mein item add karna means last mein add} """
fruits=['banana','orange','mango','lemon','apple']
fruits.append('guava')
print(fruits)
fruits.append('lime')
print(fruits,'\n')

"""Inserting items into a lists:- we can use insert() method to insert a single items at a specified index in a list.
 - that other items are shifted to the right .
 - the insert() methods takes two arguments , index and item to insert.
   Syntax:- city=['item1','item2']
            city.insert(index,item) {kisi kspecific position par add karna}"""
fruits=['apple','mango','orange']
fruits.insert(1,'lemon')
print(fruits)
fruits.insert(3,'banana')
print(fruits)

"""Extend items into a list:- Ek list ke multiple items ko doosri list ke end mein add karta hai.{multiple items add karna end main}
   Syntax:- list_name.extend(['items','items'])"""
fruits=['apple','orange','mango']
#fruits.append(['lime','guava'])
##print(fruits) #['apple','orange','mango',['lime','guava']] puri list ko ek single item bana deta hai.Lakin:-
fruits.extend(['lime','guava'])
print(fruits) #['apple',orange','mango','lime','guava']

"""Modifying /Change/Update items in lists:- lists is  a mutable or modifying  ordered collection of items.
   Syntax:-  list_name[index]=new_value """
fruits=['apple','banana','lemon']
fruits[0]='avocado'
print(fruits)
fruits[1]='apple'
print(fruits)
last_index=len(fruits)-1
fruits[last_index]='lime'
print(fruits)
#multiple items:-
fruits=['apple','mango','lime','banana']
fruits[1:3]=['grapes','guava']
print(fruits)
fruits[0:3]=['avacodo','banana','lemon']
print(fruits,"\n")

"""Checking items in a list:- Python mein list mein item check karna matlab dekhna ki koi particular items list ke ander hai ya nahi.
   - That is use two operator :-
       1. in operator
       2. not in operator
   -These operator  also name is membership operator.
   - they gives output is True and False.
           Syantax:- item in list_name        """
fruits=['banana','apple','orange']
print('mango' in fruits) # F Q ki mango list mein nahi hai.
print('orange' in fruits) #T
print('guava' not in fruits) #T Q ki guava list ka ander mein nahi hai.
print('banana' not in fruits) #F Qdki banana list ke ander hai.

"""Removing items from a list:-The remove method removes a specified item from a list(value se item remove) 
   Syntax:- list_name=['items','items']
            list_name.remove(item) """
numbers=[19,45,58,89,38,74,]
numbers.remove(45)
print(numbers)
fruits=['suleman','sultan','sahil','deepak']
fruits.remove('sahil')
print(fruits)
#fruits.remove('suleman','deepak')
#print(fruits) type error dega .

"""Removing items using Pop:- The pop() method romoves the specified index,(or the last item if index is not specidied)
    Syntax:-
         lists=['items','items']
         lists_name.pop()  {last items remove because index is not put in }.
         lists_name.pop(index) """
fruits=['banana','apple','mango','lemon']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)
fruits.pop(-1)
print(fruits)

"""Removing items using Del:- The del keywords removes the specified index &it can also be used to delete items within index range.
  - it can also delete the lists completely.
    Syntax:- list_name=['items','items']
             del list_name {to delete the list completely}
             del list_name[index] 
             """
fruits=[10,39,20,40,59,28,50,60,90,367,45.6,78.99]
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits
#print(fruits),because namesrror ,fruits is not defined.

"""Clearing lists items:-The clear() method empities the lists.
   Syntax:- list_name=['items','items']
            list_name.clear() """
numbers=[19,40,39,20,10,500,]
numbers.clear()
print(numbers) #[] that is empty.

"""Copying in a lists:-Python mein lists copying ka matlab hai ek list ki copy karna.
     Syntax:- list_name=['item','item']
              new_list_name=list_name.clear()"""
fruits=['apple','orange','banana','mango']
new_fruits=fruits.copy()
print(new_fruits) #o/p same aaya ga isliye 
new_fruits[0]='kiwi'
print(fruits)
print(new_fruits)

"""Joining items in lists:- There are several ways to join ,or concatenate,two or more lists in python."""
 # (+) plus operator:-
 #Syntax:- list3=list1 + list2
posi_no=[1,2,3,4,5]
zero=[0]
neg_no=[-5,-4,-3,-2,-1]
integer=neg_no + zero + posi_no
print(integer)
fruits=['banana','orange','mango','lemon']
vegetable=['tomato','potato','cabbage','onion']
frui_vege=fruits+vegetable
print(frui_vege)
'''Joining using extend() method the extend() method allows to append list in a list.
   Syntax:-
    list1=['item1','item2]
    list2=['item3','item4','item5']
    list1.extend(list2) {list1 ke sarre items ko list2 ke end main add hojayega.}
    list2.extend(list1) {list2 ke sarre items ko list1 ke end main add hojayaga.}'''
num1=[0,1,2,3,4,5]
num2=[6,7,8,9,10,]
num1.extend(num2)
print("numbers:",num1)
neg_no=[-5,-4,-3,-2,-1]
posi_no=[1,2,3,4,5]
zero=[0]
neg_no.extend(zero)
neg_no.extend(posi_no)
print("Integers:",neg_no)

"""Counting items in a lists:- The count() method returns the numbers of times an item appers in a lists.
  Syntax:- list_name.count() """
numbers=[10,20,30,10,30,40,10,50,10,60,]
print(numbers.count(10)) #4 Q ki 10 list ke ander 4 baar hai.
fruits=['apple','suleman','orange','banana',"sulemann",'suleman']
print(fruits.count('suleman')) #'suleman' ye list ka ander 2 baar hai,"suleman" alag hai .

"""Finding index of an items:- The index() methods returns the index of an items in the lists.
  Syntax:- list_name.index(item)"""
boys=['suleman','deepak','arun','rahul','aman']
print(boys.index('suleman'))
print(boys.index('aman'))
ages=[22,34,90,22,10,50,30,22]
print(ages.index(22)) # 0 q ki the first occurrence.

"""Reversing a list:- The reverse() method reverse the order of a list.
   Syntax:- list_name.reverse()"""
fruits=['banana','apple','orange','lemaon']
fruits.reverse()
print(fruits)
ages=[10,20,30,40,50,60]
ages.reverse()
print(ages)

"""Sorting lists items:- To sort lists we can use sort() methods or sorted() built-in function.
 -The sort() methods reorders the list items in ascending order & modifies the original lists.if the argument of sort() methods reverse is equal to true,it will arrenge the list in decending order.

 - sort():- this methods modifies the original list.
  Syntx:- list=['item','item']
         list_name.sort() {ascending}
         list_name.sort(reverse=True) {decending}"""
fruits=['banana','apple','orange','mango']
fruits.sort()
print(fruits) #alphabetice order
ages=[10,60,30,59,20,60,]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

#sorted():- returns the ordered list without modifying the original list.
fruits=['apple','banana','orange','lemaon','mango']
print(sorted(fruits))
boyes=['aman','rahul','abhi','jeet','suleman']
boyes=sorted(boyes,reverse=True)
print(boyes)




