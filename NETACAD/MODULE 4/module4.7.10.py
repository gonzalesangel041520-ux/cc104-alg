class InsufficientBalanceError(Exception): pass
def withdraw(balance,amount):
    if amount>balance: raise InsufficientBalanceError('Insufficient balance')
    return balance-amount
try: print(withdraw(500,800))
except InsufficientBalanceError as error: print('Declined:',error)
