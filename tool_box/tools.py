from pprint import pprint
from requests.auth import HTTPBasicAuth
import requests
import os
import sys
import xml.dom.minidom
from xml.etree import ElementTree
from typing import Type
from typing import Union
sys.path.insert(0, 'jamf_api_client/')
from jamf_api_client.core.get_jamf.accounts import Accounts


key = os.environ["JAMF_KEY"]
username = os.environ["JAMF_USERNAME"]
base_url = os.environ["JAMF_URL_PROD"]
user_id = os.environ["USER_ID_SET_TEST"]


def get_accounts_xml() -> object:
    """
    Get xml data from JAMF environment.

    :return: Response object from the request module
    """
    req = requests.get(f'{base_url}/accounts/userid/{user_id}', auth=HTTPBasicAuth(username, key),
                       headers={'Accept': 'application/xml'})
    return req


def put_trr_jamf(put_xml: str) -> object:
    """
    Put xml data on JAMF environment.

    :param put_xml: str
    :return: Response object from the request module
    """
    return requests.put(f'{base_url}/accounts/userid/{user_id}',
                        auth=HTTPBasicAuth(username, key), headers={'Content-Type': 'application/xml'}, data=put_xml)


def xml_str(xml_text: str) -> str:
    """
    Pretty print xml data from xml string.

    :param xml_text: str
    :return: str
    """
    dom = xml.dom.minidom.parseString(xml_text)
    pretty_xml_as_string = dom.toprettyxml()

    return pretty_xml_as_string


def is_acceptable_privilege_set(privilege_set: str) -> bool:
    """
    Validates if the privilege_set is correct.

    :param privilege_set: str
    :return: bool
    """
    acceptable_privilege_set = False
    privilege_sets = ["Administrator", "Auditor", "Enrollment Only", "Custom"]
    if privilege_set in privilege_sets:
        acceptable_privilege_set = True

    return acceptable_privilege_set


def xml_user_info(privilege_set: str, xml_text: str) -> Union[None, str]:
    """
    Gather users info from xml_text.

    :param privilege_set: str
    :param xml_text: str
    :return: str
    """
    pre_privlege_xml = None

    if is_acceptable_privilege_set(privilege_set):
        pre_privlege_xml = xml_text.split('<privilege_set>')[0]
        pre_privlege_xml += f"<privilege_set>{privilege_set}</privilege_set>"

    return pre_privlege_xml


def xml_user_privileges(xml_text: str) -> str:
    """
    Gathers the privileges data and adds accounts to close the xml tags.

    :param xml_text: str
    :return: str
    """
    privileges = xml_text.split("<privileges>")[1].split("</privileges>")[0]
    users_privileges = f"<privileges>{privileges}</privileges></account>"

    return users_privileges


def xml_jss_objects(xml_text: str) -> str:
    """
    Gathers the jss_objects data.

    :param xml_text: str
    :return: str
    """
    jamf_pro_server_objects = xml_text.split("<jss_objects>")[1].split("</jss_objects>")[0]
    jss_objects = f"<jss_objects>{jamf_pro_server_objects}</jss_objects>"

    return jss_objects


def xml_jss_settings(xml_text: str) -> str:
    """
    Gathers the jss_settings data.

    :param xml_text: str
    :return: str
    """
    jamf_pro_server_settings = xml_text.split("<jss_settings>")[1].split("</jss_settings>")[0]
    jss_settings = f"<jss_settings>{jamf_pro_server_settings}</jss_settings>"

    return jss_settings


def xml_jss_actions(xml_text: str) -> str:
    """
    Gathers the jss_actions data.

    :param xml_text: str
    :return: str
    """
    jamf_pro_server_actions = xml_text.split("<jss_actions>")[1].split("</jss_actions>")[0]
    jss_actions = f"<jss_actions>{jamf_pro_server_actions}</jss_actions>"

    return jss_actions


def xml_recon(xml_text: str) -> str:
    """
    Gathers the jss_recon data.

    :param xml_text: str
    :return: str
    """
    jamf_pro_recon = xml_text.split("<recon>")[1].split("</recon>")[0]
    recon = f"<recon>{jamf_pro_recon}</recon>"

    return recon


def xml_casper_admin(xml_text: str) -> str:
    """
    Gathers the casper_admin data.

    :param xml_text: str
    :return: str
    """
    jamf_admin = xml_text.split("<casper_admin>")[1].split("</casper_admin>")[0]
    casper_admin = f"<casper_admin>{jamf_admin}</casper_admin>"

    return casper_admin


def xml_casper_remote(xml_text: str) -> str:
    """
    Gathers the casper_remote data.

    :param xml_text: str
    :return: str
    """
    jamf_remote = xml_text.split("<casper_remote>")[1].split("</casper_remote>")[0]
    casper_remote = f"<casper_remote>{jamf_remote}</casper_remote>"

    return casper_remote


def xml_casper_imaging(xml_text: str) -> str:
    """
    Gathers the casper_imaging data.

    :param xml_text: str
    :return: str
    """
    jamf_imaging = xml_text.split("<casper_imaging>")[1].split("</casper_imaging>")[0]
    casper_imaging = f"<casper_imaging>{jamf_imaging}</casper_imaging>"

    return casper_imaging


def privilege_wrapper(xml_text: str) -> str:
    """
    Wraps the xml_text in privileges tags and closes the account tag since privileges is always the second to last tag.

    :param xml_text: str
    :return: str
    """
    return f"<privileges>{xml_text}</privileges></account>"

