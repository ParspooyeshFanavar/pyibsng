Get Started
===========
After installing the driver, then we are going to use it in our Python source code:

.. code-block:: python

    from ibsng import IBSng
    from ibsng.exception import auth
    con = IBSng("username:password@http://ip:port")

    try:
        con.auth()
    except exception.auth.InvalidAuthentication:
	print("Authentication failed. Check username or password.")


To call handler/method (after authentication):

This is the pattern: `con.<HANDLER_NAME>.<METHOD_NAME>(*args, **kwargs)`

.. code-block:: python

    print(con.user.searchUser(1, 20, 10000, '<'))


**Note:** method should be in camel case style and first word must be small.

Each method has it's own behaviour and parameters. To get more info about each one, try to read docstring of each method.

For example `searchUser`:

.. code-block:: python

    from ibsng.handlers.user import search_user
    print(search_user.searchUser.__doc__)

