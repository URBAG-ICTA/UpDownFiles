UPDownFiles
==========
This project provides a python class that aims to help downloading and uploading files via scp.

## Usage example

import the library
```
from UpDownFiles import UpDownFiles as UD
```

Create an object UPDownFiles
set up the connection parameters host, user, password and port
open the ssh caonnection.
```
ud = UD()

ud.ssh_host = ""
ud.ssh_user = ""
ud.ssh_password = ""

ud.openConnection()
'''







