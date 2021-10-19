import threading

#worker function in which the printing happens

def worker(number):
    print("Hello world: {}".format(number))


number = 0  #initialize number

#for loop to start 4 threads

for i in range(4): 
    number += 1
    thread = threading.Thread(target = worker, args =(number,)) #starts new thread
    thread.start() #starts the worker