"""Connection handler library.

This library is middleware between request and session libraries.
"""
from .request import Request
from .session import Session
from ibsng.util import string, file_dir
from ibsng.setting import auth as auth_setting
from ibsng.setting import default as default_setting
from ibsng.exception import (response as response_exception,
                             handler as handler_exception,
                             method as method_exception,
                             general as general_exception)
from ibsng import handler
from ibsng.util import hash


class Connection:
    """Connection handler class."""

    def __init__(self, conn_str, timeout=0.5, **headers):
        """Parse connection string and prepare session.

        :raises ValueError: raise ValueError when connection string is empty or
                            server address is not valid

        :param conn_str: connection string
        :type conn_str: str
        :param **headers: headers which should be overrided with main headers
        :type **headers: dict
        """
        if not conn_str:
            raise ValueError("Invalid connection string structure.")

        # required variables for requests
        self._headers = None
        self._auth_params, self._server_url = \
            string.connection_string_parser(conn_str)

        self._session = Session().get_session()
        self._request = Request(self._server_url,
                                self._session,
                                timeout=timeout)

        self.handler = handler

        # ready state to send requests
        self._r_steps = 0
        self._r_handler_name = None
        self._r_method_name = None
        self._r_method_module_name = None

        # list of all items in chain just for debugging
        self._r_chain = []

        # update headers
        self._update_headers(**headers)

    def _reset_variables(self, keep_chain=False):
        """Reset required variables.

        :param keep_chain: keep chain for debugging
        :type keep_chain: bool

        :return: None
        :rtype: None
        """
        self._r_steps = 0
        self._r_handler_name = None
        self._r_method_name = None
        if not keep_chain:
            self._r_chain.clear()

    def _update_headers(self, **headers):
        """Update headers.

        :param **headers: all required headers which should be overrided
        :type headers: dict

        :return: None
        :rtype: None
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
        """Authenticate to the server.

        It tries to authenticate user and updates headers.

        :return: None
        :rtype: None
        """
        # Prepare required headers for authentication
        tmp_params = self._auth_params
        for k, v in self._headers.items():
            if not tmp_params.get(k):
                tmp_params.update({k: v})

        # Call login.login method with parameters
        action = self._call("login.login", **tmp_params)
        self._headers.update({"auth_session": action.get("result")})
        self._headers.update({"auth_name": self._auth_params["auth_name"]})
        self.clean_headers()
        self._r_chain = []
        self._r_handler_name = None

    def clean_headers(self):
        """Remove some headers after successful authentication.

        :return: None
        :rtype: None
        """
        self._headers.pop('create_session', None)
        self._headers.pop('login_auth_type', None)
        self._headers.pop('login_auth_pass', None)
        self._headers.pop('auth_pass', None)

    def _call(self, method, **params):
        """Send request to the server.

        :param method: API handler and method names
        :type method: str
        :param **params: method parameters
        :type **params: dict

        :return: server response
        :rtype: object
        """
        action = self._request.send(method, **params)
        if action.get("error"):
            raise response_exception.throw_exception(action["error"])
        return action

    def __call__(self, *args, **kwargs):
        """Call handler method."""
        # Check handler existance
        if not file_dir.is_handler_exist(self._r_handler_name):
            raise handler_exception.ImportHandlerNotFound(self._r_handler_name)

        # Check method existance
        if not file_dir.is_method_exist(self._r_handler_name,
                                        self._r_method_module_name):
            raise method_exception.ImportMethodNotFound(self._r_method_name)

        # Import handler/method module
        try:
            module = "ibsng.handler.{}.{}". \
                     format(self._r_handler_name, self._r_method_module_name)
            imp = __import__(module, fromlist=self._r_method_name)
            action = getattr(imp, self._r_method_name)(*args, **kwargs)
        except ImportError:
            raise method_exception.ImportMethodError(self._r_method_name)

        # Prepare headers
        tmp_headers = self._headers.copy()
        tmp_headers.update(action.serialize())

        # It's time to call server method
        result = self._call('{}.{}'.format(self._r_handler_name,
                                           self._r_method_name),
                            **tmp_headers)

        self._reset_variables()
        action.outcome(result)
        json_result = result
        result = hash.dict_to_object(result)
        setattr(result, "json", json_result)
        return result

    def __getattr__(self, api_name):
        """Handler/Method handler.

        Handle first(handler) and second(method) calls.

        .. raises:: ImportMethodNotFound: raise ImportMethodNotFound when
            method file not found
        .. raises:: ImportHandlerNotFound: raise ImportHandlerNotFound when
            handler directory not found
        .. raises:: ImportMethodError: raise ImportMethodError when importing
            method encoured with erorr
        .. raises:: general_exception.ChainFormatError: in case on any invalid
            chain structure

        :param api_name: handler or method name
        :type api_name: str
        """
        self._r_chain.append(api_name)
        if self._r_steps == 0:
            self._r_handler_name = api_name
        elif self._r_steps == 1:
            self._r_method_name = api_name
            self._r_method_module_name = string.camel_to_snake(api_name)
        else:
            self._reset_variables(True)
            raise general_exception.ChainFormatError(self._r_chain)

        self._r_steps += 1
        return self
