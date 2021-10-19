import threading

class MyThread(threading.Thread):
  #class initializer
  def __init__(self, number):
    super().__init__()
    self.number = number

  #print the thread count
  def run(self):
    print('Hello world: {}'.format(number))

if __name__ == '__main__':
  number = 0 #initialize number
  for i in range(4): #for loop to start 4 threads
    number += 1
    thread = MyThread(number) #init new thread
    thread.start() #start a thread