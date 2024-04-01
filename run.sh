#!/usr/bin/env sh

ec2create(){
    echo '------------------------------------'
    echo 'Creating EC2 Instance with terraform'
    echo '------------------------------------'
    echo 'Run terraform apply...'
    terraform -chdir="./terraform" apply -auto-approve || { echo 'EC2 Instance creation failed. Exiting...' ; exit 1; }

    echo 'Adding instance ip to hosts.csv...'
    instance_ips=$(terraform -chdir="./terraform" output -raw instance_ips)
    echo "ec2,$instance_ips,ansible" >> ./ansible-playbook/hosts.csv

}

sys_update(){
    echo '-------------------------------------------------------'
    echo 'Updating all of my servers including the new EC2 server'
    echo '-------------------------------------------------------'

    echo 'Convert hosts.csv file to hosts (ini)...'
    ./csv_to_ini.py


    echo 'Update hosts...'
    hosts_file='./ansible-playbook/hosts'
    hosts_list=$(cat ./ansible-playbook/hosts.csv| awk -F ',' '{ print $1 }'|tail -n +2)

    for host in $hosts_list
    do
      echo "Updating $host ..."
      ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i $hosts_file ./ansible-playbook/update_upgrade_$host.yml
    done
}

sys_stats(){
    echo '-------------------------'
    echo 'Status of all the servers'
    echo '-------------------------'
    echo 'Running the sys_reading.py remotely...'
    ./sys_reading_remote.py || { echo 'sys_reading_remote.py failed. Exiting...' ; exit 1; }

}

ec2destroy(){
    echo '------------------------'
    echo 'Destroy the EC2 instance'
    echo '------------------------'
    echo 'Destroy EC2 instance...'
    # Might be a bad idea to use -auto-aprove on destroy command, but this is just an example
    terraform -chdir="./terraform" destroy -auto-approve || { echo 'EC2 destroyed failed. Exiting...' ; exit 1; }
    echo 'Remove EC2 from hosts.csv...'
    # sed -i doesnt work on mac, I use mac so have to redirect
    sed '/ec2/d' ./ansible-playbook/hosts.csv > /tmp/temp.csv && mv /tmp/temp.csv ansible-playbook/hosts.csv

}

case "$1" in
  'create'|'c')
        ec2create
  ;;
  'destroy'|'d')
        ec2destroy
   exit 1
  ;;
  'stats'|'s')
        sys_stats
  ;;
   'update'|'u')
        sys_update
  ;;
  *)
        ec2create
        sys_update
        sys_stats
        ec2destroy
    ;;
esac
