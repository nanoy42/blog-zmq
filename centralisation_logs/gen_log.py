import zmq
import random
import time
import argparse


class Log:
    def __init__(self, name):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.name = name

    def connect(self):
        self.socket.connect("tcp://localhost:5555")

    def start(self):
        while True:
            level, log = self.get_log()
            self.socket.send(log)
            time.sleep(random.randint(0, 5))

    def get_log(self):
        return (1, b"Test" + self.name.encode())

    def stop(self):
        self.socket.close()
        self.context.term()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="name of the generator of log")
    args = parser.parse_args()

    log = Log(args.name)
    log.connect()
    log.start()
