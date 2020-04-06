import argparse
import math
import random
import time

import msgpack
import zmq


class Controller:

    MIN_VALUE = -10
    MAX_VALUE = 40

    def __init__(self, n, task_max_size):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        self.temperatures = [
            random.randint(self.MIN_VALUE, self.MAX_VALUE) for i in range(n)
        ]
        self.threshold = random.randint(self.MIN_VALUE, self.MAX_VALUE)
        self.task_max_size = task_max_size

    def connect(self):
        self.socket.bind("tcp://*:5555")
        time.sleep(0.2)

    def send_tasks(self):
        n = math.ceil(len(self.temperatures) / self.task_max_size)
        tasks = [self.temperatures[i::n] for i in range(n)]
        for task in tasks:
            self.socket.send(msgpack.packb({"threshold": self.threshold, "task": task}))

        print(
            "%i temperatures to analyse. Limit is %i. %i tasks sent."
            % (len(self.temperatures), self.threshold, len(tasks))
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="number of temperatures")
    parser.add_argument(
        "task_max_size", help="max number of temperatures to send in one task"
    )
    args = parser.parse_args()

    controller = Controller(int(args.n), int(args.task_max_size))
    controller.connect()
    controller.send_tasks()
