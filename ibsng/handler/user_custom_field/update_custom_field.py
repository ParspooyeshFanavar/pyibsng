"""Update custom field API method."""
from ibsng.handler.handler import Handler


class updateCustomField(Handler):
    """Update custom field method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.custom_field_id, int)
        self.is_valid(self.name, str)
        self.is_valid(self.description, str, False)
        self.is_valid(self.value_type, str)
        self.is_valid_content(self.value_type, "(string|integer|float)")
        self.is_valid(self.interface_type, str)
        self.is_valid_content(self.interface_type, "(text_field|single_select\
                                                   |radio_button|checkbox)")
        self.is_valid(self.allowable_values, list, False)
        self.is_valid(self.mandatory, bool)
        self.is_valid(self.comment, str, False)

    def setup(self, custom_field_id, name, description, value_type,
              interface_type, allowable_values, mandatory, comment=""):
        """Setup required parameters.

        :param int custom_field_id: ibsng custom field id
        :param str name: custom field name
        :param str description: custom field description
        :param str value_type: custom field value type: string, integer, float
        :param str interface_type: custom field interface type: text_field,
                                   single_select, radio_button, checkbox
        :param list allowable_values: type of items depends on value_type param
        :param bool mandatory: mark field as required
        :param str comment: custom field comment

        :return: None
        :rtype: None
        """
        self.custom_field_id = custom_field_id
        self.name = name
        self.description = description
        self.value_type = value_type
        self.interface_type = interface_type
        self.allowable_values = allowable_values
        self.mandatory = mandatory
        self.comment = comment
