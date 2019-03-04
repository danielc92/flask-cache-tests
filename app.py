from flask import Flask, render_template, request, url_for
from datetime import datetime
from datetime import timedelta

# Using simple cache from python interpreter
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

# Using memcached server
# from werkzeug.contrib.cache import MemcachedCache
# cache = MemcachedCache(['127.0.0.1:4800'])


# Instantiate app instance
app = Flask(__name__)

# Set cache timeout dictionary
app.config['CACHE_LIFE'] = {'SHORT': 30, 'MEDIUM': 60 * 5, 'LONG': 60 * 60 * 4}


# Function to return now() datetime object
def return_now():
    return datetime.now()


# Function to call and set cache
def return_cache_item():

    name = cache.get('name')
    timestamp = cache.get('timestamp')

    if not name:
        cache.set('name', 'Daniel Corcoran', timeout=app.config['CACHE_LIFE']['SHORT'])
        name = cache.get('name')
    if not timestamp:
        cache.set('timestamp', return_now(), timeout=app.config['CACHE_LIFE']['SHORT'])
        timestamp = cache.get('timestamp')

    return name, timestamp


def return_difference_seconds(dt1, dt2):
    diff = dt2 - dt1
    diff_seconds = diff.total_seconds()
    return diff_seconds


@app.route('/')
def index():

    name, timestamp = return_cache_item()
    now = return_now()
    expires = timestamp + timedelta(seconds=app.config['CACHE_LIFE']['SHORT'])

    try:
        delta = return_difference_seconds(timestamp, now)
    except:
        delta = None

    return render_template('index.html',
                           expires=expires.strftime('%d-%b-%Y %H:%M:%S'),
                           name=name,
                           timestamp=timestamp.strftime('%d-%b-%Y %H:%M:%S'),
                           now=now.strftime('%d-%b-%Y %H:%M:%S'),
                           delta=delta)


if __name__ == '__main__':
    app.run(debug=True, port=4900)