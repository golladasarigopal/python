#Functions without args and without return keyword
def count():
    a=input("Enter the string:")
    c=0
    for i in a:
        c+=1
    print(c)
count()
count()
count()

#Functions with args and without return keyword
def square(a,b):
    if a%2==0 and b%2==0:
        print((a**2)+(b**2))
    else:
        print("Not even numbers:")
square(int(input("Enter the even numbers only:")),int(input("Enter the even numbers only:")))
square(int(input("Enter the even numbers only:")),int(input("Enter the even numbers only:")))
square(20,30)

#Functions without args and with return keyword
def cal():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    return a+b,a-b,a*b,a/b,a//b,a%b
print(cal())

#Functions with args and with return keyword
def perfect(a):
    a=int(input("Enter the number:"))
    b=[]
    for i in range(1,a):
        s=0
        for j in range(1,i):
            if i%j==0:
                s+=j
        if s==i:
            b+=[i]
    return b
print(perfect(1000))

#Tuple Packing
def pack(*t):
    print(t)
    print(type(t))
pack((1))
pack((True,False))
pack((3+4j))
pack('hai')

#Dictionary Packing
def pack(**d):
    print(d)
    print(type(d))
pack(a1=True,b2=2,c3=3)

#Tuple UnPacking
p='python'
q=(1,2,3,4)
def unpack(a,b,c,d,e=1,f=1):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
unpack(*p)
unpack(*q)

#Dictionary UnPacking
d={'a':1,'b':2,'c':3}
def unpack(a,b,c):
    print(a)
    print(b)
    print(c)
unpack(**d)

#Random Module in Python(OTPs)
import random
a=random.randint(1,9)
b=random.randint(10,99)
c=random.randint(100,999)
print(a)
print(b)
print(c)'''

#Global, Loval, Non-Local Variables
a=10
b=20
def outer():
    p,q=1,3
    print(a,b)
    print(p,q)
    def inner():
        nonlocal p
        p=100
        print(p)
    inner()
    print(p)
outer()
    
    
