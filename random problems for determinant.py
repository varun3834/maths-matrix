import random
order=int(input("type the order of matrix: "))

if order>=2:
    # a=float(random.uniform(-100,100)) random float value

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

if order==3:
    print([a,b,e])
    print([c,d,f])
    print([g,h,i])

ans=float(input("type your answer here: "))

if order ==2:
    correct=(a*c)-(b*d)
elif order==3:
    correct=(a*((d*i)-(h*f)))-(b*((c*i)-(f*g)))+(e*((c*h)-(d*g)))

if ans == correct:
    print("correct answer")
else:
    print(correct)