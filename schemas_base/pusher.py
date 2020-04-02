import zmq
import time

context = zmq.Context()
pusher = context.socket(zmq.PUSH)

pusher.bind("tcp://*:5555")

time.sleep(0.2) # slow joiners
for i in range(5):
    pusher.send(b'Hi worker. You have the task %i' % i)
    
