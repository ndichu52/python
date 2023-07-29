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

