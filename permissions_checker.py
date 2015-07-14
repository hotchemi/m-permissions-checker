# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
from xml.etree import ElementTree


BLACK_LIST = (
    'android.permission.READ_EXTERNAL_STORAGE',
    'android.permission.WRITE_EXTERNAL_STORAGE',
    'android.permission.READ_CALENDAR',
    'android.permission.WRITE_CALENDAR',
    'android.permission.CAMERA',
    'android.permission.READ_CONTACTS',
    'android.permission.WRITE_CONTACTS',
    'android.permission.READ_PROFILE',
    'android.permission.WRITE_PROFILE',
    'android.permission.ACCESS_FINE_LOCATION',
    'android.permission.ACCESS_COARSE_LOCATION',
    'android.permission.RECORD_AUDIO'
    'android.permission.READ_PHONE_STATE',
    'android.permission.CALL_PHONE',
    'android.permission.READ_CALL_LOG',
    'android.permission.WRITE_CALL_LOG',
    'com.android.voicemail.permission.ADD_VOICEMAIL',
    'android.permission.USE_SIP',
    'android.permission.PROCESS_OUTGOING_CALLS',
    'android.permission.BODY_SENSORS',
    'android.permission.USE_FINGERPRINT',
    'android.permission.SEND_SMS',
    'android.permission.RECEIVE_SMS',
    'android.permission.READ_SMS',
    'android.permission.RECEIVE_WAP_PUSH',
    'android.permission.RECEIVE_MMS',
    'android.permission.READ_CELL_BROADCASTS')

TARGET_FILE_NAME = 'AndroidManifest.xml'


def _manifest_files():
    manifests = []
    exclude = "build"
    for root, dirs, files in os.walk(os.getcwd()):
        if exclude in dirs:
            dirs.remove(exclude)
        for file in files:
            if file == TARGET_FILE_NAME:
                manifests.append(os.path.join(root, file))
    return manifests


def _permissions(path):
    permissions = []
    tree = ElementTree.parse(path)
    es = tree.getroot().findall('.//uses-permission')
    for e in es:
        permission = e.attrib.values().pop();
        if permission in BLACK_LIST:
            permissions.append(e.attrib.values().pop())
    return permissions


def _print_warning(str):
    print('\033[93m' + str + '\033[0m')


if __name__ == '__main__':
    for manifest in _manifest_files():
        print("Searching file: %s" % manifest)
        permissions = _permissions(manifest)
        if permissions:
            print("Unfortunately, you have to handle these permissions in MNC.")
            _print_warning('\n'.join(map(str, permissions)))
        else:
            print("Congratulations! You don't have to write any codes!")
