'''#Default Constructor
class add:
    def __new__(cls):
        print("Creating an object:")
        return super(add,cls).__new__(cls)
obj=add()'''

'''#Non-Default Constructor
class add:
    def __new__(cls):
        print("Creating an object:")
        return super(add,cls).__new__(cls)
    def __init__(self):
        self.a=10
        print("Object member created:")
obj=add()'''

'''#Non-Parameterized Constructor
class add:
    def __init__(self):
        self.a=int(input("Enter the number:"))
        self.b=int(input("Enter the number:"))
        self.c=self.a+self.b
        print(self.c)
obj=add()
obj1=add()'''

'''#Parameterized Constructor
class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
        print(self.c)
obj=add(4,8)
obj1=add(9,7)'''

'''#Example
class student:
    clgname="KMM College"
    clgadd="Tirupati"
    principal="Gopal"
    university="SV University"
    def __init__(self):
        self.sname=input("Enter the Name:")
        self.sid=int(input("Enter the ID Number:"))
        self.phno=int(input("Enter the phno:"))
        self.perc=int(input("Enter the Per:"))
        self.add=input("Enter the Address:")
        self.gender=input("Enter the Gender:")
    def display(self):
        print(self.sname)
        print(self.sid)
        print(self.phno)
        print(self.perc)
        print(self.add)
        print(self.gender)
obj=student()
obj.display()
obj1=student()
obj1.display()'''



import pickle
d={
    "sname":"Rajesh",
    "Gender":"Male",
    "Degree":"B.Tech"
  }
out=pickle.dumps(d)
print(out)
t=pickle.dumps((1,2,3))
s=pickle.dumps({1,2,3})
c=pickle.dumps((3+4j))

print(pickle.loads(out))
print(pickle.loads(t))
print(pickle.loads(s))
print(pickle.loads(c))

    
