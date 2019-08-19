# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


#fib(1000)

hours = int(input('Enter Hours: '))
rate = int(input('Enter Rate: '))

print('Pay: ', hours*rate)
