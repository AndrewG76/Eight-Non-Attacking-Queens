#Gravino, Andrew
#CS4200, Assignment 1
#2/22/23
import math

boardDisplay = [[1, 0, 0, 0, 0, 0, 0, 0], #this will be used to draw out where the queens will be and what the board will look like
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0],       
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0]]

temporaryListOfQueenPositions = [[0,0]] #the coordinates will be y, x because we go row by row and then by each column

def displayBoard():
    #this will be used to print the final layout of how the board will look and we can use it generally to figure out what our list looks at any specific time
    for row in boardDisplay: 
        print(row)

def addQueensPositionToList(): #function that lets us take note of all the positions where there is a queen
    yIterator = 0
    xIterator = 0 #initialize out iterators
    for row in boardDisplay:
        xIterator = 0 #at every new row, the column iterator goes back to 0
        for col in row:
            if col == 1: #then look for the places on the board where the piece is equal to 1 as that is where a queen has been placed.
                if temporaryListOfQueenPositions.__contains__([yIterator, xIterator]) == False: #we check to see if it would be unique adding it into the list
                    temporaryListOfQueenPositions.append([yIterator, xIterator])
            xIterator += 1 #at every column in the row, the xIterator goes up by 1
        yIterator += 1 #once we're done iterating through each column in the row, the yIterator goes up by 1 to the next
    print(temporaryListOfQueenPositions)

def checkAllDirections(y1, x1): #this is gonna be autocalled by the placeQueens function checking
    #print("the function was called")
    for i in range(0, len(temporaryListOfQueenPositions)):
        #print(temporaryListOfQueenPositions[i])
        y2 = temporaryListOfQueenPositions[i][0] #the y-coordinate is handled by the first value in the individual list
        x2 = temporaryListOfQueenPositions[i][1] #the x-coordinate it handled by the second value in the individual list
        #print("we are checking the passed", y1, "and", x1, "against queen's", y2, "and", x2)
        if abs(x1 - x2) == 0 or abs(x2 - x1) == 0: #we need this to stop it early or else we'll end up creating a division by zero error
            #and worst that happens, this means that the other queen detected was directly above it which is why the slope isn't 0 but instead would be infinity upwards
            #print("false, vertically spotted") 
            return False
        else:
            mValue = (y2 - y1)/(x2 - x1)
        if(mValue == 1 or mValue == -1): #perfect diagonals have a slope value of -1 or 1
            #print("false, diagonally spotted")
            return False
        if(mValue == 0 or mValue == -0): #then this one exists because if slope is 0, then that means it's horizontally related to it
            #print("false, horizontally spotted")
            return False
        if(x1 == x2):
            #print("false, vertically spotted")
            return False
        if(y1 == y2):
            #print("false, horizontally spotted")
            return False
    print("true")
    #print("here is their slope value m:", mValue)
    return True #you can only get here if all the diagonals, verticals, and horizontals were checked and we see none of them had a slope of -1, 1, 0, or was about to divide by 0

def placeQueens():
    for i in range(0, len(boardDisplay)):
        for j in range(0, len(boardDisplay[i])):
            if checkAllDirections(i, j) == True: #we first check to see if there's any other queen in a diagonal, vertical, or horizontal manner
                boardDisplay[i][j] = 1 #if nothing comes up and we're good, we are allowed to place a queen there 
                addQueensPositionToList() #then we call this function to update whenever we have a new queen placed
                print("we found a valid spot so here's what it looks like")
                displayBoard()
    print("after running through every iteration, here's how our final board looks")
    displayBoard()

def checkNumberOfQueens():
    if len(temporaryListOfQueenPositions) != 8:
        temporaryListOfQueenPositions[len(temporaryListOfQueenPositions) - 1][0] += 1 #this grabs the last item in the list and pulls the y-coordinate from that respective queen's coordinates to try again

def main():
    #print("Showing what the board currently looks like")
    #displayBoard()
    #checkVertically(-2)
    #checkHorizontally(-2)
    #checkAllDirections(4, 5)
    #print("Now we will add the found queens coordinates to a tuple list")
    #addQueensPositionToList()
    #print(temporaryListOfQueenPositions)
    #print("Now we will check the directions to see if we're good")   
    placeQueens()
    

main()    
#we'll need a way to verify things on a coordinate basis if anything is detectable diagonally, horizontally, or vertically
#perhaps that can be solved by an equation of rise over run?
#if the piece is directly above or below, that means the slope is going to be positive or negative infinite being directly above or below
#if the piece is diagonal, that means the slope is going to be 1 or -1
#if the piece is horizontally to the sides, that means the slope is going to be 0
#we can do a thing where a queen will check the slope of it against every queen so long as the other queens have a valid set of coordinate



#a valid set of coordinates for checking when the queens are actually "placed" is by checking like if the coordinates are negative or positive since there is no negative in an 8 by 8 chess board, going from 0 to 7