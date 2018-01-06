### Write Module

To develop and add new module for driver (new API method) do these steps:

for example we are going to create a module:
* Handler: `hello`
* Methods: `searchWorld(name, range)` and `galaxy()`.

Note: method name is in camel-case style, also first word must be small.

```sh
$ cd IBSNG_DRIVER_PATH
$ cd ibsng/handler
$ mkdir hello
$ cd hello
$ touch search_world.py
$ touch galaxy.py
```

search_world.py:
```python
from ibsng.handler import handler

class searchWorld(handler.Handler):
	def __init__(self, name, range):
		self.name = name
		self.range = range
```

galaxy.py
```python
from ibsng.handler import handler

class galaxy(handler.Handler):
	def __init__(self):
		pass
```
