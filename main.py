# Question 1
upper_limit = 2700
lower_limit = 1500

for num in range(lower_limit, upper_limit):
    if num & 7 == 0 and num % 5 == 0:
        print(num)

# Question 2
# Program to Convert Celsius To Fahrenheit
celsius = float(input("Enter temperature in celsius:"))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))

# Program to Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' % (fahrenheit, celsius))
