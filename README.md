# Project Title
Some examples with caching in flask. Using simple caching and memcached server locally.

# Before you get started
- Understanding of web servers and the important of cacheing.

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