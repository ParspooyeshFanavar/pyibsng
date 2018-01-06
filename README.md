# IBSng Python Driver

This library will provide you access on API of IBSng.

> **NOTE:** This project is under construction, some handlers work fine, but some others are under the development. 

### Support
* Python 2.7.x
* Python 3.x.x

### Install
After downloading the source code, do these steps:
```sh
$ tar xzf pyibsng-<VERSION>.tar.gz
$ cd ibsng
$ python setup.py install
```
To make sure that this library works fine, run this command:
Python2:
```sh
$ make test-py2
```
Python3:
```sh
$ make test-py3
```

### Get Started:

To start using this library we need to import `IBSng` package:
```python
from ibsng import IBSng
```

#### Test Authentication:
```python
c = IBSng("user:password@http://ip:port")
c.auth()
```