"""API methods interface handler.

All method classes should get instance of Interface class.
New method should override __init__ method and if you want
to use Python keywords in header keys like 'from', try to add
an underscore after that like so 'from_'. Interface
class will replace just one '_' with blank.

Note 1: New method name should be in camel case style and first
word must be small. Also it's file name should be small and use
underscore instead of camel case like so:

  'myNewMethod' -> my_new_method.py

Note 2: try to use default structure and avoid to override other
methods of Interface class.

Sample:

class myNewMethod(Interface):
    def __init__(self, from_, to_):
        self.from_ = from_
        self.to_ = to_
"""
from abc import ABCMeta

from ibsng.handler.initiator import Initiator
from ibsng.handler.control import Control


class Handler(Initiator, Control, metaclass=ABCMeta):
    """Base handler class to handle API methods."""

    _method_headers = dict()

    def __init__(self, *args, **kwargs):
        """Make headers ready."""
        super(Handler, self).__init__(*args, **kwargs)
        self.update_headers()
        self.control()

    def update_headers(self):
        """Update required headers keys before each request.

        :return: None
        :rtype: None
        """
        self._method_headers.update({k[:-1] if k.endswith('_') else k: v
                                     for k, v in vars(self).items()})

    def get_headers(self):
        """Return current method headers.

        :return: return method headers
        :rtype: dict
        """
        return self._method_headers

    def outcome(self, result):
        """Convert result items to required types.

        .. note: Should be implemented based on requirements

        :param dict result: IBSng json result

        :return: None
        :rtype: None
        """
        pass

    def serialize(self):
        """Serialize all entries and make ready to send.

        :return: method headers
        :rtype: dict
        """
        return self._method_headers
