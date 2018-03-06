"""String library.

This library provides some useful functions which works on strings.
"""
from ibsng.exception import connection
import re


def connection_string_parser(conn_str):
    """Parse connection string pattern.

    :raises ValueError: raise ValueError when can't parse connection string
    :raises InvalidConnectionString: rasie InvalidConnectionString when
                                     connection string is not in correct style

    :param conn_str: connection string
    :type conn_str: str

    :return: connection config
    :rtype: tuple
    """
    try:
        # Fetch server info (host/port)
        if conn_str.rfind('@') >= 0:
            server_url = conn_str[conn_str.rindex('@')+1:]
        else:
            raise ValueError("Invalid connection string structure.")

        if not validate_server_addr(server_url):
            raise ValueError("Invalid server address.")

        # Fetch IP address
        host = server_url.split(':')[1][2:]

        # Fetch user info (username/password)
        user_info = conn_str[:conn_str.rfind('@')]

        # Prepare result
        auth_params = {
            'auth_remoteaddr': host,
            'auth_name': user_info[:user_info.find(':')],
            'auth_pass': user_info[user_info.find(':')+1:],
            'login_auth_name': user_info[:user_info.find(':')],
            'login_auth_pass': user_info[user_info.find(':')+1:],
        }
        return (auth_params, server_url)
    except Exception:
        raise connection.InvalidConnectionString()


def camel_to_snake(string):
    """Convert camel to snake style.

    :param string: camel string
    :type string: str

    :return: snake style string
    :rtype: str
    """
    string = "".join([(x.replace(x, '_' + x.lower() if x.isupper() else x))
                     for x in list(string)])
    if string.startswith('_'):
        string = string[1:]
    return string


def validate_server_addr(server_addr):
    """Server address validation.

    :param server_addr: Server address (domain name or IP)
    :type server_addr: str

    :return: return validation result
    :rtype: bool
    """
    check_pattern = "^(http|https)://([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+|" + \
                    "[a-zA-Z0-9\-\.]+\.[a-zA-Z]+)(:[0-9]+)?$"
    if not re.match(check_pattern, server_addr):
        return False
    return True
