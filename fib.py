# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


#fib(1000)

#(36°C × 9/5) + 32 = 96.8°F
celcius = input('Enter celcius temp: ')

