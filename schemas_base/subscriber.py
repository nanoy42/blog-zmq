import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)

subscriber.connect("tcp://localhost:5555")

subscriber.setsockopt_string(zmq.SUBSCRIBE, "") # on souscrit à tous les messages

while True:
    print(subscriber.recv_string())

