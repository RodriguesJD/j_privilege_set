import privilege_set


def test_get_accounts_xml():
    isinstance(privilege_set.get_accounts_xml().text, str)
