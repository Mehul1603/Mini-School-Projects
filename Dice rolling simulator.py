import random
while True:
    x=input("Do you want to throw dice?(Y/N) ")
    if x.lower()=='y':
        r=random.randint(1,6)
        print("It landed",r)
    elif x.lower()=='n':
        break
    else:
        print("Invalid input")