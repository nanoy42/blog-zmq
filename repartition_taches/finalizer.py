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

import msgpack
import zmq


class Finalizer:
    def __init__(self, n):
        """Init the finalizer.
        
        Args:
            n (int): number of temperatures
        """
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.expected = n
        self.received = 0
        self.result = 0

    def connect(self):
        """Connect socket.
        """
        self.socket.bind("tcp://*:5556")

    def start(self):
        """Wait for all tasks to finish and print the result.
        """
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
