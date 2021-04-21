
import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ip address', 22, 'user', 'password')
stdin, stdout, stderr = ssh.exec_command('show version')
time.sleep(5)	#有bug，需要等待一段时间之后打印
print(stdout.read().decode('utf-8'))    # 以utf-8编码对结果进行解码
ssh.close()