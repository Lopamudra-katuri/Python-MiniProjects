import random
print('Welcome To Your Password Generator')

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'
num=int(input('Amount of passwords need to be generated: '))
length=int(input('Length of your password: '))

print('\n Your passwords are:')

for pwd in range(num):
    password=''
    for c in range(length):
        password +=random.choice(chars)
    print(password)
