from tool_box import tools

xml_text = tools.get_accounts_xml().text

xml_user_info = tools.xml_user_info("Custom", xml_text)

desktop_support_jss_objects = tools.desktop_support_jss_objects()

desktop_support_jss_settings = tools.desktop_support_jss_settings()

desktop_support_jss_actions = tools.desktop_support_jss_actions()

desktop_support_recon = tools.xml_recon(xml_text)

desktop_support_jamf_admin = tools.xml_casper_admin(xml_text)

print(desktop_support_recon)
print(tools.is_xml_str(tools.xml_recon(xml_text)))

print("\n")
print(desktop_support_jamf_admin)
print(tools.is_xml_str(tools.xml_casper_admin(xml_text)))
# privileges = desktop_support_jss_objects + desktop_support_jss_settings + desktop_support_jss_actions
#
# wrapped_up_privileges = tools.privilege_wrapper(privileges)
#
# put_xml = xml_user_info + wrapped_up_privileges
#
# put = tools.put_trr_jamf(put_xml)
#
# print(put.status_code)





