""" info API method."""
from ibsng.handler.handler import Handler


class killUser(Handler):
    """ info method class."""

    def setup(self, user_id, ras_ip, unique_id_val, kill=None):
        """Setup required parameters.

        :param str user_id: comma-seperated User IDs
        :param str ras_ip: comma-seperated RAS IPs
        :param str unique_id_val: Unique ID Value (for exmaple Port, Caller ID, etc)
        :param bool kill: true means Kill User, false means Clear User
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.ras_ip = ras_ip
        self.unique_id_val = unique_id_val
        self.kill = kill
