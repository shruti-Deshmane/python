task = input("enter the operation (/ for division)(+ for addition)( - for subtraction)(* for multiplication)")

number_1 = float(input('Enter  first number: '))
number_2 = float(input('Enter second number: '))

if task == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif task == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif task== '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif task == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('enter valid operator')