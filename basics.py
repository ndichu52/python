#syntax identantion
if 5>2:
   print("five is greater than two")

#variables
userAge=0
print(userAge)

#defining multiple variables in onego
userAge2, username = 22, "thor"
print(userAge2)
print(username)

#assigning same values to multiple variables
x = y = z ="oranges"
print(x)
print(y)
print(z)

#unpacking lists to variables
fruits =("apple","sugercane","banana",321)
a,b,c,d = fruits
print(a)
print(b)
print(c)
print(d)

#global functions
s = "good"
def myfunct():
    print("python is" +s)
myfunct()

#create a variable with the same name as as the global variable
t="awesome"
def myfunct():
 t ="fantastic"
 print("python is" +t)
myfunct()
print("python is"+t)

a="a"

print(a+a)

#datatypes
w=5
print(type(w))

e=5.0
print(type(e))
t="cow"
print(type(t))

u=5j
print(type(u))

#randomnumber
import random
print(random.randrange(1,10))





x=5
 #stings

e = "Andrew"
print(e)
print(type(e))

#multilinestring
f = """ My Name is Andrew
    First of His Name
    Leader of the Free World """
print(f)

t = "Hello World"
print(t[5])

#strings as arrays
for x in "banana":
    print(x)

#checkstringlength
p = "Kenya is the best"
print(len(p))

#check string
txt = "The Best things in Life are Expensive"
print("Expensive" in txt)
print("Free" in txt)

#Strings in if statements
txt = "The best things in life are Expensive"
if "Expensive2" in txt:
    print("Expensive is present")

#check if not
txt= "The best things in life are expensive"
print("free" not in txt)

#slicing strings
b = "  Hello, World  "
print(b[2:5])
print(b[:5])
print(b[5:])
#modify string
#upppercase
print(b.upper())
#lowecase
print(b.lower())
#Removewhitespace
print(b.strip())
#Replacestring
print(b.replace("H","K"))
#split string
print(b.split(","))

#stringconcatination
a = "Hello"
b = "World"
c= a+b
print(c)

#formatmethod
age= 20
txt = "My Name is Andrew and I am {}"
print(txt.format(age))

#Boolean
print(10>9)
print(10==9)
print(10<9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater t")

print(bool("hello"))
print(bool(15))


#evaluate two variables
a="hello"
b=15
c=0
d=""

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))

#Print the answer to a function
def myfunct():
    return True
print(myfunct())

def myfunct():
    return True
if myfunct():
    print("YES!")
else:
    print("NO!")
#modulus operators
a=12%2
print(a)
#Python lists
thislist =["apple","banana","cherry","melon","orange","kiwi"]
print(thislist)
print(thislist[1])
print(thislist[-2])
print(thislist[2:5])
print(thislist[-4:-3])
#check if items exist
if "apple "in thislist:
    print("apple is  in this list")
else:
    print("apple is not in this list")
#change item value
thislist[1]="black current"
print(thislist)
thislist[1:2]=["black current","lemon"]
print(thislist)

#insert items
thislist =["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)
#apeend items
thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

#extend list
thislist =["apple","banana","cherry"]
tropical=["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)
#remove method
thislist.remove("papaya")
print(thislist)

#popindex
thislist =["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

# delete method
thislist =["apple","banana","cherry"]
del thislist

#python tuples
thistuple=("apple","banana","cherry")
print(thistuple)

#check tuple length
print(len(thistuple))

#single tuple
thistuple=("watermelon",)
print(type(thistuple))

#access tuple items
thistuple=("apple","banana","cherry","kiwi","melon","mango")
print(thistuple[1])

#negative indexing
print(thistuple[-1])

#range indexes
print(thistuple[2:5])

#range of negative indexes
print(thistuple[-4:-1])

#update tuples
x=("apple","banana","cherry")
y= list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

#createset
thisset={"apple","banana","cherry"}
print(thisset)
#python dictionary
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict)

#userinput
#username= input("enter your username")
#print("username is:"+ username)

#if Else
a=60
b=60
if b>a:
    print("b is greater than a")

#elif- if the previuos condition were not true , then try this
elif a==b:
    print("a and b are equal")

#else- catches anything that isn't caught by preceding conditions
a=500
b=100
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b is equal")
else:
    print("a is greater than b")

#nestedif-if statement inside an if statement
x=50
if x>10:
    print("above ten")
    if x>20:
        print("and also above 20")
    else:
        print("but not above 30")

#while loops
i=1
while i<6:
    print(i)
    i+=1
#break statement
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

#continue statement
i=0
while i<6:
    i+=1
    if i==3:
        continue
        print(i)

#else statement
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

#for loops
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)

#looping through a string

#if else break statement
for x in range(6):
    if x ==3:break
    print(x)
else:
        print("finally finished")

#nested loops

adj=["red","big","tasty"]
fruits=["apple","banana""cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

#python functions
def my_function():
    print("hello from my functions")
my_function()

#arguments
def my_function(fname):
    print("hello from a function")

my_function("andrew")
my_function("emily")
my_function("ian")

#numder of arguments
def my_function(fname,lname):
    print(fname+""+lname)
my_function("ian","andrew")

#default paeameter value
def my_function(country="kenya"):
    print("i am from " +country)
my_function("sweden")
my_function( "india")
my_function()
my_function("brazil")

#return value
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#class
class person:
    def __init__(self,name, age,hieght, weight,catch_phrase):
        self.name=name
        self.age= age
        self.hieght= hieght
        self.weight=weight
        self.catch_phrase= catch_phrase

p1= person("ian",102,20,72,"you kwon nothing jon snow")
print(p1.name)
print(p1.age)
print(p1.hieght)
print(p1.weight)
print(p1.catch_phrase)

#class person:
def __int__(self,name,age):
        self.name =name
        self.age =age

def __str__(self):
        return f"{self.name}({self.age})"
#p1 =person("john",36)
#print(p1)

class person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}{self.age}"

p1=person2("john",36)
print(p1)

class person3:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = person3("John", "Doe")
x.printname()
