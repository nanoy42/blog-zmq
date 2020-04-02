import zmq


class Logger:
    def __init__(self, log_level):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.log_level = log_level

    def connect(self):
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")
        self.socket.connect("tcp://localhost:5556")

    def start(self):
        while True:
            msg = self.socket.recv()
            print(msg)


if __name__ == "__main__":
    logger = Logger(3)
    logger.connect()
    logger.start()
