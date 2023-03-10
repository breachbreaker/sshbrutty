# sshbrutty
This is a Python script that performs a brute force attack on an SSH server by attempting to login with a list of passwords. 

The script prompts the user to provide the username, host, and password list file as arguments. It uses the paramiko library to establish an SSH connection and the pwn library to display messages during the brute force attack. 

The script stops when a valid password is found or when all passwords in the list have been tried

You can run the script with the command: 

sshbrutty.py --user USERNAME --host IP --password-file /path/to/password/file.txt 

replacing USERNAME, IP, and /path/to/password/file.txt with the appropriate values.
