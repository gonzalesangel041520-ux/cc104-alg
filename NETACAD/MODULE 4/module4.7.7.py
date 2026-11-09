try:
    int('abc')
except ValueError as error: print('Conversion failed:',error)
