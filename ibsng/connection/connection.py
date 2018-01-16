"""Connection handler library.

This library is middleware between request and session libraries.
"""
from .request import Request
from .session import Session
from ibsng.util import string, file_dir
from ibsng.setting import auth as auth_setting
from ibsng.setting import default as default_setting
from ibsng.exception import exception, handler_exception, method
from ibsng import handler
from ibsng.util import hash


class Connection:
    """Connection handler class."""

    _headers = None
    _session = None
    _request = None

    # Access to handlers
    handler = None

    # Ready state to send requests
    _r_steps = 0
    _r_handler_name = None
    _r_method_name = None
    _r_method_module_name = None

    def __init__(self, conn_str, **headers):
        """Parse connection string and prepare session.

        :param conn_str: connection string
        :param **headers: headers which should be overrided with main headers
        :type conn_str: str
        :type **headers: dict
        :raises ValueError: raise ValueError when connection string is empty or
            server address is not valid
        """
        if not conn_str:
            raise ValueError("Invalid connection string structure.")

        self._auth_params, self._server_url = \
            string.connection_string_parser(conn_str)

        self._session = Session().get_session()
        self._request = Request(self._server_url,
                                self._session)

        self.update_headers(**headers)
        self.handler = handler

        # Ready state to send request
        self._r_steps = 0

    def update_headers(self, **headers):
        """Update headers.

        :param **headers: all required headers which should be overrided
        :type headers: dict
        :return: void
        :rtype: void
        """
        for k, v in headers.items():
            if default_setting.DEFAULT_HEADERS.get(k):
                default_setting.DEFAULT_HEADERS[k] = v
            else:
                default_setting.DEFAULT_HEADERS.update({k: v})
        self._headers = default_setting.DEFAULT_HEADERS
        # Add auth headers
        for k, v in auth_setting.AUTH_HEADERS.items():
            if not self._headers.get(k):
                self._headers.update({k: v})

    def auth(self):
        """Authenticate to the server."""
        # Prepare required headers for authentication
        tmp_params = self._auth_params
        for k, v in self._headers.items():
            if not tmp_params.get(k):
                tmp_params.update({k: v})
        # Call login.login method with parameters
        action = self.call('login.login', **tmp_params)
        self._headers.update({'auth_session': action.get("result")})
        self.clean_headers()

    def clean_headers(self):
        """Remove some headers after successful authentication."""
        self._headers.pop('create_session', None)
        self._headers.pop('login_auth_type', None)
        self._headers.pop('login_auth_pass', None)
        self._headers.pop('auth_pass', None)

    def call(self, method, **params):
        """Send request to the server.

        :param method: API handler and method names
        :param **params: method parameters
        :type method: str
        :type **params: dict
        :return: server response
        :rtype: object
        """
        action = self._request.send(method, **params)
        if action.get("error"):
            raise exception.throw_exception(action.error)
        return action

    def __getattr__(self, api_name):
        """Handler/Method handler.

        :param api_name: handler or method name
        :type api_name: str
        :raises ImportMethodNotFound: raise ImportMethodNotFound when method
            file not found
        :raises ImportHandlerNotFound: raise ImportHandlerNotFound when handler
            directory not found
        :raises ImportMethodError: raise ImportMethodError when importing
            method encoured with erorr
        """
        # Handle first(handler) and second(method) calls
        if self._r_steps == 0:
            self._r_handler_name = api_name
        elif self._r_steps == 1:
            self._r_method_name = api_name
            self._r_method_module_name = string.camel_to_snake(api_name)

        def wrapper(*args, **kwargs):
            # return self
            self._r_steps += 1
            if self._r_steps == 2:
                # Check handler existance
                if not file_dir.is_handler_exist(self._r_handler_name):
                    raise handler_exception.\
                            ImportHandlerNotFound(self._r_handler_name)

                # Check method existance
                if not file_dir.is_method_exist(self._r_handler_name,
                                                self._r_method_module_name):
                    raise method.ImportMethodNotFound(self._r_method_name)

                # Import handler/method module
                try:
                    module = "ibsng.handler.{}.{}". \
                        format(self._r_handler_name,
                               self._r_method_module_name)
                    imp = __import__(module, fromlist=self._r_method_name)
                    action = getattr(imp, self._r_method_name)(*args, **kwargs)
                except ImportError:
                    raise method.ImportMethodError(self._r_method_name)

                # Prepare headers
                tmp_headers = self._headers.copy()
                tmp_headers.update(action.serialize())

                # It's time to call server method
                result = self.call('{}.{}'.format(self._r_handler_name,
                                                  self._r_method_name),
                                   **tmp_headers)
                # Reset the counter
                self._r_steps = 0
                action.outcome(result)
                json_result = result
                result = hash.dict_to_object(result)
                setattr(result, "json", json_result)
                return result
            return self
        return wrapper
