import time
from os import environ
import redis
from flask import Flask
from waitress import serve

app = Flask(__name__)

if "REDIS_URL" in environ:
    __redis_url__ = environ["REDIS_URL"]
else:
    __redis_url__ = 'localhost'

if "CI_COMMIT_SHORT_SHA" in environ:
    __version__ = environ["CI_COMMIT_SHORT_SHA"]
else:
    __version__ = "develop"

cache = redis.Redis(host=__redis_url__, port=6379)

def get_hit_count():
    retries = 5
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
    try:
        count = get_hit_count()
    except:
        return 'ERR# Redis server not found at url:"{}"'.format(__redis_url__)
    
    return f'Hello, World: {count} times.\n Running version: {__version__} \n'

@app.route('/fail')
def fail():
    try:
        fail()
    except:
        fail()

if __name__ == '__main__':
    print('Starting webcounter')
    serve(app, host='0.0.0.0', port=5000)