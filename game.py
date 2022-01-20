import random

m=1
ma=10

def question():
    points=0
    i=1
    while i<=4:
        a=random.randint(m,ma)
        b=random.randint(m,ma)
        o=random.randint(0,1)
        if o==0:
            s="+"
        else:
            s="*"
        
        print(i,".) solve {} {} {}".format(a,s,b))
        n=int(input())
        if (a+b)==n or (a*b)==n:
            print("right answer!")
            points=points+1
        else:
            print("wrong answer")
        i=i+1
    print("you score ",points,"out of 4")   
    if points<3:
        print("You can do better")
    elif points>=3:
        print("Good!")

question()  
