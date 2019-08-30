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


def xml_root(xml_text):
    root = ElementTree.fromstring(xml_text)
    return root


def xml_pprint():
    dom = xml.dom.minidom.parseString(get_accounts_xml().text)
    pretty_xml_as_string = dom.toprettyxml()
    return pretty_xml_as_string


def current_users_privileges():
    # TODO use the current privileges as a template for setting
    pass





