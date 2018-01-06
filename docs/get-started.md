## Get Started
After installing the driver, then we are going to use it in our Python source code:

```python
from ibsng import IBSng
from ibsng.exception import auth
conn = IBSng("username:password@http://ip:port")

try:
	conn.auth()
except exception.auth.InvalidAuthentication:
	print("Authentication failed. Check username or password.")
```

To call handler/method (after authentication):

This is the pattern: `conn.<HANDLER_NAME>().<METHOD_NAME>(*args, **kwargs)`

```python
print(conn.user().searchUser(1, 20, 10000, '<'))
```

**Note:** method should be in camel case style and first word must be small.

Each method has it's own behaviour and parameters. To get more info about each one, try to read docstring of each method.

For example `searchUser`:

```python
from ibsng.handlers.user import search_user
search_user.searchUser.__doc__
```

**Note:** naming convension is that directory name is in small words and uses  underscores for each word and it's class name is in camel case style.