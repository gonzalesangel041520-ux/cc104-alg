try:
    quantity=int('4')
    price=float('25.50')
    total=quantity*price
except ValueError: print('Invalid input')
else: print(f'Total: {total:.2f}')
finally: print('Calculation finished')
