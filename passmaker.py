import random
import time
print ('''
        *****************************
        *                           *
        *       Password Maker      *
        *                           *
        *****************************
    ''')


chars_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

numberOfpassword = int(input('enter the number of password ==> '))
numberOfcharactor = int(input('password lenght ==>  '))

if numberOfpassword == 1:
    print('password is making...')
elif numberOfpassword <= 0:
    print('is not define...!')
elif numberOfpassword >= 2:
    print('passwords is making...')        

for pwd in range(numberOfpassword):
    password = ''
    for con in range(numberOfcharactor):
        password += random.choice(chars_list)
    print(f'pssword was maked ====> {password}')
    time.sleep(1)