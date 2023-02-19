#Gravino, Andrew
#CS4200, Assignment 1
#2/22/23


queen0 = [-1, -1]
queen1 = [-1, -2]
queen2 = [-1, -1]
queen3 = [-3, -1]
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

temporaryListOfQueenPositions = [queen0, queen1, queen2, queen3, queen4, queen5, queen6, queen7] 

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
                if temporaryListOfQueenPositions.has([yIterator, xIterator]): #we check to see if it would be unique adding it into the list
                    pass #if we notice the same tuple, then we don't add that new queen
                temporaryListOfQueenPositions.append([yIterator, xIterator]) #to get here means that it was totally unique and now we will be adding it into the list

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
    #print("the function was called")
    for i in range(0, len(temporaryListOfQueenPositions)):
        print(temporaryListOfQueenPositions[i])
        y2 = temporaryListOfQueenPositions[i][1]
        print("we are checking the passed", y1, "against queen's", y2)
        if y2 == y1: #if it shares a y-value. that isnt allowed
            print("false")
            return False
    print("true")
    return True #getting to this point means that allllll of the queens were checked and we were good since it would return false if we were wrong

def checkHorizontally(x1):
    print("the function was called")
    for i in range(0, len(temporaryListOfQueenPositions)):
        print(temporaryListOfQueenPositions[i])
        x2 = temporaryListOfQueenPositions[i][0]
        print("we are checking the passed", x1, "against queen's", x2)
        if x2 == x1: #if it shares an x-value, that isnt allowed
            print("false")
            return False        
    print("true")
    return True #getting to this point means that all the queens were checked and we were good or else it would give us a false

def checkDiagonally(x1, y1):
    print("the function was called")
    for i in range(0, len(temporaryListOfQueenPositions)):
        print(temporaryListOfQueenPositions[i])
        x2 = temporaryListOfQueenPositions[i][0]
        y2 = temporaryListOfQueenPositions[i][1]
        print("we are checking the passed", x1, "and", y1, "against queen's", x2, "and", y2)
        mValue = (y2 - y1)/(x2 - x1)
        print("here is their slope value m:", mValue)
        if(mValue == 1 or mValue == -1): #perfect diagonals have a slope value of -1 or 1
            print("false")
            return False
    print("true")
    return True #you can only get here if all the diagonals were checked and we see none of them had a slope of -1 or 1

def checkAllDirections(x1, y1):
    #print("we're checking", x1, "and", y1)
    if checkVertically(y1) == True and checkHorizontally(x1) == True and checkDiagonally(x1, y1) == True:
        print("we good")
        return True

    else:
        print("we not good yet")

def main():
    #print("Showing what the board currently looks like")
    #displayBoard()
    #checkVertically(-2)
    #checkHorizontally(-2)
    checkDiagonally(3, 7)
    #print("Now we will add the found queens coordinates to a tuple list")
    #addQueensPositionToList()
    #print(temporaryListOfQueenPositions)
    #print("Now we will check the directions to see if we're good")   

    #placeQueens()
    

main()    
#we'll need a way to verify things on a coordinate basis if anything is detectable diagonally, horizontally, or vertically
#perhaps that can be solved by an equation of rise over run?
#if the piece is directly above or below, that means the slope is going to be positive or negative infinite being directly above or below
#if the piece is diagonal, that means the slope is going to be 1 or -1
#if the piece is horizontally to the sides, that means the slope is going to be 0
#we can do a thing where a queen will check the slope of it against every queen so long as the other queens have a valid set of coordinate



#a valid set of coordinates for checking when the queens are actually "placed" is by checking like if the coordinates are negative or positive since there is no negative in an 8 by 8 chess board, going from 0 to 7