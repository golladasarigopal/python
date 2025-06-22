#LOOPING STATEMENTS

#FOR LOOP

#1. Print Numbers from 1 to N
n = 10
for i in range(1, n + 1):
    print(i, end=" ")

#2. Multiplication Table
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#3. Sum of First N Numbers
n = 100
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)

#4. Factorial of a Number
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

#5. Fibonacci Series (First N Terms)
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
    
#6. Reverse a String
s = "Interview"
rev = ""
for char in s:
    rev = char + rev
print("Reversed:", rev)

#7. Count Vowels in a String
s = "Python Developer"
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Vowel count:", count)

#8. Check for Prime (Single Number)
num = 29
is_prime = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")

#9. Print Right-Angled Triangle Pattern
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
    
#10. Find Largest Element in List
arr = [3, 8, 1, 99, 32]
max_num = arr[0]
for num in arr:
    if num > max_num:
        max_num = num
print("Largest number:", max_num)

#WHILE LOOP

#1. Print Numbers from 1 to N
n = 10
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
    
#2. Reverse a Number
num = 1234
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed:", rev)

#3. Check Palindrome Number
num = 121
temp = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Palindrome" if temp == rev else "Not Palindrome")

#4. Count Digits in a Number
num = 56789
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digit count:", count)

#5. Sum of Digits
num = 12345
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)

#6. Print Even Numbers up to N
n = 10
i = 2
while i <= n:
    print(i, end=" ")
    i += 2
    
#7. Check Prime Number
num = 17
i = 2
is_prime = True
while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1
print("Prime" if is_prime else "Not Prime")

#8. Fibonacci Series
n = 10
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

#9. Menu Driven Calculator (Basic Use of While Loop)
while True:
    print("\n1.Add  2.Subtract  3.Exit")
    choice = int(input("Enter choice: "))
    if choice == 3:
        break
    a = int(input("A: "))
    b = int(input("B: "))
    if choice == 1:
        print("Sum:", a + b)
    elif choice == 2:
        print("Difference:", a - b)
    else:
        print("Invalid choice")

#10. Print Pattern with While
rows = 5
i = 1
while i <= rows:
    print("*" * i)
    i += 1



