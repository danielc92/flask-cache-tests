from flask import Flask, render_template, request, url_for
import datetime

# Using simple cache from python interpreter
# from werkzeug.contrib.cache import SimpleCache
# cache = SimpleCache()

# Using memcached server
from werkzeug.contrib.cache import MemcachedCache
cache = MemcachedCache(['127.0.0.1:4800'])


app = Flask(__name__)
app.config['TIMEOUT_CACHE'] = 20 # Seconds
# Function to call and set cache
def return_cache_item():

    name = cache.get('name')
    timestamp = cache.get('timestamp')

    if not name:
        cache.set('name', 'Daniel Corcoran', timeout=app.config['TIMEOUT_CACHE'])
    if not timestamp:
        cache.set('timestamp', datetime.datetime.now(), timeout=app.config['TIMEOUT_CACHE'])

    return name, timestamp

def return_difference_seconds(dt1, dt2):
    diff = dt2 - dt1
    diff_seconds = diff.total_seconds()
    return diff_seconds

@app.route('/')
def index():
    name, timestamp = return_cache_item()
    now = datetime.datetime.now()

    try:
        delta = return_difference_seconds(timestamp, now)
    except:
        delta = None

    return render_template('index.html', name=name, timetamp=timestamp, now=now, delta=delta)


if __name__ == '__main__':
    app.run(debug=True, port=4900)
