"""Main request handler library.

This library prepares and send http request.
"""
from ibsng.util import hash


class Request:
    """Request handler class."""

    def __init__(self, server_addr, session):
        """Request handler init.

        :param server_addr: connection string
        :type server_addr: str
        :param session: connection session ID
        :type session: str
        """
        self._server_addr = server_addr
        self._session = session

    def send(self, method, **params):
        """Send request to the server.

        :raises ValueError: raise ValueError when server result is not JSON

        :param method: handler and method names
        :type method: str
        :param **params: send method parameters
        :type **params: dict

        :return: server result
        :rtype: dict
        """
        data = hash.serialize(dict(method=method, params=params))
        # Post request
        result = self._session.post(url=self._server_addr, data=data)
        # Convert server response to object
        try:
            return hash.deserialize(result.text)
        except Exception:
            raise ValueError("Convert server response failed.")
