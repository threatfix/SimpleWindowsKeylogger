-----------------------------------------------------
ThreatFix Simple Keylogger
-----------------------------------------------------

--------------
What is this?
--------------
This script performs the following functions:

1) Tracks user keystroke input and saves that input to local file (file path defined by user).  The local file can also be uploaded to DropBox every X seconds.
	
2) Creates a Windows registry runkey, executing this script on startup.
	
------
Usage
------
ThreatFix_Simple_Keylogger.py [Local|DropBox] [Filepath] [Optional:Persistent]

1) Local: Store the keystrokes in a text file at a specified path. [Filepath\ThreatFix_Keylogger_Log.txt]

2) DropBox: Sends the keystrokes to a text file at a specified path and uploads the file to DropBox every "n" seconds.
	Note: Must provide DropBox API key
	
3) Persistent:[Optional]This will add the keylogger to the Windows registry runkeys.

--------------
Requirements
--------------
The following are required for this keylogger to function:

1) Python 2.7: https://www.python.org/download/releases/2.7/
 	
2) dropbox-python-sdk: https://www.dropbox.com/developers-v1/core/sdks/python
	
 3) pyHook: http://sourceforge.net/projects/pyhook/
 	
 4) pywin32: http://sourceforge.net/projects/pywin32/
 	
	
ThreatFix is not responsible for any malicious use.  Be good pls.
Feel free to manipulate and improve on this. Send us your updates and we'll post them.
Original concept by: Ajin Abraham

-----------------------------------------------------
www.ThreatFix.com
-----------------------------------------------------
