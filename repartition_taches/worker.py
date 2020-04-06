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

import msgpack
import zmq


class Worker:
    def __init__(self):
        self.context = zmq.Context()
        self.recv_socket = self.context.socket(zmq.PULL)
        self.send_socket = self.context.socket(zmq.PUSH)

    def connect(self):
        self.recv_socket.connect("tcp://localhost:5555")
        self.send_socket.connect("tcp://localhost:5556")

    def start(self):
        while True:
            msg = self.recv_socket.recv()
            task = msgpack.unpackb(msg)
            result = self.exectute_task(task)
            self.send_socket.send(
                msgpack.packb({"size": len(task["task"]), "result": result})
            )

    def exectute_task(self, task):
        res = 0
        threshold = task["threshold"]
        for value in task["task"]:
            if value > threshold:
                res += 1
        return res


if __name__ == "__main__":
    worker = Worker()
    worker.connect()
    worker.start()
