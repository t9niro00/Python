import threading
import time


val = 0
lock = threading.Lock()

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target = t, args = args)
        self.start() #start the thread


def increment():
    global val
    print(threading.currentThread()) #print the current thread


    try:
        lock.acquire() #acquire the lock
        print('lock acquired')
        val += 1 #add 1 to increment
        print('Hello world: {}'.format(val)) #print the current increment
        time.sleep(0.4) #sleep for a little so that the threading is easier to read

    finally: 
        lock.release() #release the lock
        print('lock released')

def hello_world():
    while val < 7:
        increment() #run the increment function while val is smaller than 7

#main function that starts the two threads run the same function
def main():
    for i in range(2):
        thread = Thread(hello_world)

if __name__ == '__main__':
    main() #run the main function
