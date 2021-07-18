#initializing 3 different Lists

#black 1 white 2 in array
#          1 2 3 4 5 6 7 8 9   
row0 =  [3,3,3,3,3,3,3,3,3,3,3] #
row1 =  [3,1,1,1,1,1,0,0,0,0,3] #9
row2 =  [3,0,0,0,1,0,0,0,0,0,3] #18
row3 =  [3,1,1,1,0,1,0,0,0,0,3] #27
row4 =  [3,0,0,0,1,0,0,0,0,0,3] #36
row5 =  [3,0,0,0,0,0,0,0,0,0,3] #45
row6 =  [3,0,2,2,2,2,0,0,0,0,3] #54
row7 =  [3,0,2,0,0,2,0,0,0,0,3] #63
row8 =  [3,0,0,2,2,0,0,0,0,0,3] #72
row9 =  [3,0,2,0,0,2,0,0,0,0,3] #81
row10 = [3,3,3,3,3,3,3,3,3,3,3]

col = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]

checked1 = []
colour7 = 0
points = 0
myColour = 0
notMyColour = 0

#calculates the final score
def finalScore(myList=[], *args):

    check = []
    check1 = []
    empty_size = 0
    whiteScore = 0
    blackScore = 0
    global myColour
    global notMyColour


    global colour7
    global points

    for x in range(11):
        for y in range(11):
            if col[y][x] == 0:
                if (y*9-9+x) not in check1:
                    pieceCovered(x,y,check,myList)
                    myColour = 0
                    notMyColour = 0

                    if colour7 == 1:
                        blackScore = blackScore + points
                    elif colour7 == 2:
                        whiteScore = whiteScore + points
                    colour7 = 0
                    points = 0
                    check1.extend(check)
                    check.clear()

            elif col[y][x] == 1:
                blackScore += 1
                check1.append((y)*9-9+(x))

            elif col[y][x] == 2:
                whiteScore += 1
                check1.append(y*9-9+x)

            
   # whiteScore = whiteScore + 7.5
    print("Black:" + str(blackScore) + " White:"+ str(whiteScore))
    return ([blackScore, whiteScore])

#used in calculating the final score
def pieceCovered(x,y,check,myList = [], *args):
    
    global colour7 
    global points
    global myColour
    global notMyColour

    colour = myList[y][x]
 
    check.append(y*9-9+x)
    points = points + 1

    count = [0,1,2,3]

    xdir = [1,-1,0,0]
    ydir = [0,0,1,-1]
    
    
    for i in count:
        
        if myList[y+ydir[i]][x+xdir[i]] == 1:
            if myColour == 0:
                myColour = 1
                notMyColour = 2
                colour7 = 1
            elif myColour == 1:
                pass
            elif myColour == 2:
                points = 0    
                return(int(0))
        elif myList[y+ydir[i]][x+xdir[i]] == 2:
            if myColour == 0:
                myColour = 2
                notMyColour = 1
                colour7 = 2
            elif myColour == 2:
                pass
            elif myColour == 1: 
                points = 0  
                return(int(0))

        elif myList[y+ydir[i]][x+xdir[i]] == 0:
           # if it is the same
            if ((y+ydir[i])*9-9+(x+xdir[i])) not in check:
                # if we have not checked it yet
                if pieceCovered(x+xdir[i],y+ydir[i],check,myList) == 0:
                    points = 0
                    return(int(0))

# colour is the colour you're trying to capture, xloc, yloc of added piece
def pieceCaptured(x,y,checked,myList = [], *args):
    
    colour = myList[y][x]
 
    checked.append(y*9-9+x)
    
    count = [0,1,2,3]

    xdir = [1,-1,0,0]
    ydir = [0,0,1,-1]
    
    
    for i in count:
        
        if myList[y+ydir[i]][x+xdir[i]] == 0:
            checked.clear()
            return("empty")

        elif myList[y+ydir[i]][x+xdir[i]] == colour:
           # if it is the same
            if ((y+ydir[i])*9-9+(x+xdir[i])) not in checked:
                # if we have not checked it yet
                if pieceCaptured(x+xdir[i],y+ydir[i],checked,myList) == "empty":
                    checked.clear()
                    return("empty")

    return(checked)

def addPiece(location, colour ,myList = [], *args):
    loc_float = float(location)
    loc_x = int(loc_float)
    loc_y = int((loc_float - loc_x) * 10.1)

    myList[loc_y][loc_x] = colour
    print(myList)

def removePiece(location ,myList = [], *args):
    loc_float = float(location)
    loc_x = int(loc_float)
    loc_y1 = ((loc_float - loc_x) * 10.1)
    loc_y = int(loc_y1)

    myList[loc_y][loc_x] = 0
   # print(myList[loc_y][loc_x])

def checkPeice(loc,checked,myList = [], *args):

    loc_float = float(loc)
    x = int(loc_float)
    yf = ((loc_float-x)*10.1)
    y = int(yf)

    count = [0,1,2,3]
    PiecestobeRemoved = ""
    #arrays to add to x and y direction
    xdir = [1,-1,0,0]
    ydir = [0,0,1,-1]
    
    colour = myList[y][x]

    for i in count:

        if myList[y+ydir[i]][x+xdir[i]] == colour:
            pass
        elif (myList[y+ydir[i]][x+xdir[i]] == 0) or (myList[y+ydir[i]][x+xdir[i]] == 3):
            pass
        else:
            #check if the pieces need to be removed sourounding this piece
            piecesNeedRemoved = pieceCaptured(x+xdir[i],y+ydir[i], checked, myList)
            if piecesNeedRemoved == (None or 'empty'):
                pass
            else:
                for j in piecesNeedRemoved:
                    #if rgw do need to be removed get into proper format and then remove piece
                     yloc = int((j-1)/9+1)
                     xloc = (int(((j-1)/9+1-yloc)*10))+1
                     formatPiece = str(xloc) + "." + str(yloc)
                     removePiece(formatPiece, myList)
                     formatPiece = "R" + formatPiece
                     PiecestobeRemoved = PiecestobeRemoved + formatPiece
    
    #check if the piece that was added needs to be removed
    thisPieceRemoved = pieceCaptured(x,y,checked,myList)
    if thisPieceRemoved == (None or 'empty'):
        pass
    else:
        for j in thisPieceRemoved:
            yloc = int((j-1)/9+1)
            xloc = (int(((j-1)/9+1-yloc)*10))+1
            formatPiece = str(xloc) + "." + str(yloc)
            removePiece(formatPiece, myList)
            formatPiece = "R" +formatPiece
            PiecestobeRemoved = PiecestobeRemoved + formatPiece


    return(PiecestobeRemoved)


#print(pieceCaptured(5,5,col))
#addPiece("9.1",1, col)
# addPiece("5.4",1, col)
# addPiece("1.1",2, col)
# addPiece("5.6",1, col)
# addPiece("1.2",2, col)
# addPiece("6.5",1, col)
# addPiece("1.3",2, col)
# addPiece("4.5",1, col)
#print(checkPeice("9.1",checked1,col))

# addPiece("1.4",2, col)
# addPiece("1.5",1, col)

# #removePiece("1.9",col)
# print(checkPeice("9.9",checked2,col))
# print(col)

print (finalScore(col))