from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import auth

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_PATH = "/home/jordan/Documents/Admin/keepass/.keepsync/" #client_secret.json path
CLIENT_FILE = 'client_secret.json' #name of your client_secret.json file
APPLICATION_NAME = 'Keepsync'
FILE_PATH = "/home/jordan/Documents/Admin/keepass/" #path to your kdbx file
FILE_NAME = 'kdbx_master.kdbx' #name of your kdbx file

full_client = CLIENT_PATH + CLIENT_FILE
full_file = FILE_PATH + FILE_NAME

#updates an existing kdbx file
def update_kdbx(id):
    file = drive_service.files().update(fileId=id, media_body=full_file, media_mime_type='application/octet-stream').execute()
    print('Updated', file.get('id'))

#creates and pushes a new kdbx file
def upload_kdbx():
    file_metadata = {'name' : FILE_NAME}
    file = drive_service.files().create(body=file_metadata, media_body=full_file, media_mime_type='application/octet-stream', fields='id').execute()
    print('Uploaded', file.get('id'))

#returns if a kdbx file of the name FILE_NAME is in google drive
def is_kdbx_found():
    page_token = None
    query = "name='" + FILE_NAME + "'"
    response = drive_service.files().list(q=query, spaces='drive', fields='nextPageToken, files(id, name)', pageToken = page_token).execute()
    if (len(response['files']) > 0):
        found = True
    else:
        found = False
    return found

#returns the hash of the kdbx file (queried by name=FILE_NAME)
def get_kdbx_id():
    page_token = None
    query = "name='" + FILE_NAME + "'"
    response = drive_service.files().list(q=query, spaces='drive', fields='nextPageToken, files(id, name)', pageToken = page_token).execute()
    return response.get('files', [])[0].get('id')

if __name__ == "__main__":
    auth_inst = auth.auth(SCOPES, full_client, APPLICATION_NAME)
    credentials = auth_inst.getCredentials(CLIENT_PATH)
    http = credentials.authorize(httplib2.Http())
    drive_service = discovery.build('drive', 'v3', http=http)
    if is_kdbx_found():
        update_kdbx(get_kdbx_id())
    else:
        upload_kdbx()
