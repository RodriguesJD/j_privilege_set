from tool_box import tools


xml_text = tools.get_accounts_xml().text

xml_user_info = tools.xml_user_info("Administrator", xml_text)

put_xml = xml_user_info + "</account>"

put = tools.put_trr_jamf(put_xml=put_xml)
print(put.status_code)






