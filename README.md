# DevOps Training
This repository serves as a platform for my personal DevOps training, showcasing my skills in scripting and DevOps tools. Its primary objectives are:

1. **Self-Training:** To train myself in DevOps tasks.
2. **Skill Demonstration:** To demonstrate my capabilities in DevOps tools and scripting to potential employers and collaborators.
3. **Personal Future Reference:** This repository will be used by me for future reference and for future projects.

## Issue Description
1. **Servers Updates:** Simplify the update process for two of my personal servers and AWS EC2 server.
2. **Automated AWS EC2 Setup:** Implement automated setup, and destruction of Ubuntu servers on AWS EC2.
3. **Remote Server Monitoring:** Monitor system status from all servers remotely, no direct access needed.
4. **Simple Execution:** Execute all tasks with a simple command-line interface.
5. **Keep it Simple:** I am aiming to make the scripts and codes as simple and readable as possible.

## Solution
Since I try to keep it simple, I aim to maintain the scripts and code with minimal dependencies possible. Additionally, it's important that they remain readable without excessive commenting. I will thoroughly explain the solution on each section.

Throughout this README, I will reference three servers. Please refer to the table below. I will refer to the servers by their names.

| Name| Hostname|os| Comments|
| ----------- | ----------- |---------|-------|
| cloud| cloud.ss.fish|Ubuntu| My personal cloud server|
| ss| ss.fish|OpenBSD|My personal OpenBSD server|
| ec2| | Ubuntu|This server will be created on an AWS EC2 instance|

### Servers Updates
To update all servers, I'll employ both **Ansible** and **Python** scripts. The **Python** script is crucial for converting the CSV file into an INI format for the **Ansible** inventory. Since servers are listed in a CSV file for other automation purposes, it's necessary.

**Ansible Playbooks:**
1. Update and check if reboot is needed on cloud server: [ansible-playbook/update_upgrade_cloud.yml](ansible-playbook/update_upgrade_cloud.yml)
2. Update all the package on ss server: [ansible-playbook/update_upgrade_ss.yml](ansible-playbook/update_upgrade_ss.yml)
3. Update and check if reboot is needed on ec2 server: [ansible-playbook/update_upgrade_ec2.yml](ansible-playbook/update_upgrade_ec2.yml)

On all three servers, the playbook will run as the user named 'ansible,' which I created for security purposes. This user can execute specific commands without a password when using sudo and doas, as I have manually configured.

Please note that on both the cloud and ec2 server playbooks, I do not use the apt module. Instead, I manually run the command in the Ansible playbook due to [this GitHub issue #51663](https://github.com/ansible/ansible/issues/51663). Additionally, in both server playbooks, it will check if a reboot is needed after every update.

The inventory is located here: [ansible-playbook/hosts.csv](ansible-playbook/hosts.csv.example) and will be converted by the script [csv_to_ini.py](csv_to_ini.py) to [ansible-playbook/hosts](ansible-playbook/hosts). This script will run automatically when using the `run.sh` command and can also be executed manually. Further details on the `run.sh` command will be explained on further section.


### Automated AWS EC2 Setup:
To create an EC2 instance in **AWS**, I utilized **Terraform** and **aws-cli**. **aws-cli** is only needed for authentication and connection to my **AWS** account. To make this work, I created three files: `provider.tf`, `main.tf`, and `output.tf`. Let me explain what each of these files does:

1. **[terraform/provider.tf](terraform/provider.tf)**
    - Specifies `hashicorp/aws` as the provider so Terraform will work with AWS.
    - Sets the region to Sydney (`ap-southeast-2`).
    - Sets up the VPC, Internet Gateway, and creates the Security Group to allow SSH connection.
      - All of this is needed for it to connect to the internet and for SSH to work.

2. **[terraform/main.tf](terraform/main.tf)**
    - Sets the EC2 AMI to `ami-09c8d5d747253fb7a` (Ubuntu 22.04 LTS, x86), sets the instance type to `t2.micro`, and names it "DevOps-Training".
    - Sets the security group 'SSHAcess', which is created in the `provider.tf` file.
    - Creates the user 'ansible', adds my public key, edits the sudoers file, and installs the Python `psutil` module.
      - My public key is visible in the file, but since it's a public key, it's safe to share publicly.
      - I configured it so that `apt` and `apt-get` commands can run passwordless with sudo so Ansible will work.
      - Installs Python `psutil` so that the stats monitoring script will work.

3. **[terraform/output.tf](terraform/output.tf)**
    - Provides the instance IP as output after it successfully creates the instance. I do not plan to use a fixed IP to save costs, so this is necessary for other automation scripts.


### Remote Server Monitoring:
To remotely monitor system statistics on all servers, I'll utilize the psutil **Python** library for reading system statistics and paramiko for establishing SSH connections remotely.

Originally, I planned to create the system reader from scratch using available Unix tools and parsing, but this approach would complicate things, especially since I intend to use this script on three different platforms (Linux, OpenBSD, and Darwin [MacOS]). Instead, it's simpler to use the psutil module since it already works across all these platforms.

I prefer to start most of my scripts with a shebang to env, like below:
```
#!/usr/bin/env python3
```
This way, I can run the script without specifying python3 or python in front of it. Using env also ensures that the OS will pick the correct Python version/program, and since Python isn't always located in the same path on every platform, this approach is more robust.

1. **[sys_reading.py](sys_reading.py)**

This script was created with the assistance of the [psutil documentation](https://psutil.readthedocs.io/en/latest/).  It displays various system metrics, including Hostname, Platform, Uptime, CPU usage, Memory usage, Network Card IPs, Public IP, and Root disk usage.

**Using Psutil**
- **Cpu Reading:** Utilizes `psutil.cpu_percent()` to obtain CPU usage in percentage with half-second readings for quick updates.
- **Memory usage:** Retrieves memory usage information using `psutil.virtual_memory()`.
- **Root disk usage:** Obtains disk usage for the root partition using `psutil.disk_usage()`.

**Using Unix tools**
- **Uptime:** Parses system uptime using the typical Unix uptime command, processed with awk and sed. Although I couldn't find a straightforward way to use `psutil.boot_time()`, I may revisit this approach in the future.
- **Network Card IPs:** Extracts IP addresses from network interfaces using the typical Unix ifconfig command and parses the output with awk.
- **Public IP:** Retrieves the public IP address by querying the ifconfig.me website using curl.
- **Hostname:** just to keep this consistant I'll be using the standard Unix `hostname` command.

**Using Platform Library**
- **Platform:** Utilizes the standard Python platform library to obtain platform information. This could prove essential for future updates to the script, especially if different commands are required for specific platforms.

This script is currently incomplete and somewhat messy. In the future, I plan to improve it by adding the following readings and features:

- Disk usage statistics for all storage partitions.
- Last system update information.
- Detection of security vulnerabilities in the kernel and installed packages.
- Implementation of email alerts for high resource usage.

However, if I end up adding too many features, it might be more efficient to use other specialized tools that can handle these tasks more effectively than a custom script. Nevertheless, this script serves as a valuable practice exercise for me to improve my skills and expanding my knowledge in the realm of DevOps.

2. **[sys_reading_remote.py](sys_reading_remote.py)**
The script [sys_reading.py](sys_reading.py), dont have the ability to ssh into server and parse csv files and, I do not plan to add it in since the script is quite messy adding it make it look quite messy, in the future I might combine both of this script.

This script will parse [ansible-playbook/hosts.csv](ansible-playbook/hosts.csv.example) and ssh into each of the host mention in it and run `sys_reading.py` script locally.


### Simple Execution:
- shell script



## Usage
### Updates With Ansible

> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.

### Creating and Destroying EC2 Instance with Terraform
- First item
- Second item
- Third item
- Fourth item


> Dorothy followed her through many of the beautiful rooms in her castle.
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
- python (os, platfrom, psutil, and paramiko)
Using Python for system stats mainly using psutil library

 I need to highlight these ==very important words==.


### Running sys_reading.py remotely with sys_reading_remote.py
My favorite search engine is [Duck Duck Go](https://duckduckgo.com).

### Connect it all together
The background color is `#ffffff` for light mode and `#000000` for dark mode.


[Contribution guidelines for this project](ansible-playbook/update_upgrade_cloud.yml)


![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)


![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)
