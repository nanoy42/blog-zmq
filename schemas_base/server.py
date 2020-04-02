import zmq

context = zmq.Context()
reply = context.socket(zmq.REP)

reply.bind("tcp://*:5555")

message = reply.recv()
print(message)

if message == b'Hello':
    reply.send(b'World !')

