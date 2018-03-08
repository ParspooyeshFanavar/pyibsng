Write Module
============

To write a new API method for driver do these steps:

for example:
* Handler: `book`
* Methods: `searchBook(name)` and `getAllBooksID()`.

Note: method name is in camel-case style, also first word must be small.

.. code-block:: shell

	$ cd /path/to/pyibsng/
	$ cd ibsng/handler
	$ mkdir book
	$ cd book
        $ touch __init__.py
	$ touch search_book.py
	$ touch get_all_books_i_d.py

Note: when you want to mention that a word is upper case, the add an underscore before it. for example `_i_d` will be considerd as `ID` in framework. so if your method is `getAll` then its python file name must be `get_all`.


`search_book.py`:

.. code-block:: python

    """Search book by name API method."""
    from ibsng.handler.handler import Handler


    class searchBook(Handler):
        """Search book by name method."""

        def control(self):
            """Validate inputs after setup method.

            :return: None
            :rtype: None
            """
            self.is_valid(self.name, str)

        def setup(self, name):
            """Setup required parameters.

            :param str name: book name

            :return: None
            :rtype: None
            """
            self.name = name


`get_all_books_i_d.py`:

.. code-block:: python

    """Get all books ids API method."""
    from ibsng.handler.handler import Handler


    class getAllBooksID((Handler):
        """Get all books ids method."""

        pass

Note: every method which have arguments, should contain `setup` method in its class.

Note: if you want to validate arguments before sending to the sever, you should consider `control` method in your class.
