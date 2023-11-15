# Get the first number from user
first_number = int(input('Insert your first number:'))

# Get the second number from user
second_number = int(input('Insert your second number:'))

# Get the operations from user
operations = input('Insert your operations :')

# This IF statment for compare input from user 
if operations == '+':
  print(first_number + second_number)
elif operations == '-':
  print(first_number - second_number)
elif operations == '*':
  print(first_number * second_number)
else:
  print("We don't support this operation")

# This code print message on screen
print("Thanks for using our software")

