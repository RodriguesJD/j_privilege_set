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


def xml_account_info(privilege_set, xml_text):
    """
    Parse xml_text and pass in the privilage_set var. Privilege set must be an excising option.
    :param privilege_set:
    :param xml_text:
    :return:
    """
    xml_account_info_header = xml_text.split('<privilege_set>')[0]

    priv_set = f"<privilege_set>{privilege_set}</privilege_set>"

    return xml_account_info_header + priv_set







