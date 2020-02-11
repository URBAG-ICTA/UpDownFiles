from paramiko import SSHClient
from scp import SCPClient

class UpDownFiles:
    
    ssh_host = ""
    ssh_user = ""
    ssh_password = ""
    ssh_port = 8122
    ssh = None
    

    def openConnection(self):
        self.ssh = SSHClient()         
        self.ssh.load_system_host_keys()
        self.ssh.connect(self.ssh_host, port = self.ssh_port, username = self.ssh_user, password = self.ssh_password, look_for_keys=False)
        

    def downloadFiles(self, origin, destination): #origin referes to a file on the remote server, destination a refers to the local
        scp = SCPClient(self.ssh.get_transport())
        
        for i in range(len(origin)):
            scp.get(origin[i], destination[i])
        
        scp.close()
    
    def uploadFiles(self, origin, destination): # origin referes to a local file and destination referes to a remote one
        scp = SCPClient(self.ssh.get_transport())
        
        for i in range(len(origin)):
            scp.put(origin[i], destination[i])
        
        scp.close()