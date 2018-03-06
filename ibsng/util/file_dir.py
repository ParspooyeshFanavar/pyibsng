"""Util for file and directory.

This library provides some functions to work on file and directory.
"""
import os
from ibsng.setting import general
from ibsng.util import string


def is_handler_exist(handler_name):
    """Check the handler is exist in driver.

    :param handler_name: handler name
    :type handler_name: str

    :return: is handler exists or not
    :rtype: bool
    """
    handler_path = os.path.join(general.BASE_DIR,
                                "handler/{}".format(handler_name))
    if os.path.exists(handler_path):
        return True
    return False


def is_method_exist(handler_name, method_name):
    """Check the method is exist in driver.

    :param handler_name: handler name
    :type handler_name: str
    :param metho_name: method name
    :type method_name: str

    :return: is method exists or not
    :rtype: bool
    """
    method_name = string.camel_to_snake(method_name)
    method_path = os.path.join(general.BASE_DIR,
                               "handler/{}/{}.py".format(handler_name,
                                                         method_name))
    if os.path.exists(method_path):
        return True
    return False
