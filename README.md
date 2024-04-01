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
Since I try to keep it simple, I will keep the scripts and codes with minimal depedency and short as possible. Its also need to be readable enough without needing  a lot of comments. I will explain the solution 


This for reference
| Name| Hostname|os| Comments|
| ----------- | ----------- |---------|-------|
| cloud| cloud.ss.fish|Ubuntu| My personal cloud server|
| ss| ss.fish|OpenBSD|My personal OpenBSD server|
| ec2| aws-ip| Ubuntu|This serve will be created on AWS EC2 instance|
### Servers Updates

To update all of the servers **ansible** and **python** script will be use. Python script is needed to convert csv file to ini for inventory. For automation I list all of my server in csv format. 




Ansible Playbook
[Contribution guidelines for this project](ansible-playbook/update_upgrade_cloud.yml)

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
