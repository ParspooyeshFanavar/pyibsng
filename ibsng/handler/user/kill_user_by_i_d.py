""" info API method."""
from ibsng.handler.handler import Handler


class killUserByID(Handler):
    """ info method class."""

    def setup(self, **kwargs):
        """Setup required parameters.

        :param dict kwargs: input args

        :return: void
        :rtype: void
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
