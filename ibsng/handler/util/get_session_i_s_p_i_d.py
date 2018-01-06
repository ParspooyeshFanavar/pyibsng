""" info API method."""
from ibsng.handler.handler import Handler


class getSessionISPID(Handler):
    """ info method class."""

    def setup(self, web_domain):
        """Setup required parameters.

        :param str web_domain: domain of user/admin panel page that user has opened
    
        :return: void
        :rtype: void
        """
        self.web_domain = web_domain
