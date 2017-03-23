# Credit: NewBoston Youtube vid

import threading

class Message(threading.Thread):
  def run(self):
    for _ in range(10):
      print(threading.currentThread().getName())

x = Message(name='Send out Messages')
y = Message(name='Receive Messages')
x.start()
y.start()
