"""Message Center info API method."""
from ibsng.handler.handler import Handler


class getProviderTypes(Handler):
    """Message Center info method class."""

    def setup(self, **kwargs):
        """Setup required parameters.

        :param dict kwargs: input args

        :return: void
        :rtype: void
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
