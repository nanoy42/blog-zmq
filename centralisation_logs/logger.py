import argparse
import re
from datetime import datetime

import zmq


class Logger:
    """Receive and print logs.
    """

    INFO = 0
    WARN = 1
    ERROR = 2

    VERBOSE_LEVEL = {
        INFO: "INFO",
        WARN: "WARN",
        ERROR: "ERROR",
    }

    def __init__(self, log_level):
        """Initialize the Logger interface
        
        Args:
            log_level (string): info, warn or error. Any other string will be interpreted as printing all logs.
        """
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.pattern = re.compile(r"^(\d) (\S*) (.*)$")
        if log_level == "info":
            self.subscribe = str(self.INFO)
        elif log_level == "warn":
            self.subscribe = str(self.WARN)
        elif log_level == "error":
            self.subscribe = str(self.ERROR)
        else:
            self.subscribe = ""

    def connect(self):
        """Subscribe and connect socket
        """
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self.subscribe)
        self.socket.connect("tcp://localhost:5556")

    def start(self):
        """Receive logs and print information.
        """
        while True:
            result = self.pattern.search(self.socket.recv_string())
            level, name, msg = result.groups()
            current_time = datetime.now().strftime("%H:%M:%S")
            print(
                "{} ({}) - {} - {}".format(
                    self.VERBOSE_LEVEL[int(level)], name, current_time, msg
                )
            )

    def stop(self):
        """Close socket and context.
        """
        self.socket.close()
        self.context.term()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "level",
        help="level to print. Should be info, warn or all. all will be set by default",
    )
    args = parser.parse_args()

    logger = Logger(args.level)
    logger.connect()
    logger.start()
