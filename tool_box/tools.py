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


def is_xml_str(xml_to_check: str) -> bool:
    """
    Check to see that the string is formatted for xml.

    :param xml_to_check: str
    :return: bool
    """
    try:
        ElementTree.fromstring(xml_to_check)
        xml_status = True
    except ElementTree.ParseError:
        xml_status = False

    return xml_status


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


def desktop_support_jss_objects():
    """
    Desktop support privileges for Jamf Pro Server Objects.
    :return: str
    """
    privs = "<jss_objects>" \
            "<privilege>Create Advanced Computer Searches" \
            "</privilege><privilege>Read Advanced Computer Searches" \
            "</privilege><privilege>Update Advanced Computer Searches" \
            "</privilege><privilege>Delete Advanced Computer Searches</privilege>" \
            "<privilege>Create Advanced Mobile Device Searches</privilege>" \
            "<privilege>Read Advanced Mobile Device Searches</privilege>" \
            "<privilege>Update Advanced Mobile Device Searches</privilege>" \
            "<privilege>Delete Advanced Mobile Device Searches</privilege>" \
            "<privilege>Create Advanced User Searches</privilege>" \
            "<privilege>Read Advanced User Searches</privilege>" \
            "<privilege>Update Advanced User Searches</privilege>" \
            "<privilege>Delete Advanced User Searches</privilege>" \
            "<privilege>Create Advanced User Content Searches</privilege>" \
            "<privilege>Read Advanced User Content Searches</privilege>" \
            "<privilege>Update Advanced User Content Searches</privilege>" \
            "<privilege>Delete Advanced User Content Searches</privilege>" \
            "<privilege>Read AirPlay Permissions</privilege>" \
            "<privilege>Read Allowed File Extension</privilege>" \
            "<privilege>Read_API_Integrations</privilege>" \
            "<privilege>Read Attachment Assignments</privilege>" \
            "<privilege>Read Buildings</privilege><privilege>Read Categories</privilege><privilege>Read Classes</privilege><privilege>Read Computer Enrollment Invitations</privilege><privilege>Read Computer PreStage Enrollments</privilege><privilege>Read Computers</privilege><privilege>Read Configurations</privilege><privilege>Read Departments</privilege><privilege>Read Device Enrollment Program Instances</privilege><privilege>Read Device Name Patterns</privilege><privilege>Read Directory Bindings</privilege><privilege>Read Disk Encryption Configurations</privilege><privilege>Read Disk Encryption Institutional Configurations</privilege><privilege>Read Dock Items</privilege><privilege>Read eBooks</privilege><privilege>Read Enrollment Profiles</privilege><privilege>Read Computer Extension Attributes</privilege><privilege>Read Patch External Source</privilege><privilege>Read File Attachments</privilege><privilege>Read Distribution Points</privilege><privilege>Read Push Certificates</privilege><privilege>Read iBeacon</privilege><privilege>Read Infrastructure Managers</privilege><privilege>Read Inventory Preload Records</privilege><privilege>Read Accounts</privilege><privilege>Read JSON Web Token Configuration</privilege><privilege>Read Keystores</privilege><privilege>Read LDAP Servers</privilege><privilege>Read Licensed Software</privilege><privilege>Read Mac Applications</privilege><privilege>Read macOS Configuration Profiles</privilege><privilege>Read Maintenance Pages</privilege><privilege>Read Managed Preference Profiles</privilege><privilege>Read Mobile Device Applications</privilege><privilege>Read iOS Configuration Profiles</privilege><privilege>Read Mobile Device Enrollment Invitations</privilege><privilege>Read Mobile Device Extension Attributes</privilege><privilege>Read Mobile Device Managed App Configurations</privilege><privilege>Read Mobile Device PreStage Enrollments</privilege><privilege>Read Mobile Devices</privilege><privilege>Read NetBoot Servers</privilege><privilege>Read Network Integration</privilege><privilege>Read Network Segments</privilege><privilege>Read Packages</privilege><privilege>Read Patch Management Software Titles</privilege><privilege>Read Patch Policies</privilege><privilege>Read Peripheral Types</privilege><privilege>Read Personal Device Configurations</privilege><privilege>Read Personal Device Profiles</privilege><privilege>Read Policies</privilege><privilege>Read PreStages</privilege><privilege>Read Printers</privilege><privilege>Read Provisioning Profiles</privilege><privilege>Read Push Certificates</privilege><privilege>Read Removable MAC Address</privilege><privilege>Read Restricted Software</privilege><privilege>Read Scripts</privilege><privilege>Read Self Service Bookmarks</privilege><privilege>Read Self Service Branding Configuration</privilege><privilege>Read Sites</privilege><privilege>Read Smart Computer Groups</privilege><privilege>Read Smart Mobile Device Groups</privilege><privilege>Read Smart User Groups</privilege><privilege>Read Static Computer Groups</privilege><privilege>Read Static Mobile Device Groups</privilege><privilege>Read Static User Groups</privilege><privilege>Read User Extension Attributes</privilege><privilege>Read User</privilege><privilege>Read VPP Administrator Accounts</privilege><privilege>Read VPP Assignment</privilege><privilege>Read VPP Invitations</privilege><privilege>Read Webhooks</privilege>" \
            "</jss_objects>"

    return privs


def xml_jss_settings(xml_text: str) -> str:
    """
    Gathers the jss_settings data.

    :param xml_text: str
    :return: str
    """
    jamf_pro_server_settings = xml_text.split("<jss_settings>")[1].split("</jss_settings>")[0]
    jss_settings = f"<jss_settings>{jamf_pro_server_settings}</jss_settings>"

    return jss_settings


def desktop_support_jss_settings() -> str:
    """
    Desktop support privileges for Jamf Pro Server Settings.
    :return: str
    """
    desktop_settings = "<jss_settings>" \
                       "<privilege>Read Activation Code</privilege>" \
                       "<privilege>Read Apache Tomcat Settings</privilege>" \
                       "<privilege>Read Apple Configurator Enrollment</privilege>" \
                       "<privilege>Read Education Settings</privilege>" \
                       "<privilege>Read Mobile Device App Maintenance Settings</privilege>" \
                       "<privilege>Read Autorun Imaging</privilege>" \
                       "<privilege>Read Cache</privilege>" \
                       "<privilege>Read Change Management</privilege>" \
                       "<privilege>Read Computer Check-In</privilege>" \
                       "<privilege>Read Cloud Distribution Point</privilege>" \
                       "<privilege>Read Clustering</privilege>" \
                       "<privilege>Read Computer Inventory Collection</privilege>" \
                       "<privilege>Read Conditional Access</privilege>" \
                       "<privilege>Read Customer Experience Metrics</privilege>" \
                       "<privilege>Read Engage Settings</privilege>" \
                       "<privilege>Read GSX Connection</privilege>" \
                       "<privilege>Read Patch Internal Source</privilege>" \
                       "<privilege>Read Jamf Imaging</privilege>" \
                       "<privilege>Read Parent App Settings</privilege>" \
                       "<privilege>Read JSS URL</privilege>" \
                       "<privilege>Read Limited Access Settings</privilege>" \
                       "<privilege>Read Retention Policy</privilege>" \
                       "<privilege>Read Mobile Device Inventory Collection</privilege>" \
                       "<privilege>Read Password Policy</privilege>" \
                       "<privilege>Read Patch Management Settings</privilege>" \
                       "<privilege>Read PKI</privilege>" \
                       "<privilege>Read Re-enrollment</privilege>" \
                       "<privilege>Read Computer Security</privilege>" \
                       "<privilege>Read Self Service</privilege>" \
                       "<privilege>Read App Request Settings</privilege>" \
                       "<privilege>Read Mobile Device Self Service</privilege>" \
                       "<privilege>Read SSO Settings</privilege>" \
                       "<privilege>Read SMTP Server</privilege>" \
                       "<privilege>Read SSO Settings</privilege>" \
                       "<privilege>Read User-Initiated Enrollment</privilege>" \
                       "</jss_settings>"

    return desktop_settings


def xml_jss_actions(xml_text: str) -> str:
    """
    Gathers the jss_actions data.

    :param xml_text: str
    :return: str
    """
    jamf_pro_server_actions = xml_text.split("<jss_actions>")[1].split("</jss_actions>")[0]
    jss_actions = f"<jss_actions>{jamf_pro_server_actions}</jss_actions>"

    return jss_actions


def desktop_support_jss_actions() -> str:
    """
    Desktop support privileges for Jamf Pro Server Actions.
    :return: str
    """
    desktop_support_actions = "<jss_actions>" \
                              "<privilege>Allow User to Enroll</privilege>" \
                              "<privilege>Assign Users to Mobile Devices</privilege>" \
                              "<privilege>Change Password</privilege>" \
                              "<privilege>Dismiss Notifications</privilege>" \
                              "<privilege>Enroll Computers and Mobile Devices</privilege>" \
                              "<privilege>Remove restrictions set by Jamf Parent</privilege>" \
                              "<privilege>Send Blank Pushes to Mobile Devices</privilege>" \
                              "<privilege>Send Computer Bluetooth Command</privilege>" \
                              "<privilege>Send Computer Delete User Account Command</privilege>" \
                              "<privilege>Send Computer Remote Command to Download and Install OS X Update</privilege>" \
                              "<privilege>Send Computer Remote Desktop Command</privilege>" \
                              "<privilege>Send Computer Remote Lock Command</privilege>" \
                              "<privilege>Send Computer Remote Wipe Command</privilege>" \
                              "<privilege>Send Computer Unlock User Account Command</privilege>" \
                              "<privilege>Send Computer Unmanage Command</privilege>" \
                              "<privilege>Send Email to End Users via JSS</privilege>" \
                              "<privilege>Send Inventory Requests to Mobile Devices</privilege>" \
                              "<privilege>Send Messages to Self Service Mobile</privilege>" \
                              "<privilege>Send Mobile Device Bluetooth Command</privilege>" \
                              "<privilege>Send Mobile Device Diagnostics and Usage Reporting and App Analytics Commands</privilege>" \
                              "<privilege>Send Mobile Device Disable Data Roaming Command</privilege>" \
                              "<privilege>Send Mobile Device Disable Voice Roaming Command</privilege>" \
                              "<privilege>Send Mobile Device Enable Data Roaming Command</privilege>" \
                              "<privilege>Send Mobile Device Enable Voice Roaming Command</privilege>" \
                              "<privilege>Send Mobile Device Lost Mode Command</privilege>" \
                              "<privilege>Send Mobile Device Managed Settings Command</privilege>" \
                              "<privilege>Send Mobile Device Mirroring Command</privilege>" \
                              "<privilege>Send Mobile Device Personal Hotspot Command</privilege>" \
                              "<privilege>Send Mobile Device Remote Command to Download and Install iOS Update</privilege>" \
                              "<privilege>Send Mobile Device Remote Lock Command</privilege>" \
                              "<privilege>Send Mobile Device Remote Wipe Command</privilege>" \
                              "<privilege>Send Mobile Device Remove Passcode Command</privilege>" \
                              "<privilege>Send Mobile Device Remove Restrictions Password Command</privilege>" \
                              "<privilege>Send Mobile Device Restart Device Command</privilege>" \
                              "<privilege>Send Mobile Device Set Activation Lock Command</privilege>" \
                              "<privilege>Send Mobile Device Set Device Name Command</privilege>" \
                              "<privilege>Send Mobile Device Set Wallpaper Command</privilege>" \
                              "<privilege>Send Mobile Device Shared iPad Commands</privilege>" \
                              "<privilege>Send Mobile Device Shut Down Command</privilege>" \
                              "<privilege>Send Update Passcode Lock Grace Period Command</privilege>" \
                              "<privilege>Unmanage Mobile Devices</privilege>" \
                              "<privilege>View Activation Lock Bypass Code</privilege>" \
                              "<privilege>View Disk Encryption Recovery Key</privilege>" \
                              "<privilege>View Event Logs</privilege><" \
                              "privilege>View JSS Information</privilege>" \
                              "<privilege>View License Serial Numbers</privilege>" \
                              "<privilege>View Mobile Device Lost Mode Location</privilege>" \
                              "</jss_actions>"

    return desktop_support_actions


def xml_recon(xml_text: str) -> str:
    """
    Gathers the jss_recon data.

    :param xml_text: str
    :return: str
    """
    jamf_pro_recon = xml_text.split("<recon>")[1].split("</recon>")[0]
    recon = f"<recon>{jamf_pro_recon}</recon>"

    return recon


def desktop_support_recon() -> str:
    """
    Desktop support privileges for recon.

    :return: str
    """
    recon = "<recon>" \
            "<privilege>Add Computers Remotely</privilege>" \
            "<privilege>Create QuickAdd Packages</privilege>" \
            "</recon>"

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


def desktop_support_casper_admin() -> str:
    """
    Desktop support privileges for jamf admin.
    :return: str
    """
    casper_admin = "<casper_admin>" \
                   "<privilege>Use Casper Admin</privilege>" \
                   "<privilege>Save With Casper Admin</privilege>" \
                   "</casper_admin>"

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


def desktop_support_casper_remote():
    """
    Desktop support privileges for casper_remote.
    :return: str
    """
    jamf_remote = "<casper_remote>" \
                  "<privilege>Use Casper Remote</privilege>" \
                  "<privilege>Install/Uninstall Software Remotely</privilege>" \
                  "<privilege>Run Scripts Remotely</privilege>" \
                  "<privilege>Map Printers Remotely</privilege>" \
                  "<privilege>Add Dock Items Remotely</privilege>" \
                  "<privilege>Manage Local User Accounts Remotely</privilege>" \
                  "<privilege>Change Management Account Remotely</privilege>" \
                  "<privilege>Bind to Active Directory Remotely</privilege>" \
                  "<privilege>Set Open Firmware/EFI Passwords Remotely</privilege>" \
                  "<privilege>Reboot Computers Remotely</privilege>" \
                  "<privilege>Perform Maintenance Tasks Remotely</privilege>" \
                  "<privilege>Search for Files/Processes Remotely</privilege>" \
                  "<privilege>Enable Disk Encryption Configurations Remotely</privilege>" \
                  "<privilege>Screen Share with Remote Computers</privilege>" \
                  "<privilege>Screen Share with Remote Computers Without Asking</privilege>" \
                  "</casper_remote>"

    return jamf_remote


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


# TODO need context for priviledge set. Desktop will fail some tests cuase they dont have those tags