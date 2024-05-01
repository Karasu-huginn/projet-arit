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

def get_rotated_coord(x,y, maxCoord, clock):   # get a rotated version of coordinates
    if clock:
        x, y = y, maxCoord-x
    else: 
        x, y = maxCoord-y, x
    return x,y

def substring_divide(message, length):  # divides a string into multiple strings by a given length and returns a list storing them
    addedLength = 0
    listOfStrings = list()
    while addedLength < len(message):
        listOfStrings.append(message[addedLength:length+addedLength])
        addedLength += length
    return listOfStrings

def message_adapt_length(message, n):   # adds random characters at the end of the message to make it long enough to fit the grid
    if n*n-len(message) != 0:
        for i in range(n*n-len(message)):
            message = ''.join([message,chr(randint(97,122))])
    return message

def get_key_grid(board, coords):    # prints the grid-key to decypher the message afterwards, can be modified later on to save it in a separate file
    for i in range(len(coords)):
        board[coords[i][0]][coords[i][1]] = 1
    print(board)

def key_to_coords(key): # gets the coordinates needed to decypher the message
    coords = list()
    coordsPair = [0, 0]
    for i in range(len(key)):
        for u in range(len(key[i])):
            if key[i][u] == 1:
                coordsPair[0], coordsPair[1] = i, u     #! might affect final result
                coords.append(coordsPair[0:])
    return coords

def reset_key_board(board, coords):
    for i in range(len(board)):
        for u in range(len(board[i])):
            board[i][u] = 0
    for i in range(len(coords)):
        board[coords[i][0]][coords[i][1]] = 1
    return board


def cypher(message, clock):
    message = message_keep_letters(message)
    n = determine_board_length(message)
    message = message_adapt_length(message, n)
    length = n-1
    board = [[0]*n for i in range(n)]   # creates a bidimensional list containing 0s
    keyBoard = [[0]*n for i in range(n)]
    coords = list()
    coordsPair = [0,0]
    for i in range(math.floor(n/2)):
        for u in range(math.ceil(n/2)): # on sélectionne un coin entier de cases
            x, y = u, i
            for j in range(randint(0,4)):
                x, y = get_rotated_coord(x,y, length, clock)
            keyBoard[x][y] = 1
            coordsPair[0], coordsPair[1] = x, y
            coords.append(coordsPair[0:])
    display_board(keyBoard)
    get_key_grid(board, coords)

    dividedMessage = substring_divide(message, math.floor(n/2)*math.ceil(n/2))

    
    for i in range(4):
        char = 0
        for u in range(n):
            for j in range(n):
                if keyBoard[u][j] == 1:
                    board[u][j] = dividedMessage[i][char]
                    char += 1
        display_board(board)
        print('')
        for u in range(math.floor(n/2)*math.ceil(n/2)):
            coords[u][0], coords[u][1] = get_rotated_coord(coords[u][0], coords[u][1], length, clock)
        keyBoard = reset_key_board(keyBoard, coords)
        display_board(keyBoard)
    display_board(board)

def decypher(message, clock, key):
    coords = key_to_coords(key)
    n = len(key)
    print(coords)
    message = substring_divide(message, n)
    board = [[0]*(len(message)*6//4) for i in range(4)]
    print(board)
    for i in range(4):
        for u in range(len(message)*6//4):
            board[i][u] = message[coords[u][0]][coords[u][1]]
    
        for u in range(math.floor(n/2)*math.ceil(n/2)):
            coords[u][0], coords[u][1] = get_rotated_coord(coords[u][0], coords[u][1], n-1, clock)
        print(coords)
    print(board)

#key = [[0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0]]
#message = "iceffecressriscagstesreestuloanngchm"
key = [[0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0]]
message = "ryuoyutodurosimncptoeaumanokvtheehab"
decypher(message, True, key)

#message = "yourmouthdontmovebuticanhearyouspeak"
#cypher(message, True)



#board = cypher(message)
#test = ''
#for i in range(6):
#    test += listToString(board[i])
#print(test)


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
