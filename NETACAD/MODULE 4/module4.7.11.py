def divide(a,b): return a/b
try:
    print(divide(float('12'),float('3')))
except ValueError: print('Enter valid numbers')
except ZeroDivisionError: print('Cannot divide by zero')
