# worker.py - Worker process

from redis import Redis
from rq import Worker, Queue, Connection

listen = ['default']
redis_conn = Redis(host='localhost', port=6379)

if __name__ == '__main__':
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen))
        worker.work()
