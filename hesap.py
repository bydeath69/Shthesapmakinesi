#python 3.7.1

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
print("Select operation.")
print("1.Ekle")
print("2.Çıkarmak")
print("3.Çarpmak")
print("4.Bölmek")
while(1):
  # Take input from the user 
  choice = int(input("Işlem (1/2/3/4):"))
  num1 = int(input("Ilk numarayi girin: "))
  num2 = int(input("Ikinci numarayi girin: "))
  if choice == 1:
    print(num1,"+",num2,"=", add(num1,num2))
  elif choice == 2:
    print(num1,"-",num2,"=", subtract(num1,num2))
  elif choice == 3:
    print(num1,"*",num2,"=", multiply(num1,num2))
  elif choice == 4:
    print(num1,"/",num2,"=", divide(num1,num2))
  else:
    print("Invalid input")
