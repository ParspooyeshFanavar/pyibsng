"""Echo request input API method."""
from ibsng.handler.handler import Handler


class echo(Handler):
    """Echo request input method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.echo, str)

    def setup(self, echo):
        """Setup required parameters.

        :param str echo: string arg

        :return: None
        :rtype: None
        """
        self.echo = echo
