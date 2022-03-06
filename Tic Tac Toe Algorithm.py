# Tic Tac Toe

board = {}
row = ('r1','r2','r3')
col = ('c1','c2','c3')
for i in row:
    for j in col:
        key = i + j
        board[key] = 0
c = ('r1c1','r1c3','r3c1','r3c3')
e = ('r2c1','r2c3','r1c2','r3c2')
#Considering the user wants to play against computer in hard mode

i = input('Enter the place which you want to take (row no. and column no.)\nEx: r1c2, r3c1, etc.\n')
board[i] = 'x'
    
if i in c:
    board['r2c2']='o'
elif i in e:
    
elif i == 'r2c2':
    board[c[1]] = 'o'