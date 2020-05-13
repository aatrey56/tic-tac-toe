import random

def board():
    global over
    global board
    board = [[None, None, None], \
            [None, None, None], \
            [None, None, None]]
    over = 0
    print("Welcome to Tic Tac Toe! You will be playing the computer. Enter the column and row numbers from 0-2 to make your move.")

def printBoard():
    print("0\t1\t2")
    for i in range (3):
        print(board[i])

def uTurn():
    uRow=int(input("What row do you want your piece at?"))
    uColumn=int(input("What column do you want your piece at?"))
    if (uRow>2):
        print("That's out of bounds")
        uTurn()
    elif(uColumn>2):
        print("That's out of bounds")
        uTurn()
    else:
        board[uRow][uColumn]=("X")
        printBoard()
        print("\nComputer's turn")

def cTurn():
    cRow=random.randint(0,2)
    cColumn=random.randint(0,2)
    if ((board[cRow][cColumn])==("X")):
        cTurn()
    else:
        board[cRow][cColumn]=("O")
        printBoard()
        print("\nYour turn")

def winner():
    if(board[0][0]==board[0][1]==board[0][2]):        
        if((board[0][0])==("X")):
            print("You win!")
            over += 1
        elif((board[0][0])==("O")):
            print("You lose...")
            over += 1
        elif((board[0][0])==(None)):
            return
    elif(board[1][0]==board[1][1]==board[1][2]):        
        if((board[1][0])==("X")):
            print("You win!")
            over += 1
        elif((board[1][0])==("O")):
            print("You lose...")
            over += 1
        elif((board[1][0])==(None)):
            return

    elif(board[2][0]==board[2][1]==board[2][2]):        
        if((board[2][0])==("X")):
            print("You win!")
            over += 1
        elif((board[2][0])==("O")):
            print("You lose...")
            over += 1
        elif((board[2][0])==(None)):
            return

    elif(board[0][0]==board[1][0]==board[2][0]):        
        if((board[0][0])==("X")):
            print("You win!")
            over += 1
        elif((board[0][0])==("O")):
            print("You lose...")
            over += 1
        elif((board[0][0])==(None)):
            return

    elif(board[0][1]==board[1][1]==board[2][1]):        
        if((board[0][1])==("X")):
            print("You win!")
            over += 1
        elif((board[0][1])==("O")):
            print("You lose...")
            over += 1
        elif((board[0][1])==(None)):
            return

    elif(board[0][2]==board[1][2]==board[2][2]):        
        if((board[0][2])==("X")):
            print("You win!")
            over += 1
        elif((board[0][2])==("O")):
            print("You lose...")
            over += 1
        elif((board[0][2])==(None)):
            return

    elif(board[0][0]==board[1][1]==board[2][2]):        
        if((board[0][0])==("X")):
            print("You win!")
            over += 1
        elif((board[0][0])==("O")):
            print("You lose...")
            over += 1
        elif((board[0][0])==(None)):
            return

    elif(board[0][2]==board[1][1]==board[2][0]):        
        if((board[0][2])==("X")):
            print("You win!")
            over += 1
        elif((board[0][2])==("O")):
            print("You lose...")
            over += 1
        elif((board[0][2])==(None)):
            return        

def game():
    while(over==0):
        uTurn()
        cTurn()
        winner()

board()
game()