"""Main request handler library.

This library prepares and send http request.
"""
from ibsng.util import hash


class Request:
    """Request handler class."""

    # all required headers
    _session = None

    # server url
    _server_addr = None

    def __init__(self, server_addr, session):
        """Request handler init.

        :param server_addr: connection string
        :param session: connection session ID
        :type server_addr: str
        :type session: str
        """
        self._server_addr = server_addr
        self._session = session

    def send(self, method, **params):
        """Send request to the server.

        :param method: handler and method names
        :param **params: send method parameters
        :type method: str
        :type **params: dict
        :return: server result
        :rtype: object
        :raises ValueError: raise ValueError when server result is not JSON
        """
        data = hash.serialize(dict(method=method, params=params))
        # Post request
        result = self._session.post(url=self._server_addr, data=data)
        # Convert server response to object
        try:
            return hash.deserialize(result.text)
        except Exception:
            raise ValueError("Convert server response failed.")
