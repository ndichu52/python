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
""""
this is commenting
print(hello universe)
print(hello world)
""""

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
    print("b is not greater t

