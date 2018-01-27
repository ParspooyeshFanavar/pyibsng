"""Run debug code API method."""
from ibsng.handler.handler import Handler


class runDebugCode(Handler):
    """Run debug code method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.command, str)

    def setup(self, command):
        """Setup required parameters.

        :param str command: command

        :return: None
        :rtype: None
        """
        self.command = command
