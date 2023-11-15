from modules import calculator
import math
import random2

# Get the first number from user
first_number = int(input('Insert your first number:'))

# Get the second number from user
second_number = int(input('Insert your second number:'))

# Get the operations from user
operations = input('Insert your operations :')

# This IF statment for compare input from user 
if operations == '+':
  print(f"Result: {calculator.addition(first_number, second_number)}")
elif operations == '-':
  print(f"Result: {calculator.subtraction(first_number, second_number)}")
elif operations == '*':
  print(f"Result: {calculator.multiplication(first_number, second_number)}")
elif operations == '/':
  print(f"Result: {calculator.division(first_number, second_number)}")
elif operations == 'power':
  print(f"Result: {math.pow(first_number, second_number)}")
elif operations == 'sqr':
  print(f"Result: {math.sqrt(first_number)}")
elif operations == 'random':
  print(f"Result: {random2.randint(first_number, second_number)}")
