#BREAK STATEMENT
# 1. Stop when target found in list
nums = [1, 3, 5, 7, 9]
target = 7
for num in nums:
    if num == target:
        print("Found:", num)
        break

# 2. Search character in string
s = "interview"
for char in s:
    if char == 'v':
        print("Character found:", char)
        break

# 3. Password retry system
for attempt in range(3):
    pwd = input("Enter password: ")
    if pwd == "admin":
        print("Access granted")
        break
else:
    print("Access denied")

# 4. Prime check with break
n = 11
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# 5. Exit loop on negative number
nums = [2, 4, -3, 6]
for n in nums:
    if n < 0:
        print("Negative number found:", n)
        break

# 6. Break in nested loop
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(i, j)

# 7. Stop input on 'exit'
while True:
    data = input("Enter text: ")
    if data == "exit":
        break
    print("You entered:", data)

# 8. Break when sum > 100
total = 0
for i in range(1, 20):
    total += i
    if total > 100:
        print("Sum exceeded 100 at:", i)
        break

# 9. Stop printing after 5
for i in range(10):
    if i == 5:
        break
    print(i)

# 10. Skip menu on wrong input
menu = ["Login", "Register", "Exit"]
while True:
    choice = input("Choose (1-3): ")
    if choice == "3":
        print("Exiting...")
        break

#CONTINUE sTATEMENTS

# 1. Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 2. Skip empty names
names = ["John", "", "Emma", ""]
for name in names:
    if name == "":
        continue
    print("Name:", name)

# 3. Skip vowels in string
s = "interview"
for char in s:
    if char in "aeiou":
        continue
    print(char, end="")

# 4. Skip if age is invalid
ages = [22, -1, 30, 0]
for age in ages:
    if age <= 0:
        continue
    print("Valid age:", age)

# 5. Print only positive numbers
nums = [-2, 3, -1, 5]
for n in nums:
    if n < 0:
        continue
    print("Positive:", n)

# 6. Skip a specific word
words = ["hello", "skip", "world"]
for word in words:
    if word == "skip":
        continue
    print(word)

# 7. Skip login if already logged in
users = ["admin", "guest", "loggedin"]
for user in users:
    if user == "loggedin":
        continue
    print("Logging in:", user)

# 8. Continue until divisible by 5
for i in range(1, 11):
    if i % 5 != 0:
        continue
    print("Divisible by 5:", i)

# 9. Skip wrong input
inputs = ["yes", "", "no", None]
for val in inputs:
    if not val:
        continue
    print("Input:", val)

# 10. Skip loop at a condition in while loop
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("i =", i)

#PASS STATEMENT
    
# 1. Empty function placeholder
def my_function():
    pass

# 2. Empty class
class MyClass:
    pass

# 3. Empty exception block
try:
    x = 1 / 0
except ZeroDivisionError:
    pass

# 4. Placeholder for TODO
def future_feature():
    pass  # Will implement later

# 5. Pass in if block
x = 10
if x > 0:
    pass  # valid case

# 6. Use in loop for placeholder
for i in range(5):
    if i == 3:
        pass
    print(i)

# 7. Pass in nested if-else
num = 5
if num > 0:
    if num == 5:
        pass
    else:
        print("Positive number")

# 8. Use inside method
class Test:
    def process(self):
        pass

# 9. Placeholder inside recursion
def recur(n):
    if n == 0:
        pass
    else:
        recur(n-1)

# 10. Use in class inheritance
class A:
    pass

class B(A):
    def method(self):
        pass


