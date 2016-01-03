<p align="center"> 
<img src="http://i.imgur.com/lUBGmV8.png"></p>

### About
This script performs the following functions:
*Tracks user keystroke input and saves that input to local file (file path defined by user).  The local file can also be uploaded to DropBox every X seconds.
*Creates a Windows registry runkey, executing this script on startup.
	
### Usage
ThreatFix_Simple_Keylogger.py [Local|DropBox] [Filepath] [Optional:Persistent]
*Local: Store the keystrokes in a text file at a specified path. [Filepath\ThreatFix_Keylogger_Log.txt]
*DropBox: Sends the keystrokes to a text file at a specified path and uploads the file to DropBox every "n" seconds.
	Note: Must provide DropBox API key
*Persistent:[Optional]This will add the keylogger to the Windows registry runkeys.

### Requirements
The following are required for this keylogger to function:

*Python 2.7: https://www.python.org/download/releases/2.7/
*dropbox-python-sdk: https://www.dropbox.com/developers-v1/core/sdks/python
*pyHook: http://sourceforge.net/projects/pyhook/
*pywin32: http://sourceforge.net/projects/pywin32/
 	
ThreatFix is not responsible for any malicious use.  Be good pls.
Feel free to manipulate and improve on this. Send us your updates and we'll post them.
Original concept by: Ajin Abraham

### About
![ThreatFix](http://cdn1.editmysite.com/uploads/5/1/4/0/51408561/background-images/1387838909.png)


<p align="center"> 
Copyright (c) 2015 Paul Hutelmyer
<p align="center"> 
[Threatfix.com](http://www.threatfix.com)

