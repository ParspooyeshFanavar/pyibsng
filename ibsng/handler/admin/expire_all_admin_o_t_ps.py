"""Expire all admin OTPs API method."""
from ibsng.handler.handler import Handler


class expireAllAdminOTPs(Handler):
    """Expire all admin OTPs class."""

    def setup(self, **kwargs):
        """Setup required parameters.

        :param dict kwargs: input args

        :return: None
        :rtype: None
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
