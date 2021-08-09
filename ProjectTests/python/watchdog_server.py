import socket
import logging
from threading import Thread, Lock
import os

class Watchdog_server:

    def __init__(self):
        # variables
        self.Psocket_host = "127.0.0.1"
        self.Vsocket_host = "127.0.0.1"
        self.Psocket_port = 10237
        self.Vsocket_port = 10238
        self.Pmutex = Lock()
        self.Vmutex = Lock()
        self.Pfail_flag = False
        self.Vfail_flag = False
        self.stop_flag = False
        
        # logging setup
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S") 

    def start(self):
        # start theads
        self.P_thread = Thread(target=self.__Pwatchdog_start, daemon=True)
        # self.V_thread = Thread(target=self.__Vwatchdog_start, daemon=True)
        self.P_thread.start()
        # self.V_thread.start()

    def stop(self):
        self.stop_flag = True
        self.P_thread.join()
        # self.V_thread.join()
    
    def isPConnected(self):
        self.Pmutex.acquire()
        result = self.Pfail_flag
        self.Pmutex.release()
        return (not result)
    
    def isVConnected(self):
        self.Vmutex.acquire()
        result = self.Vfail_flag
        self.Vmutex.release()
        return (not result)

    def __Pwatchdog_start(self):
        self.Psocket = self.SocketHelper(self.Psocket_host, self.Psocket_port)
        logging.info("[P]Watchdog for physical board started")
        failure_counter = 0
        # expect to receive 0 from Psocket
        # if both fail flags are false, reply 0, otherwise reply 1

        while not self.stop_flag:
            try:
                result = self.Psocket.read_data()
                self.Psocket.set_timeout(3)
                if result == 1:
                    # fail to receive data, increment failure counter
                    failure_counter += 1
                    if failure_counter >= 3:
                        self.Pmutex.acquire()
                        self.Pfail_flag = True
                        self.Pmutex.release()
                        break
                elif result == 0:
                        self.Vmutex.acquire()
                        if self.Vfail_flag:
                            # visual side disconnected
                            reply_msg = 1
                        else:
                            # everything is normal
                            failure_counter = 0
                            reply_msg = 0
                        self.Vmutex.release()
                        self.Psocket.send_data(reply_msg)

                self.Vmutex.acquire()
                self.Pmutex.acquire()
                logging.info(f"[P]Received: {result} failure_counter: {failure_counter} Pflag: {self.Pfail_flag} Vflag: {self.Vfail_flag}")
                self.Pmutex.release()
                self.Vmutex.release()
            except Exception as e:
                logging.info("[P]"+str(e))
                # any error will conclude to Psocket failure
                self.Pmutex.acquire()
                self.Pfail_flag = True
                self.Pmutex.release()
                break
        
        logging.info("[P]Physical board connection lost")
        self.Psocket.close_socket()
        os.system("pkill python")
    

    def __Vwatchdog_start(self):
        self.Vsocket = self.SocketHelper(self.Vsocket_host, self.Vsocket_port)
        logging.info("[V]Watchdog for virtual board started")
        failure_counter = 0
        # expect to receive 0 from Vsocket
        # if both fail flags are false, reply 0, otherwise reply 1

        while not self.stop_flag:
            try:
                result = self.Vsocket.read_data()
                self.Vsocket.set_timeout(3)
                if result == 1:
                    # fail to receive data, increment failure counter
                    failure_counter += 1
                    if failure_counter >= 3:
                        self.Vmutex.acquire()
                        self.Vfail_flag = True
                        self.Vmutex.release()
                        break
                elif result == 0:
                        self.Pmutex.acquire()
                        if self.Pfail_flag:
                            # physical side disconnected
                            reply_msg = 1
                        else:
                            # everything is normal
                            failure_counter = 0
                            reply_msg = 0
                        self.Pmutex.release()
                        self.Vsocket.send_data(reply_msg)

                self.Pmutex.acquire()
                self.Vmutex.acquire()
                logging.info(f"[V]Received: {result} failure_counter: {failure_counter} Pflag: {self.Pfail_flag} Vflag: {self.Vfail_flag}")
                self.Vmutex.release()
                self.Pmutex.release()
            except Exception as e:
                logging.info("[V]"+str(e))
                # any error will conclude to Vsocket failure
                self.Vmutex.acquire()
                self.Vfail_flag = True
                self.Vmutex.release()
                break
        
        logging.info("[P]Virtual board connection lost")
        self.Vsocket.close_socket()


    class SocketHelper:
        def __init__(self, host, port):
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.bind((host, port))
            self.s.listen(5)
            self.conn, self.addr = self.s.accept()
        
        def set_timeout(self, timeout):
            self.s.settimeout(timeout)
        
        def send_data(self, content):
            self.conn.send(bytes(str(content), "utf-8"))

        def read_data(self):
            try:
                buf = self.conn.recv(1024)
                return int(buf.decode("utf-8"))
            except:
                # 1 means connection fail
                return 1
        
        def close_socket(self):
            self.conn.close()
            self.s.close()