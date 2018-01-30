"""List groups API method."""
from ibsng.handler.handler import Handler


class listGroups(Handler):
    """List groups method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.isp_id, str)
        self.is_valid_content(self.isp_id, self.IDS_PATTERN)
        self.is_valid(self.active_only, bool)

    def setup(self, isp_ids, active_only=False):
        """Setup required parameters.

        :param str isp_ids: comma-seprated list of isp ids
        :param bool active_only: pass true if you only want active groups

        :return: None
        :rtype: None
        """
        self.active_only = active_only
        self.isp_id = ",".join(map(str, isp_ids))
