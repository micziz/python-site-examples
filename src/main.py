def fib(n):
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
fib(1000)

fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)
list(enumerate(fruits))

1 / 2
2 ** 3
17 / 3
17 // 3

print("Hello, I'm Python!")
name = input('What is your name?\n')
print('Hi, %s.' % name)

numbers = [2, 4, 6, 8]
product = 1
for number in numbers:
    product = product * number
print('The product is:', product)