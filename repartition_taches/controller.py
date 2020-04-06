# Blog ZMQ source code
# Copyright (C) 2020 Yoann Pietri

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
