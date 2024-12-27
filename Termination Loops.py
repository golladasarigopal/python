'''class add:
    def __new__(cls):
        print("Creating the object:")
        return super(add,cls).__new__(cls)
    def __init__(self):
        self.a=10
        print("Object member created:")
obj=add()'''


class add:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.d=self.a+self.b+self.c
        print(self.d)
obj=add(4,5,6)
obj1=add(2,4,6)
obj2=add(7,4,1)
