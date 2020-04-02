import zmq
import msgpack


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
