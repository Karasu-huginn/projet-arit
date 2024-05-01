from tkinter import *
from random import randint
import math


def message_keep_letters(message):  # removes spaces and apostrophes and returns a string
    message = list(message)
    for i in range(len(message)-1,0,-1):
        if message[i] == " " or message[i] == "'":
            message.pop(i)
    message = listToString(message)
    return message

def listToString(list, additionnalValue=''):    # transform a list into a string and returns it
    string = ''
    for i in range(len(list)):
        string += list[i] + additionnalValue
    return string

def display_board(board):   # displays the board in the console
    for i in range(len(board)):
        for u in range(len(board)):
            print(board[i][u], end=' ')
        print('')

def determine_board_length(message):    # determines the needed length of the board to contain the whole message
    for i in range(0,100):
        if i%2 == 0:
            if i*i >= len(message):
                return i
        else:
            if (i*i)-1 >= len(message):
                return i

def test_move(board, x, y, maxCoord, character):    # test function to rotate a character along the grid
    board[x][y] = character
    x, y = y, maxCoord-x
    return x,y

def get_rotated_coord(x,y, maxCoord):   # test function to only get a rotated version of coordinates
    x, y = y, maxCoord-x
    return x,y

def adapt_length(length):   # adapt the length for the test_move() function
    if length%2 == 0:
        return length
    else:
        return length-1

def substring_divide(message, length):  # divides a string into multiple strings by a given length and returns a list storing them
    addedLength = 0
    listOfStrings = list()
    while addedLength < len(message):
        listOfStrings.append(message[addedLength:length+addedLength])
        addedLength += length
    return listOfStrings


message = "c'est un message a chiffrerrr"
message = message_keep_letters(message)
n = determine_board_length(message)
length = adapt_length(n)
board = [[0]*n for i in range(n)]   # creates a bidimensional list containing 0s
#x = 4
#y = 1

coords = list()
coordsPair = [0,0]
for i in range(math.floor(n/2)):
    for u in range(math.ceil(n/2)): # on sélectionne un coin entier de cases
        x, y = u, i
        for j in range(randint(0,4)):
            x, y = get_rotated_coord(x,y, length)
        coordsPair[0], coordsPair[1] = x, y
        coords.append(coordsPair[0:])
print(coords)

dividedMessage = substring_divide(message, math.floor(n/2)*math.ceil(n/2))
print(dividedMessage)

for i in range(4):
    display_board(board)
    print(dividedMessage[i])
    for u in range(math.floor(n/2)*math.ceil(n/2)):
        board[coords[u][0]][coords[u][1]] = dividedMessage[i][u]
    for u in range(math.floor(n/2)*math.ceil(n/2)):
        coords[u][0], coords[u][1] = get_rotated_coord(coords[u][0], coords[u][1], length)
display_board(board)


#for i in range(4):
#    x,y = test_move(board, x, y, n-1, message[i])





"""
root = Tk()
root.geometry("820x300")
root.title("Menu de jeu")
root.config(bg="white")
root.config(padx=0, pady=10)
labelMessage = Label(root, text="Message à chiffrer :\n")
labelMessage.place(x=10, y=10, width=800, height=40)
entryMessage = Entry(root)
entryMessage.place(x=10, y=60, width=800, height=20)
label2 = Label(root, text="Message à déchiffrer")
label2.place(x=10, y=80, width=800, height=20)
diago = Entry(root)
diago.place(x=10, y=140, width=800, height=20)
taillelabel5 = Label(root, text="")
taillelabel5.place(x=10, y=160, width=800, height=20)
root.mainloop()
"""
#valider = Button(root, text="Valider", command=lambda:inputs(taille,taillelabel2,diago,taillelabel5,root))
#valider.place(x=10, y=180, width=800, height=40)
#start = Button(root, text="start vs player", command=lambda:plateau(False,taille,taillelabel2,diago,taillelabel5,root))
#start.place(x=10, y=220, width=380, height=40)
#start = Button(root, text="start vs computer", command=lambda:plateau(True,taille,taillelabel2,diago,taillelabel5,root))
#start.place(x=430, y=220, width=380, height=40)
