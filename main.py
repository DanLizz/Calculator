import art
print(art.logo)

#Addition
def add(num1, num2):
  """Add num1 and num2 and return the sum"""
  return num1 + num2

#Subtraction
def subtract(num1, num2):
  """Subtract num2 from num1 and return the result"""
  return num1 - num2

#Multiplication
def multiply(num1, num2):
  """Multiply num1 and num2 and return the result"""
  return num1 * num2

#Divide
def divide(num1, num2):
  """Divide num1 with num2 and return the result"""
  return num1 / num2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():

  print(art.logo)

  n1 = float(input("Enter the first number: "))

  for symbol in operations:
    print(symbol,end =" ")
  answer = n1

  yes = True
  while yes:
    operation_symbol = input("Pick an operation: ")
    n2 = float(input("Enter the next number: "))
    answer = operations[operation_symbol](answer, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")
    repeat = input("Type 'y' to continue calculating, or type 'n' to start new calculation:").lower()
    if repeat == 'y':
      yes = True
      n1 = answer
    else:
      yes = False
      calculator()

calculator()