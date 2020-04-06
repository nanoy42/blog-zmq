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

import random
import time

import zmq

context = zmq.Context()
puller = context.socket(zmq.PULL)

puller.connect("tcp://localhost:5555")


while True:
    print(puller.recv_string())
    time.sleep(random.randint(1, 5))  # execute la tache
    print("Task done")
