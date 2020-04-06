# BLOG ZMQ

This a the source code for the following blog article : https://nanoy.fr/blog/zeromq

## Installation

You can install the dependencies  with the command 

```
pipenv install
```

If you want the same versions as the last commit on this project :

```
pipenv install --ignore-pipfile
```

You can also install with rhe requirements.txt file:

```
pip3 install -r requirements.txt
```

## Architecture

### schemas_base

Contains 3 basis schemes : client server, publisher subscriber and pusher puller.

Yon can use test the schemes using the following command (each command of the same block should be launched in different terminals) :

```
python3 server.py
python3 client.py
```

```
python3 subscriber.py
python3 publisher.py
```

```
python3 puller.py
python3 puller.py
python3 pusher.py
```
### repartition_taches

You can test the example with the following command :

```
python3 finalizer.py 25000
python3 worker.py
python3 worker.py
python3 worker.py
python3 controller.py 250000 1000
```

### centralisation_logs

You can run the example with the following command

```
python3 log_proxy.py
python3 logger.py
python3 logger.py error
python3 gen_log.py device1
python3 gen_log.py device2
```
