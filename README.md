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
1. Playbook for cloud server[ansible-playbook/update_upgrade_cloud.yml](ansible-playbook/update_upgrade_cloud.yml)
2. Playbook for ss server [ansible-playbook/update_upgrade_ss.yml](ansible-playbook/update_upgrade_ss.yml)
3. Playbook for ec2 server [ansible-playbook/update_upgrade_ec2.yml](ansible-playbook/update_upgrade_ec2.yml)

On all three of the servers, the playbook will run as ansible user that I created for security purpose. The user can run specifics command without password when they run the command with sudo and doas as I manually configured. 

Note that on both cloud and ec2 server playbook I dont use the apt module instead I run the command manually on ansible playbook its because of [ansible github issue #51663](https://github.com/ansible/ansible/issues/51663). 

The inventory is here server[ansible-playbook/hosts.csv](ansible-playbook/hosts.csv.example) and will be convert by the script [csv_to_ini.py](csv_to_ini.py) and be change to  [ansible-playbook/hosts](ansible-playbook/hosts). This script will be run if using the run.sh command, and also can be manually run. run.sh command will be explain in other sections.


### Automated AWS EC2 Setup:
- terraform
Using terraform for ec2

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

### Remote Server Monitoring:
- python (os, platfrom, psutil, and paramiko)
Using Python for system stats mainly using psutil library

 I need to highlight these ==very important words==.

### Simple Execution:
- shell script

> Dorothy followed her through many of the beautiful rooms in her castle.
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
## Usage
#### Updates With Ansible
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


### Running sys_reading.py remotely with sys_reading_remote.py
My favorite search engine is [Duck Duck Go](https://duckduckgo.com).

### Connecting all together
The background color is `#ffffff` for light mode and `#000000` for dark mode.


[Contribution guidelines for this project](ansible-playbook/update_upgrade_cloud.yml)


![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)


![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)
