# from redis.client import Redis
# client = Redis(connection_pool=BlockingConnectionPool())

import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
r.get('foo')

