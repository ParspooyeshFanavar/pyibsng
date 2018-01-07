"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class getActiveLeaves(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, **kwargs):
        """Setup required parameters.

        :param dict kwargs: input args

        :return: void
        :rtype: void
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
