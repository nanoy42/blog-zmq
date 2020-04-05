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
