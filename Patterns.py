n=int(input("Enter the number rows:"))
for i in range(1,n+1):
    print("* "*n)

n=int(input("Enter the number rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

n=int(input("Enter the number rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

n=int(input("Enter the number rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()

n=int(input("Enter the number rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-j,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+n-i),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+n-j),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
    
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(i,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+i),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+j),end=" ")
    print()
    
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-i,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-j,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(65+n-i),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(65+n-j),end=" ")
    print()
    
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),"* "*i,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),(str(i)+" ")*i)
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),(chr(64+i)+" ")*i)
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),"*"*(n+1-i))

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),(str(n+1-i)+"")*(n+1-i))

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(j,end="")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),(str(chr(65+n-i))+"")*(n+1-i))

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(65,66+n-i):
        print(chr(j),end="")
    print()
