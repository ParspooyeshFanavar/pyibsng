"""Kill user API method."""
from ibsng.handler.handler import Handler


class killUser(Handler):
    """Kill user method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, str)
        self.is_valid(self.ras_ip, str)
        self.is_valid(self.unique_id_val, str)
        self.is_valid(self.kill, bool)

    def setup(self, user_ids, ras_ips, unique_id_val, kill=False):
        """Setup required parameters.

        :param list user_id: ibsng user ids
        :param list ras_ips: ras ips
        :param str unique_id_val: unique id value (for exmaple port, caller id,
                                  etc)
        :param bool kill: true means 'Kill User', false means 'Clear User'

        :return: None
        :rtype: None
        """
        self.user_id = ",".join(map(str, user_ids))
        self.ras_ip = ",".join(map(str, ras_ips))
        self.unique_id_val = unique_id_val
        self.kill = kill
