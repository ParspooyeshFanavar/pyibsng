"""Set ISP page style API method."""
from ibsng.handler.handler import Handler


class setISPPageStyle(Handler):
    """Set ISP page style method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.isp_id, int)
        self.is_valid(self.header_logo_ext, str)
        self.is_valid(self.header_logo_contents, str)
        self.is_valid(self.header_bg_color, str)
        self.is_valid(self.header_text_color, str)
        self.is_valid(self.footer_logo_ext, str)
        self.is_valid(self.footer_logo_contents, str)
        self.is_valid(self.footer_bg_color, str)
        self.is_valid(self.footer_text_color, str)
        self.is_valid(self.footer_msg, str)

    def setup(self, isp_id, header_logo_ext, header_logo_contents,
              header_bg_color, header_text_color, footer_logo_ext,
              footer_logo_contents, footer_bg_color, footer_text_color,
              footer_msg):
        """Setup required parameters.

        :param int isp_id: isp id
        :param str header_logo_ext: header logo file extension,
                                    for example 'gif'
        :param str header_logo_contents: base64-encoded data of header
                                         logo image
        :param str header_bg_color: header background color, in html color
                                    format, for example 'E0DEDE'
        :param str header_text_color: header text color, html color format,
                                      for example 'E0DEDE'
        :param str footer_logo_ext: footer logo file extension,
                                    for example 'gif'
        :param str footer_logo_contents: base64-encoded data of footer
                                         logo image
        :param str footer_bg_color: footer background color, in html color
                                    format, for example 'E0DEDE'
        :param str footer_text_color: footer text color, in html color format,
                                      for example 'E0DEDE'
        :param str footer_msg: base64-encoded string of footer message

        :return: None
        :rtype: None
        """
        self.isp_id = isp_id
        self.header_logo_ext = header_logo_ext
        self.header_logo_contents = header_logo_contents
        self.header_bg_color = header_bg_color
        self.header_text_color = header_text_color
        self.footer_logo_ext = footer_logo_ext
        self.footer_logo_contents = footer_logo_contents
        self.footer_bg_color = footer_bg_color
        self.footer_text_color = footer_text_color
        self.footer_msg = footer_msg
