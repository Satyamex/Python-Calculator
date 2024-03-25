# In this program I will make calculator using if-else statements

# here is greeting part of program
print("Welcome to calculator User! ")

# First I will assign values to their variable
num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the second number: "))
op = input("What do you want to do? ")
result = 1.0

# Now we make our calculator
if op == '+':
    result = num1+num2
    print("The result is :- " + str(result))

elif op == '-':
    result = num1-num2
    print("The result is :- " + str(result))

elif op == '*':
    result = num1*num2
    print("The result is :- " + str(result))

elif op == '/':
    result = num1/num2
    print("The result is :- " + str(result))

else:
    print("ERROR! make sure your input was a real function")
