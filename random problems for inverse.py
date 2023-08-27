import random
order=int(input("type the order of matrix: "))

if order>=2:

    a=float(random.randint(-50,50))
    b=float(random.randint(-50,50))
    c=float(random.randint(-50,50))
    d=float(random.randint(-50,50))
    if order>=3:
        e=float(random.randint(-50,50))
        f=float(random.randint(-50,50))
        g=float(random.randint(-50,50))
        h=float(random.randint(-50,50))
        i=float(random.randint(-50,50))
        print("successfully generated a quesation")
if order==2:
    print([a,b])
    print([c,d])
elif order==3:
    print([a,b,e])
    print([c,d,f])
    print([g,h,i])

existance=input("type inverse exist(y) or not(n): ")
if existance=="y":

    if order==2:
        ans11=float(input("type your a11 here: "))
        ans12=float(input("type your a12 here: "))
        ans21=float(input("type your a21 here: "))
        ans22=float(input("type your a22 here: "))

    if order==3:
        ans11=float(input("type your a11 here: "))
        ans12=float(input("type your a12 here: "))
        ans13=float(input("type your a13 here: "))
        ans21=float(input("type your a21 here: "))
        ans22=float(input("type your a22 here: "))
        ans23=float(input("type your a23 here: "))
        ans31=float(input("type your a31 here: "))
        ans32=float(input("type your a32 here: "))
        ans33=float(input("type your a33 here: "))
elif existance=="n":
    print('inverse does not exist as determinant=0')


if order==2:
    det=(a*c)-(b*d)
    if det==0:
        print('inverse does not exist as determinant=0')
    else:
        print([d/det,-b/det])
        print([-c/det,a/det])
elif order==3:
    det=(a*((d*i)-(h*f)))-(b*((c*i)-(f*g)))+(e*((c*h)-(d*g)))
    if det==0:
        print('inverse does not exist as determinant=0')
    else:

        cofactor11=(d*i)-(f*h)
        cofactor22=(a*i)-(e*g)
        cofactor33=(a*d)-(b*c)
        cofactor31=(b*f)-(e*d)
        cofactor13=(c*h)-(d*g)

        cofactor12=(c*i)-(f*g)
        cofactor21=(b*i)-(e*h)
        cofactor23=(a*h)-(b*g)
        cofactor32=(a*f)-(e*c)
    
        minor11=cofactor11
        minor22=cofactor22
        minor33=cofactor33
        minor31=cofactor31
        minor13=cofactor13

        minor12=-cofactor12
        minor21=-cofactor21
        minor23=-cofactor23
        minor32=-cofactor32
    
        adj11=minor11
        adj12=minor21
        adj13=minor31
        adj21=minor12
        adj22=minor22
        adj23=minor32
        adj31=minor13
        adj32=minor23
        adj33=minor33


        
        a11=adj11/det
        a12=adj12/det
        a13=adj13/det
        a21=adj21/det
        a22=adj22/det
        a23=adj23/det
        a31=adj31/det
        a32=adj32/det
        a33=adj33/det

        if ans11==a11 and ans12==a12 and ans13==a13 and ans21==a21 and ans22==a22 and ans23==a23 and ans31==a31 and ans32==a32 and ans33==a33 or existance=="y":
            print("correct answer")
            print([ans11,ans12,ans13])
            print([ans21,ans22,ans23])
            print([ans31,ans32,ans33])
        else:
            print("wrong answer")
            print("right answer is")
            print([a11,a12,a13])
            print([a21,a22,a23])
            print([a31,a32,a33])

