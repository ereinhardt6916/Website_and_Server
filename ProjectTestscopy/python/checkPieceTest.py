#initializing 3 different Lists

# White = 1,  Black = 2
#          1 2 3 4 5 6 7 8 9   
row0 =  [3,3,3,3,3,3,3,3,3,3,3] #
row1 =  [3,0,0,0,0,0,0,0,0,0,3] #9
row2 =  [3,0,0,0,0,0,0,0,0,0,3] #18
row3 =  [3,0,0,0,1,1,0,0,0,0,3] #27
row4 =  [3,0,0,1,2,2,1,0,0,0,3] #36
row5 =  [3,0,0,2,1,1,2,0,0,0,3] #45
row6 =  [3,0,0,2,1,1,2,0,0,0,3] #54
row7 =  [3,0,0,0,2,2,0,0,0,0,3] #63
row8 =  [3,0,0,0,0,0,0,0,0,0,3] #72
row9 =  [3,0,0,0,0,0,0,0,0,0,3] #81
row10 = [3,3,3,3,3,3,3,3,3,3,3]

col = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]

checked = []

# colour is the colour you're trying to capture, xloc, yloc of added piece
def pieceCaptured(x,y,myList = [], *args):
    
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
                if pieceCaptured(x+xdir[i],y+ydir[i],myList) == "empty":
                    checked.clear()
                    return("empty")

    return(checked)

def addPiece(location, colour ,myList = [], *args):
    loc_float = float(location)
    loc_x = int(loc_float)
    loc_y = int((loc_float - loc_x) * 10.1)

    myList[loc_y][loc_x] = colour
    print(myList[loc_y][loc_x])

def removePiece(location ,myList = [], *args):
    loc_float = float(location)
    loc_x = int(loc_float)
    loc_y1 = ((loc_float - loc_x) * 10.1)
    loc_y = int(loc_y1)

    myList[loc_y][loc_x] = 0
   # print(myList[loc_y][loc_x])

def checkPeice(x,y,myList = [], *args):

    count = [0,1,2,3]

    #arrays to add to x and y direction
    xdir = [1,-1,0,0]
    ydir = [0,0,1,-1]
    
    colour = myList[y][x]

    for i in count:

        if myList[y+ydir[i]][x+xdir[i]] == colour:
            pass
        elif myList[y+ydir[i]][x+xdir[i]] == 0:
            pass
        else:
            #check if the pieces need to be removed sourounding this piece
            piecesNeedRemoved = pieceCaptured(x+xdir[i],y+ydir[i], myList)
            if piecesNeedRemoved == (None or 'empty'):
                pass
            else:
                for j in piecesNeedRemoved:
                    #if rgw do need to be removed get into proper format and then remove piece
                     yloc = int((j-1)/9+1)
                     xloc = (int(((j-1)/9+1-yloc)*10))+1
                     formatPeice = str(xloc) + "." + str(yloc)
                     removePiece(formatPeice, myList)
    
    #check if the piece that was added needs to be removed
    thisPieceRemoved = pieceCaptured(x,y,myList)
    if thisPieceRemoved == (None or 'empty'):
        pass
    else:
        for j in thisPieceRemoved:
            yloc = int((j-1)/9+1)
            xloc = (int(((j-1)/9+1-yloc)*10))+1
            formatPeice = str(xloc) + "." + str(yloc)
            removePiece(formatPeice, myList)

#print(pieceCaptured(5,5,col))
#addPiece("1.9", 1, col)
#removePiece("1.9",col)
checkPeice(4,4,col)
print(col)