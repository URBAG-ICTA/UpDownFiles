UPDownFiles
==========
This project provides a python class that aims to help downloading and uploading files via scp.

## Usage example

import the library
```
from UpDownFiles import UpDownFiles as UD
```

Create an object UPDownFiles
set up the connection parameters *host*, *user*, *password* and *port*
open the ssh caonnection.
```
ud = UD()

ud.ssh_host = ""
ud.ssh_user = ""
ud.ssh_password = ""
ud.ssh_port = 22

ud.openConnection()
```

## Upload Files
Create a python list with all the files you want to download from your remote server, and a list with the corresponding names you want them to get on yout local computer.
```
localFiles = ["./uploadTest1.txt", "./uploadTest2.txt"]
remoteFiles = ["~/uploadTest1.txt", "~/uploadTest2.txt"]
```
And finally upload the files
```
ud.uploadFiles(localFiles, remoteFiles)
```

## Download Files
Create a python list wih all the files you want to upload from your local computer, an a list with the corresponding names you want them to have on the remte server
```
remoteFiles = ["~/uploadTest1.txt", "~/uploadTest2.txt"]
localFiles = ["./NEW_uploadTest1.txt", "./NEW_uploadTest2.txt"]

ud.downloadFiles(remoteFiles, localFiles)
```







