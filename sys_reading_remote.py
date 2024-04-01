#!/usr/bin/env python3
import paramiko


# Define SSH credentials and hostnames
private_key_path = '/Users/ss/.ssh/id_ed25519'
ssh_credentials = {
    'cloud.ss.fish': {'username': 'ansible', 'port':22},
    'ss.fish': {'username': 'ansible', 'port':7394}
}

# Define the local and remote paths for the Python script
local_python_script_path = './sys_reading.py'
remote_python_script_path = '/tmp/sys_reading.py'

# Function to connect via SSH and get system usage
def get_system_usage(hostname, username, port):
    try:
        # SSH Connection
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Load SSH private key
        private_key = paramiko.Ed25519Key.from_private_key_file(private_key_path)
        
        # Connect using SSH key
        ssh_client.connect(hostname, username=username, pkey=private_key, port=port)

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


print("-" * 50)
for hostname, creds in ssh_credentials.items():
    print(f"System usage for {hostname}:")
    system_usage = get_system_usage(hostname, creds['username'], creds['port'])
    print(system_usage)
    print("-" * 50)

