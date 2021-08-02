from watchdog_server import Watchdog_server

watchdog = Watchdog_server()

def checkConnectionFlags():
    if not watchdog.isPConnected():
        raise Exception("Physical Board Connection Lost")
    elif not watchdog.isVConnected():
        raise Exception("Physical Board Connection Lost")