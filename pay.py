#calculator to work out weekly pay
print('My weekly pay calculator')
print('------------------------')

#collect hours and rate of pay
hrsWorked = input('Enter hours worked: ')
ratePay = input('Enter rate of pay: ')
print('\n')

#calculate and display weekly pay
wPay = int(hrsWorked) * float(ratePay)
print(f'Your weekly pay will be ${wPay:.2f}')

