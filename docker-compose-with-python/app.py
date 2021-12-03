#!/usr/bin/env python3

# https://docs.docker.com/compose/gettingstarted/  tutorial location
import time

# Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker,
# python redis library enables python scripts to communicate with redis server
import redis

# Flask is a micro web framework written in Python
from flask import Flask

app = Flask(__name__)

#cache = redis.Redis(host='0.0.0.0', port=6379)
# In this example, redis is the hostname of the redis container on the application’s network. We use the default port for Redis, 6379.
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 6
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

# Add following line to run the flask sever with command $./app.py
if __name__ == "__main__":
    app.run()