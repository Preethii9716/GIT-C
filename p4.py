mark1=int(input("Enter mark1"))
mark2=int(input("Enter mark2"))
mark3=int(input("Enter mark3"))
if(mark1>mark2 and mark1>mark3):
    if(mark2>mark3):
        print("Mark 1 and Mark 2 is bigger")
        print("The average of both is",(mark1+mark2)/2)
    else:
        print("Mark1 and Mark3 is bigger")
        print("Te average of both is",(mark1+mark3)/2)
elif(mark2>mark1 and mark2>mark3):
    if(mark1>mark3):
        print("Mark 2 and Mark 1 is bigger")
        print("The average of both is",(mark2+mark1)/2)
    else:
        print("Mark2 and Mark3 is bigger")
        print("Te average of both is",(mark2+mark3)/2)
else:
    if(mark1>mark2):
        print("Mark 3 and Mark 1 is bigger")
        print("The average of both is",(mark3+mark1)/2)
    else:
        print("Mark3 and Mark2 is bigger")
        print("Te average of both is",(mark3+mark2)/2)
