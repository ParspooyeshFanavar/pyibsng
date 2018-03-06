"""Get permissions of template API method."""
from ibsng.handler.handler import Handler


class getPermsOfTemplate(Handler):
    """Get permissions of template method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.perm_template_name, str)

    def setup(self, perm_template_name):
        """Setup required parameters.

        :param str perm_template_name: permission template name

        :return: None
        :rtype: None
        """
        self.perm_template_name = perm_template_name
