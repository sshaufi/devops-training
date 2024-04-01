#!/usr/bin/env python3

import paramiko
import csv

# Define SSH credentials and hostnames
private_key_path = '/Users/ss/.ssh/id_ed25519'

# Define the local and remote paths for the Python script
local_python_script_path = './sys_reading.py'
remote_python_script_path = '/tmp/sys_reading.py'

# Function to connect via SSH and get system usage
def get_system_usage(hostname, username):
    try:
        # SSH Connection
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Load SSH private key
        private_key = paramiko.Ed25519Key.from_private_key_file(private_key_path)
        
        # Connect using SSH key
        
        if ":" in hostname:
            conn = hostname.split(":")
            ssh_client.connect(conn[0], username=username, pkey=private_key, port=conn[1])
        else:
            ssh_client.connect(hostname, username=username, pkey=private_key, port='22')


        # Transfer Python script to remote server
        sftp_client = ssh_client.open_sftp()
        sftp_client.put(local_python_script_path, remote_python_script_path)
        sftp_client.close()
        
        # Execute command to get system usage
        stdin, stdout, stderr = ssh_client.exec_command('python3 {}'.format(remote_python_script_path))
        output = stdout.read().decode("utf-8")
        
        # Close SSH connection
        ssh_client.close()
        
        return output
    except Exception as e:
        return str(e)


with open('./ansible-playbook/hosts.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("System usage for row ",row['group'],":")
        system_usage = get_system_usage(row['hostname'], row['ansible_user'])
        print(system_usage)
        print("-" * 50)



