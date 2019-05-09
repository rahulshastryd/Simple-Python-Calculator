# Program make a simple calculator that can add, subtract, multiply and divide using functions

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

# This function calcuates x to the power of y
def power(x, y):
  result = 1
  counter = 0
  while counter < y:
    result = result * x
    counter += 1
  return result  


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power Of")

isRunning = True

while isRunning:
  choice = input("Enter choice(1/2/3/4/5) or 0 for exit:")

  if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    isRunning = False
  elif choice == '0':
    print("Exiting program..")
    exit()
  else:
    print("Invalid input! Please, try again.")
    

  if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

  elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

  elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

  elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))

  elif choice == '5':
    print(num1,"to the power of ",num2,"=", power(num1,num2))
