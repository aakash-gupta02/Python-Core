# Accept two numbers and print the greatest between them.
"""

num1 = int(input("Enter first Number"))
num2 = int(input("Enter second Number"))

if num1 > num2:
    print(f"{num1}, is Greater")
elif num1 < num2:
    print(f"{num2}, is Greater")
else:
    print(f"{num1} & {num2} is Equal")   


#Q2. Accept the gender from the user as char and print the respective greeting message

gender = input("Enter your Gender M or F:")

if gender == "M":
    print("Good Morning, Sir")

else:
    print("Good Morning, Madam")





#Q3. Accept an integer and check whether it is an even number or odd.

num1 = int(input("Enter first Number"))

if num1%2 == 0:
    print(f"{num1} is a Even Number")

else:
    print(f"{num1}, is a Odd Number")


"""


#Q4. Accept name and age from the user. Check if the user is a
# valid voter or not.



name = input("Enter your Name: ")
age = int(input("Enter your Age: "))

if age <= 18:
    print(f"{name}, u are not allowed to Vote now")
else:
    print(f"{name}, u are allowed to Vote now")

