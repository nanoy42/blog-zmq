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

import zmq


class LogProxy:
    """Proxy interface
    """

    def __init__(self):
        """Initialize context and sockets.
        """
        self.context = zmq.Context()
        self.incoming_socket = self.context.socket(zmq.XSUB)
        self.outgoing_socket = self.context.socket(zmq.XPUB)

    def connect(self):
        """Connect sockets.
        """
        self.incoming_socket.bind("tcp://*:5555")
        self.outgoing_socket.bind("tcp://*:5556")

    def start(self):
        """Start the proxy.
        """
        zmq.proxy(self.incoming_socket, self.outgoing_socket)

    def stop(self):
        """Close sockets and context.
        """
        self.incoming_socket.close()
        self.outgoing_socket.close()
        self.context.term()


if __name__ == "__main__":
    log_proxy = LogProxy()
    log_proxy.connect()
    log_proxy.start()
