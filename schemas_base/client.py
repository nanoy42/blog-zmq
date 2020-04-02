import zmq

context = zmq.Context()
request = context.socket(zmq.REQ)

request.connect("tcp://localhost:5555")

request.send(b"Hello")

message = request.recv()
print(message)
