#CONDITIONAL or DECISIONAL STATEMENTS
#IF STATEMENT:

#1.Check if a number is positive
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")

#2.Check if a number is negative
number = int(input("Enter a number: "))

if number < 0:
    print("The number is negative.")

#3.Check if a number is zero
number = int(input("Enter a number: "))

if number == 0:
    print("The number is zero.")

#4.Check if a number is greater than 10
number = int(input("Enter a number: "))

if number > 10:
    print("The number is greater than 10.")

#5.Check if a string is empty
text = input("Enter some text: ")

if text == "":
    print("You entered an empty string.")

#6.Check if a person is eligible for a discount (age >= 65)
age = int(input("Enter your age: "))

if age >= 65:
    print("You are eligible for a discount.")

#7.Check if a number is divisible by 3
number = int(input("Enter a number: "))

if number % 3 == 0:
    print("The number is divisible by 3.")

#8.Check if a number is odd
number = int(input("Enter a number: ")
             )
if number % 2 != 0:
    print("The number is odd.")

#9.Check if the number is even
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")

#10.Check if a character is a vowel
char = input("Enter a character: ").lower()

if char in 'aeiou':
    print(f"The character '{char}' is a vowel.")


#IF-ELSE STATEMENT:

#1.Check if a number is positive or negative
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

#2.Check if a number is even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#3.Check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#4.Check if a person is eligible to vote (age >= 18)
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#5.Check if a number is divisible by 5
number = int(input("Enter a number: "))

if number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

#6.Find the largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater than {b}.")
else:
    print(f"{b} is greater than {a}.")

#7.Check if a number is greater than 100
number = int(input("Enter a number: "))

if number > 100:
    print("The number is greater than 100.")
else:
    print("The number is less than or equal to 100.")

#8.Check if a number is within a specific range (10 to 50)
number = int(input("Enter a number: "))

if 10 <= number <= 50:
    print("The number is within the range of 10 to 50.")
else:
    print("The number is out of the range.")

#9.Check if a string is a palindrome
string = input("Enter a string: ")

if string == string[::-1]:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

#10.Grade Calculation Based on Marks
marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
else:
    print("Grade below A")



#IF-ELIF-ELSE STATEMENT:
    
#1.Check if a number is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#2.Check if a number is even, odd, or zero
number = int(input("Enter a number: "))

if number == 0:
    print("The number is zero.")
elif number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
#3.Grade calculation based on marks
marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

#4.Check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#5.Check if a number is divisible by 5, 10, or neither
number = int(input("Enter a number: ")
             )
if number % 5 == 0 and number % 10 == 0:
    print("The number is divisible by both 5 and 10.")
elif number % 5 == 0:
    print("The number is divisible by 5.")
elif number % 10 == 0:
    print("The number is divisible by 10.")
else:
    print("The number is divisible by neither 5 nor 10.")

#6.Check if a person is eligible for voting or not
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You will be eligible to vote in 2 years.")
else:
    print("You are not eligible to vote yet.")

#7.Check the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"The largest number is {a}.")
elif b >= a and b >= c:
    print(f"The largest number is {b}.")
else:
    print(f"The largest number is {c}.")

#8.Check if a number is between 1 and 100
number = int(input("Enter a number: "))

if 1 <= number <= 100:
    print("The number is between 1 and 100.")
else:
    print("The number is not between 1 and 100.")
#9.Check if a number is positive, negative, or zero, with additional condition for large numbers
number = float(input("Enter a number: "))

if number > 1000000:
    print("The number is very large.")
elif number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#10.Check if a character is a vowel, consonant, or other
char = input("Enter a character: ").lower()

if char in 'aeiou':
    print(f"The character '{char}' is a vowel.")
elif char.isalpha():
    print(f"The character '{char}' is a consonant.")
else:
    print("The input is not a valid alphabet character.")


#NESTED-IF STATEMENT:

#1.Check if a number is positive, negative, or zero, and further check if it’s even or odd
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif number < 0:
    if number % 2 == 0:
        print("The number is negative and even.")
    else:
        print("The number is negative and odd.")
else:
    print("The number is zero.")

#2.Check if a year is a leap year and if it's divisible by 400
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if year % 400 == 0:
        print(f"{year} is a leap year and divisible by 400.")
    else:
        print(f"{year} is a leap year but not divisible by 400.")
else:
    print(f"{year} is not a leap year.")

#3.Check if a student passes or fails based on marks and further check if they passed with distinction
marks = float(input("Enter your marks: "))

if marks >= 50:
    if marks >= 75:
        print("You passed with distinction!")
    else:
        print("You passed.")
else:
    print("You failed.")

#4.Check if a number is between 1 and 100, and if it's odd or even
number = int(input("Enter a number: "))

if 1 <= number <= 100:
    if number % 2 == 0:
        print("The number is between 1 and 100 and is even.")
    else:
        print("The number is between 1 and 100 and is odd.")
else:
    print("The number is not between 1 and 100.")

#5.Check if a person is eligible to vote and if they are a senior citizen (age >= 65)
age = int(input("Enter your age: "))

if age >= 18:
    if age >= 65:
        print("You are eligible to vote and you are a senior citizen.")
    else:
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#6.Check if a number is positive and divisible by both 5 and 10
number = int(input("Enter a number: "))

if number > 0:
    if number % 5 == 0 and number % 10 == 0:
        print("The number is positive and divisible by both 5 and 10.")
    else:
        print("The number is positive but not divisible by both 5 and 10.")
else:
    print("The number is not positive.")

#7.Check if a number is a multiple of 3 and 5, and further check if it's also a multiple of 10
number = int(input("Enter a number: "))

if number % 3 == 0:
    if number % 5 == 0:
        if number % 10 == 0:
            print("The number is a multiple of 3, 5, and 10.")
        else:
            print("The number is a multiple of 3 and 5, but not 10.")
    else:
        print("The number is a multiple of 3 but not 5.")
else:
    print("The number is not a multiple of 3.")

#8.Check if a string contains a vowel and further check if it starts with a vowel
string = input("Enter a string: ").lower()

if any(vowel in string for vowel in 'aeiou'):
    if string[0] in 'aeiou':
        print(f"The string '{string}' contains a vowel and starts with a vowel.")
    else:
        print(f"The string '{string}' contains a vowel but does not start with a vowel.")
else:
    print(f"The string '{string}' does not contain any vowels.")

#9. Check if a person is eligible for a senior citizen discount and further check if they have a disability
age = int(input("Enter your age: "))
has_disability = input("Do you have a disability? (yes/no): ").lower()

if age >= 65:
    if has_disability == "yes":
        print("You are eligible for a senior citizen discount and you have a disability.")
    else:
        print("You are eligible for a senior citizen discount.")
else:
    print("You are not eligible for a senior citizen discount.")

#10.Check if a number is a prime number and further check if it's greater than 10
num = int(input("Enter a number: "))

if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        if num > 10:
            print(f"{num} is a prime number and is greater than 10.")
        else:
            print(f"{num} is a prime number but not greater than 10.")
    else:
        print(f"{num} is not a prime number.")
else:
    print(f"{num} is not a prime number.")




















































