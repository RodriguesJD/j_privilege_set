from tool_box import tools

# test that is_xml() works to validate xml

t = tools.is_xml("test")
print(t)


# xml_text = tools.get_accounts_xml().text
#
# xml_user_info = tools.xml_user_info("Custom", xml_text)
#
# desktop_support_jss_objects = tools.privilege_wrapper(tools.desktop_support_jss_objects())
#
# put_xml = xml_user_info + desktop_support_jss_objects
#
# put = tools.put_trr_jamf(put_xml)
#
# print(put.status_code)





