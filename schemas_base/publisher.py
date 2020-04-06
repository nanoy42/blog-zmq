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

import time

import zmq

context = zmq.Context()
publisher = context.socket(zmq.PUB)

publisher.bind("tcp://*:5555")

time.sleep(0.20)  # regle le probleme des slow joiners
for i in range(5):
    publisher.send(b"Hello everyone. This is message %i" % i)
    time.sleep(2)
