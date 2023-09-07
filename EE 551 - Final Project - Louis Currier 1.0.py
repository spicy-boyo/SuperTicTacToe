## EE 551A - Engineering Programming: Python
## Final Project - Louis Currier

#To play the games run the game engine function as it calls the rest

class Board():
    def __init__(self): #Initializes the board array
        self.values = ["-","-","-","-","-","-","-","-","-"]
        self.markers = ["X","O"]
    
    def __str__(self): #Overwrites the print function to print as a board
        return (" " + str(self.values[0]) + " | " + str(self.values[1]) + " | " + str(self.values[2]) + "\n" 
                "-----------"+"\n"
                " " + str(self.values[3]) + " | " + str(self.values[4]) + " | " + str(self.values[5]) + "\n"
                "-----------"+"\n"
                " " + str(self.values[6]) + " | " + str(self.values[7]) + " | " + str(self.values[8]) + "\n")
    
    def takeTurn(self,turn,space): #Takes in what turn it is and what space is being taken
        if self.values[space] != "-": #Makes sure the space is not taken
             print("Invalid move. Pick another space.")
             return False
        elif turn % 2 == 0: #X always goes first and then they alternate
            self.values[space] = "X"
        else:
            self.values[space] = "O"
        return True
    
    
    def checkWin(self): #Goes through all possible win conditions for both values
        for i in self.markers:
            if self.values[0] == self.values[1] == self.values[2] == i:
                return i #Returns value of winner
            elif self.values[3] == self.values[4] == self.values[5] == i:
                return i
            elif self.values[6] == self.values[7] == self.values[8] == i:
                return i
            elif self.values[0] == self.values[3] == self.values[6] == i:
                return i
            elif self.values[1] == self.values[4] == self.values[7] == i:
                return i
            elif self.values[2] == self.values[5] == self.values[8] == i:
                return i
            elif self.values[0] == self.values[4] == self.values[8] == i:
                return i
            elif self.values[2] == self.values[4] == self.values[6] == i:
                return i 
        return 0 #Returns zero if no winner yet
    
    def checkStalemate(self): # Checks the board for stalemate by fill-out
        if "-" not in self.values: #If the board is full, the game is a tie
            return True
        return False

def convert(space): #This function is used to convert the inputs into indices of the array
    if space == "1 1":
        return 0
    elif space == "1 2":
        return 1
    elif space == "1 3":
        return 2
    elif space == "2 1":
        return 3
    elif space == "2 2":
        return 4
    elif space == "2 3":
        return 5
    elif space == "3 1":
        return 6
    elif space == "3 2":
        return 7
    elif space == "3 3":
        return 8
    else:
        print("Invalid space! Remember type 'row space column'")
        return

def ticTacToe(): #Main Tic Tac Toe Game
    newBoard = Board() #Generates the play space
    winCon = 0 #Initializes a winCon
    turnCounter = 0 #Initializes a turn counter for the game
    print("As a heads up, X always goes first. To pick a spot to place type the row and then the column that you want." + "\n" + "i.e. the middle spot is '2 2'")
    while winCon == 0:
        print(newBoard) #Prints the board after each turn
        space = input("Where do you want to put your space?\n")
        space = convert(space)
        if space in range(9): #Needed to assure the value as a int
            newBoard.takeTurn(turnCounter,space) #Apply the takeTurn method from Board class
            winCon = newBoard.checkWin()#Apply the win check which is in terms of X, O and Draw
            if winCon == "O" or winCon == "X":
                print(newBoard) #Prints the won board
                print(winCon + " wins!") #Winner statement
                return winCon
            else: # If no win, game continues
                if newBoard.checkStalemate() == True:# Draw handling
                    print(newBoard)
                    print("It's a draw!?")
                    return "Draw"
                else: #No changes so game continues to next turn
                    turnCounter += 1

def rockPaperScissors(): #Rock paper scissors chosen to break ties
    print("To break the tie, you'll play Rock Paper Scissors. Winner is best of 3.")
    xwins = 0 #Initialize both wins
    owins = 0
    winner = False #Initialize win condition
    while  winner == False:
        p1 = None #These conditions reset the game on each game so its best of three
        p2 = None
        valid1 = False
        valid2 = False
        while valid1 != True: #Loop to make sure that a valid choice is made
            p1 = input("Player X select 'rock' 'paper' or 'scissors'")
            if p1 == "rock" or p1 == "paper" or p1 == "scissors":
                valid1 = True
            else:
                print("Please enter a valid choice!")
        while valid2 != True: #Loop to make sure that a valid choice is made for player 2
            p2 = input("Player X select 'rock' 'paper' or 'scissors'")
            if p2 == "rock" or p2 == "paper" or p2 == "scissors":
                valid2 = True
            else:
                print("Please enter a valid choice!")
        #These if/elif statements check winners and win conditions as well as ties
        if p1 == "rock" and p2 == "scissors" or p1 == "paper" and p2 == "rock" or p1 == "scissors" and p2 == "paper":
            print("X threw out " + p1 + " and O threw out " + p2) #Statement of inputs
            print("That's a win for X!") #Winner of round
            xwins += 1
            if xwins == 2:
                print("X wins!") #winner of game
                return "X"
        #This next is same as last but for O
        elif p2 == "rock" and p1 == "scissors" or p2 == "paper" and p1 == "rock" or p2 == "scissors" and p1 == "paper":
            print("X threw out " + p1 + " and O threw out " + p2)
            print("That's a win for O!")
            owins += 1
            if owins == 2:
                print("O wins!")
                return "O"
        else: #Check for draws
            print("X threw out " + p1 + " and O threw out " + p2)
            print("Draw! Try again.")

def ticTacToeSquared(): #New addition, tic tac toes in tic tac toe
    winCon = 0 #initializing win condition and the board
    t2Board = Board()
    print("Welcome to Tic Tac Toe Squared, its like before but each space has to be fought for!\nX gets to choose first, but who gets the space depends on who wins it")
    while winCon == 0:
        print(t2Board)#Print the overall board after each win
        choice = input("Which space do you want to fight for? \n Remember to state as 'row space column'.")
        choice = convert(choice)#Same convert method
        spaceWinner = ticTacToe() #Tic tac toe regular is played out and the winner is set
        if spaceWinner == "Draw": #Handles draw condition
            print("Can't end on a draw, so onto our tie breaker")
            spaceWinner = rockPaperScissors()
        if choice in range(9):#Similar to regular tic tac toe
            if spaceWinner == "X":
                t2Board.takeTurn(0,choice) #Takes the board space for x if winner
            elif spaceWinner == "O":
                t2Board.takeTurn(1,choice) #Takes the board space for O if winner
            winCon = t2Board.checkWin() # check for win
            if winCon == "O" or winCon == "X": #If the game is won
                print(t2Board) #Print the board
                print(winCon + " wins!") #State the winner
                return winCon
            else: #Handles non wins
                if t2Board.checkStalemate() == True:#If theres a stalemate, ends in draw
                    print(t2Board)
                    print("It's a draw!?")
                    return "Draw"
                #else of this, the game just continues

## Main body of code
gameCounter = 0
while True:
    if gameCounter == 0:#Welcome message
        print("Welcome to Tic Tac Toe Squared! If you're ready to play a game type 'Game on'")
        gameCounter = 1
    else:# Custom message after a game to give choice
        print("Hope you enjoyed that game, if you're ready to play again type 'Game on'" + "\n" + "If you're done playing, type 'Goodbye'")
    choice = input("Whatcha want to do? :")
    if choice == "Goodbye": #Break condition
        print("Hope you had fun playing!")
        break
    elif choice != "Goodbye" and choice != "Game on": #Catches invalid strings
        print("I'm sorry, try typing your answer again.")
    elif choice == "Game on": #Opens game options menu
        gameEnd = False
        while gameEnd == False: #Game loop
            gameChoice = input("What game would you like to play?" + "\n" + "Type TTT to play Tic Tac Toe or Type T2 to play it squared! :")
            if gameChoice == "TTT":#Plays tic tac toe
                winner = ticTacToe()
                if winner == "Draw": #No draws allowed, someone needs to win
                    print("Can't end on a draw, so onto our tie breaker")
                    winner = rockPaperScissors()
                    if winner == "X": #Winner statements
                        print("X wins!")
                    else:
                        print("O wins!")
                gameEnd = True
                
            elif gameChoice != "TTT" and choice != "T2": #Covers errors
                print("I'm sorry, try typing what game you want to again.")

            elif gameChoice == "T2": #Plays Tic Tac Toe Squared
                winner = ticTacToeSquared()
                if winner == "Draw": #Same as last, no draws allowed
                    print("Can't end on a draw, so onto our tie breaker")
                    winner = rockPaperScissors()
                    if winner == "X":
                        print("X wins!")
                    else:
                        print("O wins!")
                gameEnd = True


                

        





