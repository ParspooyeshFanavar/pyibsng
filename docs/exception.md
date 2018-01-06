##IBSng API: Exceptions

```python
from ibsng import exception
```

###Exceptions lists:

* **connection**
  * *100: InvalidConnectionString(void)*
  * *101: ServerConnectionError(void)*
* **handler**
  * *201: ImportHandlerNotFound(handler_name)*
* **Method**
  * *301: ServerMethodError(error_text)*
  * *302: ImportMethodNotFound(method_name)*
  * *303: ImportMethodError(method_name)*
* **auth**:
  * *401: InvalidAuthentication(void)*
* **unknown**
  * *501: UnknownError(error_text)*

To throw a server exception:
* **exception**:
  * *600: throw_exception(server_error)*

### New Exception:

To create new exception, it should be get inherit from `IBSngException` class.

```python
from ibsng.exception.base import IBSngException
class NewException(IBSngException):
    """Some description about this exception."""
    _err_code = <YOUR ERR NUMBER>
    def __init__(self, your_input):
        message = "Error message: {}".format(your_input)
        super(NewException, self).__init__(message)
```

Note: Each exception should has `_err_code` variable in public.