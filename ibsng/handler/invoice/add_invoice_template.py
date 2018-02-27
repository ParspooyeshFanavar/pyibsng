"""Add invoice template API method."""
from ibsng.handler.handler import Handler


class addInvoiceTemplate(Handler):
    """Add invoice template method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.template_name, str)

    def setup(self, template_name):
        """Setup required parameters.

        :param str template_name: template name

        :return: None
        :rtype: None
        """
        self.template_name = template_name
