from tool_box import tools


def test_get_accounts_xml():
    get_account = tools.get_accounts_xml()
    assert isinstance(get_account.text, str)
    assert get_account.status_code == 200


def test_xml_str():
    xml_text = tools.get_accounts_xml().text
    assert isinstance(xml_text, str)

    root = tools.xml_str(xml_text)
    assert isinstance(root, str)
