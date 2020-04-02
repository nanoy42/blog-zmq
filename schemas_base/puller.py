import zmq
import time
import random

context = zmq.Context()
puller = context.socket(zmq.PULL)

puller.connect("tcp://localhost:5555")


while True:
    print(puller.recv_string())
    time.sleep(random.randint(1,5)) # execute la tache
    print("Task done")
