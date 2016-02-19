import threading
import paramiko
import subprocess
import sys

def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()
	#client.load_host_keys('/home/xxx/.ssh/known_hosts')
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username=user, password=passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.exec_command(command)
		print ssh_session.recv(1024)
	return

ip      = sys.argv[1]
user    = sys.argv[2]
passwd  = sys.argv[3]
command = sys.argv[4]

ssh_command(ip, user, passwd, command)
