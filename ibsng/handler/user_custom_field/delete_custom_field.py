"""Delete custom field API method."""
from ibsng.handler.handler import Handler


class deleteCustomField(Handler):
    """Delete custom field method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.name, str)

    def setup(self, name):
        """Setup required parameters.

        :param str name: custom field name

        :return: None
        :rtype: None
        """
        self.name = name
