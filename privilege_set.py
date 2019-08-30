from tool_box import tools



xml_text = tools.get_accounts_xml().text
print(tools.xml_account_info("Custom", xml_text))
