order=int(input("type the order of matrix: "))

if order>=2:
    a=float(input("type number at a(1,1) place: "))
    b=float(input("type number at a(1,2) place: "))
    c=float(input("type number at a(2,1) place: "))
    d=float(input("type number at a(2,2) place: "))
    if order>=3:
        e=float(input("type number at a(1,3) place: "))
        f=float(input("type number at a(2,3) place: "))
        g=float(input("type number at a(3,1) place: "))
        h=float(input("type number at a(3,2) place: "))
        i=float(input("type number at a(3,3) place: "))
        # print("successfully added all elements")

if order==2:
    print([a,b])
    print([c,d])

if order==3:
    print([a,b,e])
    print([c,d,f])
    print([g,h,i])

# ans=float(input("type your answer here: "))

if order ==2:
    correct=(a*c)-(b*d)
elif order==3:
    correct=(a*((d*i)-(h*f)))-(b*((c*i)-(f*g)))+(e*((c*h)-(d*g)))




# if ans == correct:
#     print("correct answer")

