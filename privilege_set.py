from tool_box import tools



xml_text = tools.get_accounts_xml().text

tools.xml_jss_objects(xml_text)
# def create_text_from_resp(xml_text):
#     with open("administrator_permissions.xml", "w") as f:
#         f.write(xml_text)



# xml_content = tools.get_accounts_xml().content
# # print(xml_text)
# desktop_supporl_sting_xml = ""
#
# parse_xml_text = xml_text.split('<privilege>')
# header = parse_xml_text[0]
# line_count = 0
# for line in parse_xml_text:
#     if line_count == 0:
#         desktop_supporl_sting_xml += line
#         line_count += 1
#     else:
#         if "Searches" in line:  # all users get full searches permissions
#             desktop_supporl_sting_xml += f"<privilege>{line}"
#         elif "Create" in line:
#             pass
#         elif "Update" in line:
#             pass
#         elif "Delete" in line:
#             pass
#         elif 'Read' in line:
#             desktop_supporl_sting_xml += f"<privilege>{line}"
#         elif 'jss_objects' in line:
#             print(line)
#         else:
#             desktop_supporl_sting_xml += f"<privilege>{line}"
#
# print(desktop_supporl_sting_xml)
# print(tools.xml_str(xml_text))
# # print(desktop_supporl_sting_xml)
# # t = tools.put_trr_jamf(desktop_supporl_sting_xml)
# # print(t.status_code)
#
#
# # with open('administrator_permissions.xml') as xml:
# #     header_priv_set = f"{xml_text.split('</ldap_server>')[0]}</ldap_server>"
# #
# #     privilege_set_xml = '<privilege_set>Custom</privilege_set>'
# #
# #     footer_priv_set = '</account>'
# #
# #     privileges = desktop_supporl_sting_xml
# #
# #     permissions = f"{header_priv_set}{privilege_set_xml}{privileges}{footer_priv_set}"
# #     print(permissions)
# #     t = tools.put_trr_jamf(permissions)
# #     print(t.status_code)
#
#
#
#
