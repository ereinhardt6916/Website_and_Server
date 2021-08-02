#https://github.com/Net4ky/PPsocket

import time
from shelper import SocketHelper
from comm_functions import startup
from comm_functions import player1first
from comm_functions import player2first
from watchdog_server import Watchdog_server

port1 = 10231
port2 = 10236
host2 = "127.0.0.1"
host1 = "localhost"

while True:
    try:
        #************************setup***********************************************************
        socket1 = SocketHelper(host1,port1)
        socket2 = SocketHelper(host2,port2)

        watchdog = Watchdog_server()
        watchdog.start()

        player1colour = startup(socket1, socket2)

        

        # b needed because we can only sen bytes object in python, need to decode it to get a string
        #mesg = [b"W001B050", b"!sur"] #b"W004B050",b"W005B050.9",b"W006B050",b"W007B070",b"W008B080",b"W009B090.9",b"W0010B010",

        if player1colour == b"Blac":
            while True:
                x = player1first(socket1, socket2)
                if x == "end":
                    break
                elif x == "FAIL":
                    print("Connection Failed")
                    break
        elif player1colour == "FAIL":
            print("Connection Failed")
        else:
            while True:
                x =  player2first(socket1, socket2)
                if x == "end":
                    break
                elif x == "FAIL":
                    print("Connection Failed")
                    break
    except Exception as e:
        print(e)
    finally:
        try:
            socket1.close_socket()
            socket2.close_socket()
            watchdog.stop()
            time.sleep(1)
        except:
            pass
    

