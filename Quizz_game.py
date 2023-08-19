print("welcome to my computer guizz game")

playing = input("do you want to play?")

if playing.lower() == "yes":
    print("okay! let's play")
    score=0
else:
    print("too bad for you")
    quit()

answer =input("what does RAM stand for")
if answer.lower()=="random access memory":
    print("this is correct")
    score +=1
else:
    print("this is in correct")

answer =input("what does ROM stand for")
if answer.lower()=="read only memory":
    print("this is correct")
    score +=1
else:
    print("this is in correct")

answer =input("what does CPU stand for")
if answer.lower()=="central processing unit":
    print("this is correct")
    score +=1
else:
    print("this is in correct")

answer =input("what does bios stand for")
if answer.lower()=="basic input output prossesor":
    print("this is correct")
    score +=1
else:
    print("this is in correct")

print("you got" +str(+score) +"questions correct!!")
print("you got"+ str((score/4)*100)+ "%")