"""Main inputs validator library."""
from ibsng.exception.method import InvalidArgumentType, InvalidArgumentValue


class Control(object):
    """Controlling inputs.

    .. note: do not implement __init__ method for this class.
    """

    def is_valid(self, argument_value, argument_type):
        """Validate argument type before sending to the server.

        .. raise: InvalidArgumentType

        :param type argument_value: argument data
        :param type argument_type: type of argument which argument must be.

        :return: argument validation
        :rtype: bool
        """
        if not isinstance(argument_value, argument_type):
            raise InvalidArgumentType(self.__class__.__name__,
                                      argument_value,
                                      argument_type)
        return True

    def is_valid_content(self, argument_value, valid_values=[]):
        """Validate argument content before sending to the server.

        .. raise: InvalidArgumentValue

        :param type argument_value: argument data
        :param type valid_values: list of valid values which argument_data
                                  should be in.

        :return: argument validation
        :rtype: bool
        """
        if not argument_value or argument_data not in valid_values:
            raise InvalidArgumentValue(self.__class__.__name__,
                                       argument_value,
                                       valid_values)
        return True

    def control(self):
        """This method will be called to validate inputs.

        .. note: Should be implemented based on requirements

        :return: None
        :rtype: None
        """
        pass