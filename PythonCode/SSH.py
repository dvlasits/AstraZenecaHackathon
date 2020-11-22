import paramiko as paramiko
import pickle


class OnlineInterface:

    def putData(self, data):
        host = "files.srcf.net"
        port = 22
        username = "dv323"
        password = "*******"

        command = "ls"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)

        with open('test.pkl', 'wb') as f:
            pickle.dump(data, f)


        sftp = ssh.open_sftp()
        sftp.put("test.pkl", "test.pkl")
        sftp.close()
        ssh.close()

    def getData(self):
        host = "files.srcf.net"
        port = 22
        username = "dv323"
        password = "kikirik567"

        command = "ls"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)

        sftp = ssh.open_sftp()
        sftp.get("test.pkl", "test.pkl")
        sftp.close()
        ssh.close()
        with open('test.pkl', 'rb') as f:
            return pickle.load(f)
