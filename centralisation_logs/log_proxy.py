import zmq


class LogProxy:
    def __init__(self):
        self.context = zmq.Context()
        self.incoming_socket = self.context.socket(zmq.XSUB)
        self.outgoing_socket = self.context.socket(zmq.XPUB)

    def connect(self):
        self.incoming_socket.bind("tcp://*:5555")
        self.outgoing_socket.bind("tcp://*:5556")

    def start(self):
        zmq.proxy(self.incoming_socket, self.outgoing_socket)

    def stop(self):
        self.incoming_socket.close()
        self.outgoing_socket.close()
        self.context.term()


if __name__ == "__main__":
    log_proxy = LogProxy()
    log_proxy.connect()
    log_proxy.start()
