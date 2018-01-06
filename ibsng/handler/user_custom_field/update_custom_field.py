""" info API method."""
from ibsng.handler.handler import Handler


class updateCustomField(Handler):
    """ info method class."""

    def setup(self, custom_field_id, name, description, comment, value_type, interface_type, allowable_values, mandatory):
        """Setup required parameters.

        :param int custom_field_id: 
        :param str name: 
        :param str description: 
        :param str comment: 
        :param choice value_type: 
        :param choice interface_type: 
        :param list allowable_values: type of items depends on value_type param
        :param bool mandatory: 
    
        :return: void
        :rtype: void
        """
        self.custom_field_id = custom_field_id
        self.name = name
        self.description = description
        self.comment = comment
        self.value_type = value_type
        self.interface_type = interface_type
        self.allowable_values = allowable_values
        self.mandatory = mandatory
