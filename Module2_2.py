first = int(input('type first number:'))
second = int(input('type second number:'))
third = int(input('type third number:'))

if first == second and second == third :
    print('3')
elif first == second or first == third or second == third :
    print('2')
else :
    print('0')