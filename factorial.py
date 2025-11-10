def factorial(num):
    if num == 1:
        return 1
    else:
        fact = num * factorial(num - 1)
        return fact

val = int(input('Enter a number: '))
print(f'Factorial of {val} is: {factorial(val)}')