#Gravino, Andrew
#CS4200, Assignment 1
#2/22/23


queen0 = [-1, -1]
queen1 = [-1, -1]
queen2 = [-1, -1]
queen3 = [-1, -1]
queen4 = [-1, -1]
queen5 = [-1, -1]
queen6 = [-1, -1]
queen7 = [-1, -1]

boardDisplay = [[0, 0, 0, 0, 0, 0, 0, 0], #this will be used to draw out where the queens will be and what the board will look like
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0],       
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0]]

temporaryListOfQueenPositions = [] 

def displayBoard():
    #this will be used to print the final layout of how the board will look and we can use it generally to figure out what our list looks at any specific time
    for row in boardDisplay: 
        print(row)

def addQueensPositionToList(): #function that lets us take note of all the positions where there is a queen
    yIterator = 0
    xIterator = 0 #initialize out iterators
    for row in boardDisplay:
        yIterator += 1
        xIterator = 0 #at every new row, the x goes back to 0 
        for col in row:
            xIterator += 1
            if col == 1: #then look for the places on the board where the piece is equal to 1 as that is where a queen has been placed.
                temporaryListOfQueenPositions.append([yIterator, xIterator])

def placeQueens():
    for i in range(0, len(boardDisplay)):
        for j in range(0, len(boardDisplay[i])):
            if checkAllDirections(i, j) == True: #we first check to see if there's any other queen in a diagonal, vertical, or horizontal manner
                boardDisplay[i][j] = 1 #if nothing comes up and we're good, we are allowed to place a queen there 
                addQueensPositionToList() #then we call this function to update whenever we have a new queen placed
            
                


    '''
    for i in range(0, 7):
        print("meow", i)

    meow 0
    meow 1
    meow 2
    meow 3
    meow 4
    meow 5
    meow 6
    '''

def checkVertically(y1): #our passed variables are the current iterated spot's x and y coordinates
    for queen in temporaryListOfQueenPositions:
        y2 = queen[1]
        print("we are checking the passed", y1, "against queen's", y2)
        if y2 == y1: #if it shares a y-value. that isnt allowed
            return False #okay now what LOL
        else:
            return True

def checkHorizontally(x1):
    for queen in temporaryListOfQueenPositions:
        x2 = queen[0]
        if x2 == x1: #if it shares an x-value, that isnt allowed
            return False
        else:
            return True

def checkDiagonally(x1, y1):
    for queen in temporaryListOfQueenPositions:
        x2 = queen[0]
        y2 = queen[1]
        if((y2 - y1)/(x2 - x1) == 1 or (y2 - y1)/(x2 - x1) == -1): #perfect diagonals have a slope value of -1 or 1
            return False
        else:
            return True

def checkAllDirections(x1, y1):
    #print("we're checking", x1, "and", y1)
    if checkVertically(y1) == True and checkHorizontally(x1) == True and checkDiagonally(x1, y1) == True:
        print("we good")
        return True

    else:
        print("we not good yet")

def main():
    print("Showing what the board currently looks like")
    displayBoard()
    #print("Now we will add the found queens coordinates to a tuple list")
    #addQueensPositionToList()
    #print(temporaryListOfQueenPositions)
    print("Now we will check the directions to see if we're good")   

    #placeQueens()
    

main()    
#we'll need a way to verify things on a coordinate basis if anything is detectable diagonally, horizontally, or vertically
#perhaps that can be solved by an equation of rise over run?
#if the piece is directly above or below, that means the slope is going to be positive or negative infinite being directly above or below
#if the piece is diagonal, that means the slope is going to be 1 or -1
#if the piece is horizontally to the sides, that means the slope is going to be 0
#we can do a thing where a queen will check the slope of it against every queen so long as the other queens have a valid set of coordinate



#a valid set of coordinates for checking when the queens are actually "placed" is by checking like if the coordinates are negative or positive since there is no negative in an 8 by 8 chess board, going from 0 to 7