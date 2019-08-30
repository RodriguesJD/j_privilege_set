from tool_box import tools
from xml.etree import ElementTree

ET = ElementTree
xml_text = tools.get_accounts_xml().text
xml_str = tools.xml_str(xml_text=xml_text)
privilege_set = xml_str
print(privilege_set)
print("\n\n\n")
header_priv_set = f"{privilege_set.split('</access_level>')[0]}</access_level>"

privilege_set_xml = "    <privilege_set>test_set</privilege_set>"

privileges = f"    <privileges>{privilege_set.split('<privileges>')[1].split('</privileges>')[0]}</privileges>"

footer_priv_set = "</account>"

put_xml_string = f"{header_priv_set}\n{privilege_set_xml}\n{privileges}\n{footer_priv_set}"


# TODO put the put_xml_string and see if that changes the name of the <privilege_set></privilege_set> if so check webUI
