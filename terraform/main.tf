resource "aws_instance" "DevOps-Training" {
  ami           = "ami-09c8d5d747253fb7a"
  instance_type = "t2.micro"
  key_name      = "m3air"
  security_groups = ["SSHAccess"]

  tags = {
    Name = "DevOps-Training"
  }

  user_data = <<-EOF
    #!/bin/bash
    sudo useradd -m -s /bin/bash ansible
    sudo mkdir -p /home/ansible/.ssh
    sudo sh -c "echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAID5U8m1UhT68H0jUjVyHztHli2kdNkdIkRqvLJx2S6+W ss@m3air.local' >> /home/ansible/.ssh/authorized_keys"
    sudo chmod 600 /home/ansible/.ssh/authorized_keys
    sudo chown -R ansible:ansible /home/ansible/.ssh
    echo 'ansible ALL=(ALL) NOPASSWD: /usr/bin/apt, /usr/bin/apt-get' | sudo tee /etc/sudoers.d/ansible
    sudo apt-get -y install python3-psutil
  EOF
}
