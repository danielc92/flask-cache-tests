# Project Title
Some examples with caching in flask. Using simple caching and memcached server locally.

# Before you get started
- Understanding of web servers and the important of cacheing.
- Understanding of basic flask application and how to run locally.
- Flask app contains method to calculate difference in dates, as well as method to set and get cache values.
- Flask app simply displays retrieval data for cache when visitting `localhost:4900`
- Memcached server configuration currently set to port `4800` in flask app, however `SimpleCache` can be used as an alternative solution.

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/flask-cache-tests.git
```
**Modules/dependencies:**
- `flask`

Install the following dependences:
```sh
pip install flask
```

Installing memcached
```sh
brew install memcached
```

Running memcached as background process. `-d` runs as background process. `-p` designates the port. 
```sh
memcached -p {port} -d
```

# Tests
- Testing setting and getting key values from local cache using `SimpleCache` method.
- Testing setting and getting key values from local cache using `memcached` server method.

# Contributors
- Daniel Corcoran

# Sources
- [Installing memcached server on macosx](https://www.hacksparrow.com/install-memcached-on-mac-os-x.html)