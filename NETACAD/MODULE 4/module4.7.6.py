def set_age(age):
    if age<0: raise ValueError('Age cannot be negative')
    return age
try: print(set_age(-2))
except ValueError as error: print('Error:',error)
