try:
    values=[10,20,30]
    index=int('5')
    print(values[index])
except ValueError: print('Index must be an integer')
except IndexError: print('Index is outside the list')
