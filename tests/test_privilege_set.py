from tool_box import tools


def test_get_accounts_xml():
    get_account = tools.get_accounts_xml()
    isinstance(get_account.text, str)
    assert get_account.status_code == 200


def test_xml_root():
    xml_text = tools.get_accounts_xml().text
    isinstance(xml_text, str)
    root = tools.xml_root(xml_text)

    # xml_root returns xml class object
    assert str(type(root)) == "<class 'xml.etree.ElementTree.Element'>"
