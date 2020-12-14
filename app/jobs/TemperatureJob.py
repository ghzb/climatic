import time
import threading
import app.providers.TemperatureServiceProvider as Service

stop_threads = False


def thread_func():
    """ Count half seconds"""
    while True:
        global stop_threads
        
        Service.run()
        time.sleep(0.5)
        
        if stop_threads: 
            break

thread = threading.Thread(target = thread_func)

def make(schedule):
    schedule.every().minutes.do(Service.insert)
    thread.start()

def destroy():
    global stop_threads
    stop_threads = True
    thread.join()