from pprint import pprint
from requests.auth import HTTPBasicAuth
import requests
import os
import sys
import xml.dom.minidom
from xml.etree import ElementTree
from typing import Type
sys.path.insert(0, 'jamf_api_client/')
from jamf_api_client.core.get_jamf.accounts import Accounts


key = os.environ["JAMF_KEY"]
username = os.environ["JAMF_USERNAME"]
base_url = os.environ["JAMF_URL_PROD"]
user_id = os.environ["USER_ID_SET_TEST"]


def get_accounts_xml():
    req = requests.get(f'{base_url}/accounts/userid/{user_id}', auth=HTTPBasicAuth(username, key),
                       headers={'Accept': 'application/xml'})
    return req


def put_trr_jamf(put_xml: str):
    return requests.put(f'{base_url}/accounts/userid/{user_id}',
                        auth=HTTPBasicAuth(username, key), headers={'Content-Type': 'application/xml'}, data=put_xml)


def xml_str(xml_text):
    dom = xml.dom.minidom.parseString(xml_text)
    pretty_xml_as_string = dom.toprettyxml()

    return pretty_xml_as_string


def is_acceptable_privilege_set(privilege_set):
    acceptable_privilege_set = False
    privilege_sets = ["Administrator", "Auditor", "Enrollment Only", "Custom"]
    if privilege_set in privilege_sets:
        acceptable_privilege_set = True

    return acceptable_privilege_set


def xml_user_info(privilege_set, xml_text):
    """
    Gather users info from xml_text.
    """
    pre_privlege_xml = None

    if is_acceptable_privilege_set(privilege_set):
        pre_privlege_xml = xml_text.split('<privilege_set>')[0]
        pre_privlege_xml += f"<privilege_set>{privilege_set}</privilege_set>"

    return pre_privlege_xml


def xml_user_privileges(xml_text):
    privileges = xml_text.split("<privileges>")[1].split("</privileges>")[0]
    users_privileges = f"<privileges>{privileges}</privileges></account>"

    return users_privileges






