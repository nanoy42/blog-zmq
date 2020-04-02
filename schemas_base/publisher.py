import zmq
import time

context = zmq.Context()
publisher = context.socket(zmq.PUB)

publisher.bind("tcp://*:5555")

time.sleep(0.11) # regle le probleme des slow joiners
for i in range(5):
    publisher.send(b'Hello everyone. This is message %i' % i)
    time.sleep(2)
