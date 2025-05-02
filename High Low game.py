import random

a = eval(input('Enter the lower and upper limit as a tuple: '))
l,u=a
r = random.randint(l,u)
r = 7

x = 9
while x > 0:
    g = int(input("Enter a  guess: "))
    if g < r:
        x -= 1
        if x == 0:
            continue
        print('Your number is LOWER than the number')
    
    elif g > r:
        x -= 1
        if x == 0:
            continue
        print('Your number is HIGHER than the number')
    
    else:
        print('Correct\nCongrats! You won!')
        break
else:
    print('You are out of guesses.')