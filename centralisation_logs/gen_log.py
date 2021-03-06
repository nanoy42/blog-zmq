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
import random
import time

import zmq


class Log:
    """Generator of logs.
    """

    INFO = 0
    WARN = 1
    ERROR = 2

    def __init__(self, name):
        """Initialise the Log interface
        
        Args:
            name (string): name of the log generator
        """
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.name = name

    def connect(self):
        """Connect socket
        """
        self.socket.connect("tcp://localhost:5555")

    def start(self):
        """Send logs.

        The log generator send random logs (see get_log) with an interval from 0 to 5 seconds.
        """
        while True:
            level, log = self.get_log()
            self.socket.send_string("%i %s %s" % (level, self.name, log))
            time.sleep(random.randint(0, 5))

    def get_log(self):
        """Simulate logs.

        70% of logs are info logs.
        20% of logs are warning logs.
        10% of logs are error logs.
        
        Returns:
            (int, string): the log level and the string message.
        """
        p = random.random()
        if p <= 0.7:
            return (self.INFO, "Just info.")
        elif p <= 0.9:
            return (self.WARN, "Some warning.")
        else:
            return (self.ERROR, "Critical error.")

    def stop(self):
        """Close socket and context.
        """
        self.socket.close()
        self.context.term()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="name of the generator of log")
    args = parser.parse_args()

    log = Log(args.name)
    log.connect()
    log.start()
