def startup(socket1, socket2):
    
    #read response from socket1
    socket1.s_appept()
    colour1 = socket1.read_data()
    print ("Reading S1:" + colour1.decode("utf-8") )
    
    #read response from socket2
    socket2.s_appept()
    colour2 = socket2.read_data()
    print ("Reading S2:" + colour2.decode("utf-8") )
    
    if (colour1 == colour2) or (colour1 == b"Blac"):

        print("Writing S1:" + b"0000Blac".decode("utf-8") )
        socket1.send_data(b"0000Blac")

        print("Writing S2:" + b"1111Whit".decode("utf-8") )
        socket2.send_data(b"1111Whit")

        socket2.s_appept()
        colour2 = socket2.read_data()
        print ("Reading S2:" + colour2.decode("utf-8") )

        colour1 = b"Blac"

    elif colour1 == b"Whit":

        print("Writing S1:" + b"1111Whit".decode("utf-8") )
        socket1.send_data(b"1111Whit")

        
        print("Writing S2:" + b"0000Blac".decode("utf-8") )
        socket2.send_data(b"0000Blac")

        socket1.s_appept()
        colour1 = socket1.read_data()
        print ("Reading S1:" + colour1.decode("utf-8") )


    return colour1


def player1first(socket1, socket2, i):

    if i == b"!sur":

        #reading peice place
        socket1.s_appept()
        location1 = socket1.read_data()
        print ("Reading S1:" + location1.decode("utf-8") )

        #writing End Sequence
        print("Writing S1:" + i.decode("utf-8") )
        socket1.send_data(i) 

        #void
        socket1.s_appept()
        print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )


        #writing End Sequence
        print("Writing S2:" + i.decode("utf-8") )
        socket2.send_data(i) 

        #void
        socket2.s_appept()
        location2 = socket2.read_data()
        print ("Reading S2:" + location2.decode("utf-8") )

        #writing score
        print("Writing S2:" + b"W010B005".decode("utf-8") )
        socket2.send_data(b"W010B005") 

        #void
        socket1.s_appept()
        print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )


        #writing location
        print("Writing S1:" + b"W010B005".decode("utf-8") )
        socket1.send_data(b"W010B005") 


    else:
        #reading peice place
        socket1.s_appept()
        location1 = socket1.read_data()
        print ("Reading S1:" + location1.decode("utf-8") )
        
        #writing score
        print("Writing S1:" + i.decode("utf-8") )
        socket1.send_data(i) 
        
        #void
        socket1.s_appept()
        print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )



        #writing location
        location1 = bytes(("A"+location1.decode("utf-8")),"utf-8")
        print("Writing S2:" + location1.decode("utf-8") )
        socket2.send_data(location1) 

        #reading peice place
        socket2.s_appept()
        location2 = socket2.read_data()
        print ("Reading S2:" + location2.decode("utf-8") )

        #writing score
        print("Writing S2:" + i.decode("utf-8") )
        socket2.send_data(i) 

        #void
        socket2.s_appept()
        print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )


        #writing location
        location2 = bytes(("A"+location2.decode("utf-8")),"utf-8")
        print("Writing S1:" + location2.decode("utf-8") )
        socket1.send_data(location2) 

    return


def player2first(socket1, socket2, i):

    if i == b"!sur":

        #reading peice place
        socket2.s_appept()
        location2 = socket2.read_data()
        print ("Reading S2:" + location2.decode("utf-8") )

        #writing End Sequence
        print("Writing S2:" + i.decode("utf-8") )
        socket2.send_data(i) 

        #void
        socket2.s_appept()
        print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )


        #writing End Sequence
        print("Writing S1:" + i.decode("utf-8") )
        socket1.send_data(i) 

        #void
        socket1.s_appept()
        location1 = socket1.read_data()
        print ("Reading S1:" + location1.decode("utf-8") )

        #writing score
        print("Writing S1:" + b"W010B005".decode("utf-8") )
        socket1.send_data(b"W010B005") 

        #void
        socket2.s_appept()
        print ("Reading S1:" + (socket2.read_data()).decode("utf-8") )


        #writing location
        print("Writing S2:" + b"W010B005".decode("utf-8") )
        socket2.send_data(b"W010B005") 

    else:
        #reading peice place
        socket2.s_appept()
        location2 = socket2.read_data()
        print ("Reading S2:" + location2.decode("utf-8") )
        
        #writing score
        print("Writing S2:" + i.decode("utf-8") )
        socket2.send_data(i) 
        
        #void
        socket2.s_appept()
        print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )



        #writing location
        location2 = bytes(("A"+location2.decode("utf-8")),"utf-8")
        print("Writing S1:" + location2.decode("utf-8") )
        socket1.send_data(location2) 

        #reading peice place
        socket1.s_appept()
        location1 = socket1.read_data()
        print ("Reading S1:" + location1.decode("utf-8") )

        #writing score
        print("Writing S1:" + i.decode("utf-8") )
        socket1.send_data(i) 

        #void
        socket1.s_appept()
        print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )


        #writing location
        location1 = bytes(("A"+location1.decode("utf-8")),"utf-8")
        print("Writing S2:" + location1.decode("utf-8") )
        socket2.send_data(location1) 

    return
