#Hangman Game

import random

d = ['SHOTGUN', 'ASSAULT', 'SUBMACHINE', 'CROSSBOW', 'HUNTING', 'COMBAT', 'TACTICAL']

def ind(p,y):
    f = []
    for i in range(len(y)):
        if p == y[i]:
            f = f + [i]
    return f

def ifset(p,y):
    u = 0
    for i in range(len(p)):
        if p[i] in o:
            u+=1
    if u >= 1:
        return True
    else:
        return False


while True:

    v = input("Do you wanna play?(Y/N): ")

    if v == 'N' or v == 'n':
        break

    elif v == 'Y' or v == 'y':
        r = random.randint(0,6)
        w = d[r]
        l = len(w)
        print("The word is of",l,"letter.")
        print('*'*l)
        t = 0
        c = l+2
        h = 0
        o=[]
        bb=[]

        while t != c and h != l:
            g = input("Guess the letter of the word: ")
            g = g.upper()
            
            if len(g) != 1:
                print("Press one letter only!")
                continue

            else:

                if ifset(ind(g,w),o) or g in bb:
                    print("You have already guessed this letter")

                elif g in w and not(ifset(ind(g,w),o)):
                    print("Correct guess!")
                    o = o + ind(g,w)
                    h += 1*len(ind(g,w))

                else:
                    print("Incorrect guess")
                    bb = bb + [g]
                    t += 1 

            for i in range(0,l):
                if g == w[i] or i in o:
                    print(w[i],end='')
                else:
                    print('*',end='')
            print()
            print('You can now only make',c-t,'wrong guesses')
            print()

        if t == c:
            print("You're out of guesses :(")
            print("The word was",w)

        else:
            print("Congrats! You have guessed the correct word",w,"!")

    else:
        print("Invalid input")
