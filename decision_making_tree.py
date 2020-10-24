print("1)TABLE OF YOUR GIVEN NUMBER\n2)ADDITION\n3)SUBTRACTION\n4)MULTIPLICATION\n5)DIVISION\n6)DESIGN PATTERNS\n7)DRAW SHAPES")
temp=int(input("enter your choice within 1-7:"))
if(temp==1):
    p=int(input("Enter the number of which you want to print table:"))
    for i in range(1,11):
        print(p,"*",i,"=",p*i)   
if(temp==2):
    p=int(input("Enter first number"))
    q=int(input("Enter second number"))
    r=p+q
    print("Result is ",r)
if(temp==3):
    p=int(input("Enter first number"))
    q=int(input("Enter second number"))
    r=p-q
    print("Result is ",r)
if(temp==4):
    p=int(input("Enter first number"))
    q=int(input("Enter second number"))
    r=p*q
    print("Result is ",r) 
if(temp==5):
    p=int(input("Enter first number"))
    q=int(input("Enter second number"))
    r=p/q
    print("Result is ",r) 
if(temp==6):
    print("---:PATTERN DESIGNS:---")
    print("1)****\n  ****\n  ****\n  ****\n\n2)1\n  2 3\n  4 5 6\n\n3)*\n  * *\n  * * *")
    p=int(input("Enter any choice 1-3:->"))
    if(p==1):
        for i in range(4):
            for j in range(4):
                print("*",end=' ')
            print("\n")
    if(p==2):
        x=1
        for i in range(1,4):
            for j in range(i):
                print(x,end=' ')
                x+=1
            print("\n")    
    if(p==3):
        for i in range(1,4):
            for j in range(i):
                print("*",end=' ')
            print("\n")    
if(temp==7):
    print("---:SHAPE DESIGNING:---")
    print("1)Make a circle\n2)Make a square\n3)Make triangle")
    p=int(input("Enter your choice 1-3:->"))
    import turtle
    x=turtle.Turtle()
    if(p==1):
        z=int(input("Enter the radius of the circle"))
        x.begin_fill()
        x.fillcolor("red")
        x.circle(z)
        x.end_fill()
    if(p==2):
        z=int(input("Enter the sides of square"))
        x.begin_fill()
        x.fillcolor("blue")
        for i in range(4):
            x.forward(z)
            x.left(90)
        x.end_fill()
    if(p==3):
        z=int(input("Enter the sides of triangle"))
        x.begin_fill()
        x.fillcolor("red")
        x.circle(z,steps=3)
        x.end_fill()    
