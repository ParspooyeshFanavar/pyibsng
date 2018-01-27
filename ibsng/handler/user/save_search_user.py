"""Save search user API method."""
from ibsng.handler.handler import Handler


class saveSearchUser(Handler):
    """Save search users method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.basic, list)
        self.is_valid(self.attrs, list)
        self.is_valid(self.order_by, str)
        self.is_valid(self.desc, bool)
        self.is_valid(self.output_type, str)

    def setup(self, conds, basic, attrs, order_by, desc, output_type):
        """Setup required parameters.

        :param dict conds: conditions
        :param list basic: basic user attrs.
                           (user_id, creation_date, credit, deposit, group_id,
                           group_name, isp_id, isp_name, nearest_exp_date,
                           recharge_deposit, status)
        :param list attrs: output of getUserInfo for complete list of attrs.
                           (normal_username, normal_password, first_login,
                           real_first_login, nearest_exp_date,
                           nearest_exp_date_epoch, time_to_nearest_exp_date,
                           charge_rule_usage, charge, last_renew,
                           abs_exp_date, assign_dns, assign_dns_1,
                           assign_dns_2, assign_ip, assign_netmask,
                           assign_route_ip, caller_id, fast_dial,
                           forward_number, asterisk_extension,
                           asterisk_ras_ip, asterisk_ras_id,
                           asterisk_ext_details, asterisk_sip_details,
                           asterisk_iax_details, asterisk_did_ras_ip,
                           asterisk_did_ras_id, comment, name, email, phone,
                           cell_phone, birthdate, address, postal_code,
                           credit_limit, exp_date_temp_extend,
                           temp_extend_log_id, exp_from_creation_date,
                           exp_from_first_login, exp_from_renew, exp_monthly,
                           extra_charge_profile, fast_dial, forward_number,
                           idle_threshold_timespan, idle_bytes_threshold,
                           idle_timeout, bw_send_rate, bw_receive_rate
                           in_ras_bw, in_ras_ippool, ippool, limit_caller_id,
                           limit_mac, limit_port, limit_ras, limit_ras,
                           limit_station_ip, limit_usage_days, lock,
                           assigned_endpoint, mc_charge, mc_charge_send_latin,
                           mc_charge_send_unicode, mc_charge_recv,
                           mc_min_user_credit, email_address, mail_quota,
                           mail_usage, mikrotik_address_list, mikrotik_bw,
                           mikrotik_bw_recv_rate, mikrotik_bw_send_rate,
                           mikrotik_bw_recv_burst, mikrotik_bw_send_burst,
                           mikrotik_bw_recv_burst_threshold,
                           mikrotik_bw_send_burst_threshold,
                           mikrotik_bw_recv_burst_time,
                           mikrotik_bw_send_burst_time,
                           mikrotik_bw_priority,
                           mikrotik_bw_min_recv_rate,
                           mikrotik_bw_min_send_rate,
                           multi_login,
                           notification_profile,
                           time_periodic_accounting_monthly,
                           time_periodic_accounting_monthly_limit,
                           time_periodic_accounting_monthly_usage,
                           time_periodic_accounting_monthly_reset,
                           traffic_periodic_accounting_monthly,
                           traffic_periodic_accounting_monthly_limit,
                           traffic_periodic_accounting_monthly_usage,
                           traffic_periodic_accounting_monthly_reset,
                           time_periodic_accounting_daily,
                           time_periodic_accounting_daily_limit,
                           time_periodic_accounting_daily_usage,
                           time_periodic_accounting_daily_reset,
                           traffic_periodic_accounting_daily,
                           traffic_periodic_accounting_daily_limit,
                           traffic_periodic_accounting_daily_usage,
                           traffic_periodic_accounting_daily_reset,
                           time_periodic_accounting_weekly,
                           time_periodic_accounting_weekly_limit,
                           time_periodic_accounting_weekly_usage,
                           time_periodic_accounting_weekly_reset,
                           traffic_periodic_accounting_weekly,
                           traffic_periodic_accounting_weekly_limit,
                           traffic_periodic_accounting_weekly_usage,
                           traffic_periodic_accounting_weekly_reset,
                           monthly_periodic_credit_change,
                           monthly_periodic_credit_change_day,
                           monthly_periodic_credit_change_type,
                           monthly_periodic_credit_change_amount,
                           monthly_periodic_credit_change_after_first_login,
                           monthly_periodic_credit_change_negate_credit,
                           monthly_periodic_credit_change_do_on_first_login,
                           monthly_periodic_credit_change_reset,
                           monthly_periodic_credit_change_reset,
                           daily_periodic_credit_change,
                           daily_periodic_credit_change_type,
                           daily_periodic_credit_change_amount,
                           daily_periodic_credit_change_after_first_login,
                           daily_periodic_credit_change_negate_credit,
                           daily_periodic_credit_change_do_on_first_login,
                           daily_periodic_credit_change_reset,
                           persistent_lan_ip, persistent_lan_mac,
                           persistent_lan_ras_ip, plan, radius_attrs,
                           rel_exp_date, rel_exp_date_unit,
                           rel_exp_date_negative_credit,
                           rel_exp_date_negative_credit_unit,
                           renew_next_group, second_normal_username,
                           serial, session_timeout, voip_preferred_language,
                           voip_username, negative_credit_start,
                           save_bw_usage, allow_user_disconnect,
                           deny_change_password, auto_renew,
                           reset_negative_credit_on_renew,
                           renew_do_not_reset_credit,
                           renew_do_not_reset_credit_on_state_package,
                           renew_do_not_reset_credit_on_state_recharged,
                           auto_renew_on_credit_finish
                           auto_renew_do_not_reset_credit
                           auto_recharge, allow_recharge_by_voucher,
                           prevent_web_login, enable_failed_login
                           ignore_idle_threshold_static_ip,
                           ignore_idle_threshold,
                           caller_id_bind_on_login,
                           limit_mac_bind_on_login,
                           limit_port_ibind_on_login,
                           limit_ras_bind_on_login,
                           limit_station_ip_bind_on_login,
                           limit_caller_id_allow_not_defined,
                           is_deposit_transferee,
                           is_deposit_transferer)
        :param str order_by: order by a field (normal_username,
                             voip_username, user_id, group_id,
                             creation_date, owner_id, credit, deposit,
                             first_login, serial, serial_numeric)
        :param bool desc: descending
        :param str output_type: output type (csv, pdf)

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.basic = basic
        self.attrs = attrs
        self.order_by = order_by
        self.desc = desc
        self.output_type = output_type
