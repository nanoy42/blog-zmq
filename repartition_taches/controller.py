import zmq
import random
import msgpack
import math
import time


class Controller:

    MIN_VALUE = -10
    MAX_VALUE = 40
    TASK_MAX_SIZE = 1000

    def __init__(self, n):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        self.temperatures = [
            random.randint(self.MIN_VALUE, self.MAX_VALUE) for i in range(n)
        ]
        self.threshold = random.randint(self.MIN_VALUE, self.MAX_VALUE)

    def connect(self):
        self.socket.bind("tcp://*:5555")
        time.sleep(0.2)

    def send_tasks(self):
        n = math.ceil(len(self.temperatures) / self.TASK_MAX_SIZE)
        tasks = [self.temperatures[i::n] for i in range(n)]
        for task in tasks:
            self.socket.send(msgpack.packb({"threshold": self.threshold, "task": task}))

        print(
            "%i temperatures to analyse. Limit is %i. %i tasks sent."
            % (len(self.temperatures), self.threshold, len(tasks))
        )


if __name__ == "__main__":
    controller = Controller(25000)
    controller.connect()
    controller.send_tasks()
