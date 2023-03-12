# sshbrutty
This is a Python script based on the one from TCM Academy's Python101 course that performs a brute force attack on an SSH server by attempting to login with a list of passwords.

I added to the original script and it now prompts the user to provide the username, host, and password list file as arguments. 

The script stops when a valid password is found or when all passwords in the list have been tried.

## Dependencies
This script requires Python 3 and the following packages:

- argparse
- paramiko
- pwn


You can run the script with the command: 

```python
sshbrutty.py --user USERNAME --host IP --password-file /path/to/password/file.txt 
```

replacing USERNAME, IP, and /path/to/password/file.txt with the appropriate values.

## Disclaimer
This script should only be used for educational or testing purposes on systems for which you have permission to perform a brute force attack.
