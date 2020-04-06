import argparse

import msgpack
import zmq


class Finalizer:
    def __init__(self, n):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.expected = n
        self.received = 0
        self.result = 0

    def connect(self):
        self.socket.bind("tcp://*:5556")

    def start(self):
        while self.expected != self.received:
            msg = self.socket.recv()
            response = msgpack.unpackb(msg)
            self.received += response["size"]
            self.result += response["result"]

        print(
            "On %i temperatures, %i were above the limit."
            % (self.received, self.result)
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="number of temperatures")
    args = parser.parse_args()

    finalizer = Finalizer(int(args.n))
    finalizer.connect()
    finalizer.start()
