from tool_box import tools

xml_text = tools.get_accounts_xml().text

def test_get_accounts_xml():
    get_account = tools.get_accounts_xml()
    assert isinstance(get_account.text, str)
    assert get_account.status_code == 200


def test_xml_str():
    assert isinstance(xml_text, str)
    root = tools.xml_str(xml_text)
    assert isinstance(root, str)


def test_is_acceptable_privilege_set():
    assert tools.is_acceptable_privilege_set("Administrator")

    assert not tools.is_acceptable_privilege_set("bad priv set")


def test_xml_account_info():
    assert isinstance(tools.xml_user_info("Administrator", xml_text), str)

    assert not tools.xml_user_info("bad set", xml_text)
