#!/usr/bin/env python3

def admin_login(username, password):
 
 if(username.lower() == 'admin' or username.upper()== 'admin') and password == '12345':
    return "access granted"
 else: 
    return 'Access denied'
  

def hows_the_weather(temperature):
    if(temperature < 40):
       return 'Its brisk out there'
    elif(temperature > 40 and temperature < 65):
       return 'Its a little chilly out there'
    elif(temperature >85):
       return 'Its too dng hot out there'
    else :
       return 'Its perfect out there!'
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation!"
