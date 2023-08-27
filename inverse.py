order=int(input("type the order of matrix: "))

if order>=2:
    a=float(input("type number at a(1,1) place: "))
    b=float(input("type number at a(1,2) place: "))
    c=float(input("type number at a(2,1) place: "))
    d=float(input("type number at a(2,2) place: "))
    if order==2:
        print("successfully added all elements")
    if order>=3:
        e=float(input("type number at a(1,3) place: "))
        f=float(input("type number at a(2,3) place: "))
        g=float(input("type number at a(3,1) place: "))
        h=float(input("type number at a(3,2) place: "))
        i=float(input("type number at a(3,3) place: "))
        print("successfully added all elements")

if order==2:
    print('your typed matrix')
    print([a,b])
    print([c,d])
    check=input("""type your input here:
                  n if not right matrix: """)

elif order==3:
    print('your typed matrix')
    print([a,b,e])
    print([c,d,f])
    print([g,h,i])
    check= input("""type your input here:
                  n if not right matrix: """)
if check=="n":
    raise "key error in matrix"
else:
    pass


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

        print([adj11/det,adj12/det,adj13/det])
        print([adj21/det,adj22/det,adj23/det])
        print([adj31/det,adj32/det,adj33/det])

    
