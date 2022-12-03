a = int(input("How many terms? "))
number1, number2 = 0, 1
count = 0
if a <= 0:
   print("Please enter a positive integer")

elif a == 1:
   print("Fibonacci sequence upto",a,":")
   print(number1)
else:
   print("Fibonacci sequence:")
   while count < a:
       print(number1)
       nth = number1 + number2
       number1 = number2
       number2 = nth
       count += 1
