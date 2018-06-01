# Keepsync

Keepsync is a utility for [KeePass](https://keepass.info).
KeePass is an open source password manager.

A problem that I had with KeePass was syncing my devices (Android, Linux, Mac and Windows). I developed this application to upload my kdbx file to Google Drive where my other devices could source the file from.
I personally use KeePassDroid. The reason this script is useful is because you can set Database content provider to source from that Google Drive kdbx file.

Usage is as easy as updating your file through KeePass and then:
'''bash
$ keepsync
'''

## Installation
1. Clone this repository.
2. Create a file structure that you like.
3. Remember to change the variables in main.py to reflect the changes from 2!
4. Generate a client_secrets.json file.
5. Install all the dependencies for the python script.
6. (Optional) Create the aliases detailed in the [aliases section](https://github.com/FueledbyJordan/keepsync/README.md#aliases). Remember to source bash if you do so.
7. Run the script. It will open your preferred browser and ask for permissions to read and write to your Google Drive.
8. The script should write the file to your Google Drive!

---

## Aliases

'''bash
alias keepass="keepass <PATH_TO_YOUR_KDBX_FILE> &"
alias keepsync="python3 <PATH_TO_main.py>"
'''
