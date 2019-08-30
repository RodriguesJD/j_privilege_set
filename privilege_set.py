from tool_box import tools


xml_text = tools.get_accounts_xml().text

xml_user_info = tools.xml_user_info("Custom", xml_text)




