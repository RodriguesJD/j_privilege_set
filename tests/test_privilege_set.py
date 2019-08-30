from tool_box import tools


def test_get_accounts_xml():
    isinstance(tools.get_accounts_xml().text, str)
