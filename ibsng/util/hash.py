"""Hash library.

This library provides some functions which are useful
to work on dict/json objects.
"""
import json


def serialize(data):
    """Serialize dict object.

    :raises ValueError: raise ValueError when can't dump dict

    :param data: dict object
    :type data: dict

    :return: json string
    :rtype: str
    """
    return json.dumps(data)


def deserialize(data):
    """Deserialize json string.

    :raises ValueError: raise ValueError when can't load json

    :param data: json string
    :type data: str

    :return: dict object
    :rtype: dict
    """
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        raise ValueError("Deserialize failed. Invalid data.")


class dict_to_object:
    """Convert dictionary to object."""

    def __init__(self, data_dict):
        """Convert dictionary to object.

        :param data_dict: data dict object
        :type data_dict: dict
        """
        for k, v in data_dict.items():
            if (isinstance(v, (list, tuple))):
                setattr(self, k, [dict_to_object(x)
                                  if isinstance(x, dict) else x for x in v])
            else:
                setattr(self, k, dict_to_object(v)
                        if isinstance(v, dict) else v)

    def inspect(self, key_name=None):
        """Prepare result as readable structure.

        :param key_name: result key name
        :type key_name: str

        :return: readable data structure
        :rtype: object
        """
        result = []
        for var in dir(self):
            if var.startswith("__"):
                continue

            if key_name and key_name == var:
                return getattr(self, var)

            result.append(var)
        return result
