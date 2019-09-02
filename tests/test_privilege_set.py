from tool_box import tools

xml_text = tools.get_accounts_xml().text


def test_get_accounts_xml():
    get_account = tools.get_accounts_xml()
    assert isinstance(get_account.text, str)
    assert get_account.status_code == 200


def test_put_trr_jamf():
    # TODO create test for put_trr_jamf
    pass


def test_xml_str():
    assert isinstance(xml_text, str)
    root = tools.xml_str(xml_text)
    assert isinstance(root, str)


def test_is_acceptable_privilege_set():
    assert tools.is_acceptable_privilege_set("Administrator")

    assert not tools.is_acceptable_privilege_set("bad priv set")


def test_is_xml():
    good_xml = tools.desktop_support_jss_objects()
    assert tools.is_xml(good_xml)

    not_xml = "This is not xml"
    assert not tools.is_xml(not_xml)


def test_xml_account_info():
    assert isinstance(tools.xml_user_info("Administrator", xml_text), str)

    assert not tools.xml_user_info("bad set", xml_text)


def test_xml_user_privileges():
    assert tools.xml_user_privileges(xml_text)


def test_xml_jss_objects():
    assert tools.xml_jss_objects(xml_text)


def test_xml_jss_settings():
    assert tools.xml_jss_settings(xml_text)


def test_xml_jss_actions():
    assert tools.xml_jss_actions(xml_text)


def test_xml_recon():
    assert tools.xml_recon(xml_text)


def test_xml_casper_admin():
    assert tools.xml_casper_admin(xml_text)


def test_xml_casper_remote():
    assert tools.xml_casper_remote(xml_text)


def test_xml_casper_imaging():
    assert tools.xml_casper_imaging(xml_text)


def test_privilege_wrapper():
    assert tools.privilege_wrapper(xml_text)
