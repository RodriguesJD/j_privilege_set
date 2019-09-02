from tool_box import tools

xml_text = tools.get_accounts_xml().text


# xml_user_info = tools.xml_user_info("Custom", xml_text)
#
# desktop_support_jss_objects = tools.desktop_support_jss_objects()
#
# desktop_support_jss_settings = tools.desktop_support_jss_settings()
#
# privileges = desktop_support_jss_objects + desktop_support_jss_settings
#
# wrapped_up_privileges = tools.privilege_wrapper(privileges)
#
# put_xml = xml_user_info + wrapped_up_privileges
#
# put = tools.put_trr_jamf(put_xml)
#
# print(put.status_code)





