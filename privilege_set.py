from tool_box import tools
from xml.etree import ElementTree

ET = ElementTree
xml_text = tools.get_accounts_xml().text
xml_root = tools.xml_root(xml_text=xml_text)
print(xml_root)

