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
[0, 0, 0, 0, 0, 0, 0, 1], 
[0, 0, 1, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 0, 0, 1, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0]]

temporaryListOfQueenPositions = []

def displayBoard():
    #this will be used to print the final layout of how the board will look and we can use it generally to figure out what our list looks at any specific time
    for row in boardDisplay: 
        print(row)

def checkVertically(y1, x1): #our passed variables are the current iterated spot's x and y coordinates
    #initialize the x and y positions of coordinate 2
    y2 = -1
    x2 = -1
    yIterator = 0
    xIterator = 0 #initialize out iterators
    for row in boardDisplay:
        yIterator += 1
        xIterator = 0 #at every new row, the x goes back to 0 
        for col in row:
            xIterator += 1
            if row[col] == 1: #then look for the places on the board where the piece is equal to 1 as that is where a queen has been placed.
                temporaryListOfQueenPositions.append([xIterator, yIterator])
                

def checkHorizontally():
    pass

def checkDiagonally():
    pass

def main():
    print("omg SLAYYYYY")
    displayBoard()
    print("hiiii")
    checkVertically(2, 4)       
    print(temporaryListOfQueenPositions)

main()    
#we'll need a way to verify things on a coordinate basis if anything is detectable diagonally, horizontally, or vertically
#perhaps that can be solved by an equation of rise over run?
#if the piece is directly above or below, that means the slope is going to be positive or negative infinite being directly above or below
#if the piece is diagonal, that means the slope is going to be 1 or -1
#if the piece is horizontally to the sides, that means the slope is going to be 0
#we can do a thing where a queen will check the slope of it against every queen so long as the other queens have a valid set of coordinate



#a valid set of coordinates for checking when the queens are actually "placed" is by checking like if the coordinates are negative or positive since there is no negative in an 8 by 8 chess board, going from 0 to 7