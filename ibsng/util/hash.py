"""Hash library.

This library provides some functions which are useful
to work on dict/json objects.
"""
import json


def serialize(data):
    """Serialize dict object.

    :param data: dict object
    :type data: dict
    :return: json string
    :rtype: str
    :raises ValueError: raise ValueError when can't dump dict
    """
    return json.dumps(data)


def deserialize(data):
    """Deserialize json string.

    :param data: json string
    :type data: str
    :return: dict object
    :rtype: dict
    :raises ValueError: raise ValueError when can't load json
    """
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        raise ValueError("Deserialize failed. Invalid data.")


class dict_to_object:
    """Convert dictionary to object."""

    def __init__(self, d):
        """Convert dictionary to object.

        :param d: dict object
        :type d: dict
        """
        for k, v in d.items():
            if (isinstance(v, (list, tuple))):
                setattr(self, k, [dict_to_object(x)
                                  if isinstance(x, dict) else x for x in v])
            else:
                setattr(self, k, dict_to_object(v)
                        if isinstance(v, dict) else v)
