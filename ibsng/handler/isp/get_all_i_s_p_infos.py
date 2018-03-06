"""Get all ISP infos API method."""
from ibsng.handler.handler import Handler


class getAllISPInfos(Handler):
    """Get all ISP infos method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        if hasattr(self, 'sort_by'):
            self.is_valid(self.sort_by, str)

    def setup(self, sort_by=None):
        """Setup required parameters.

        :param type sort_by: sort by

        :return: None
        :rtype: None
        """
        if sort_by:
            self.sort_by = sort_by
