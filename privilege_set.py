from tool_box import tools

xml_text = tools.get_accounts_xml().text

xml_user_info = tools.xml_user_info("Custom", xml_text)

desktop_support_jss_objects = tools.desktop_support_jss_objects()

desktop_support_jss_settings = tools.desktop_support_jss_settings()

desktop_support_jss_actions = tools.desktop_support_jss_actions()

desktop_support_recon = tools.desktop_support_recon()

desktop_support_jamf_admin = tools.desktop_support_casper_admin()

desktop_support_casper_remote = tools.desktop_support_casper_remote()


privileges = desktop_support_jss_objects + \
             desktop_support_jss_settings + \
             desktop_support_jss_actions

wrapped_up_privileges = tools.privilege_wrapper(privileges)

put_xml = xml_user_info + wrapped_up_privileges

put = tools.put_trr_jamf(put_xml)

print(put.status_code)

make_user_admin_prompt = input("type yes to make user an admin")
if make_user_admin_prompt == 'yes':
    tools.make_user_admin(xml_text)






