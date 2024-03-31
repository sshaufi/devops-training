terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_route_table" "terraform" {
  vpc_id = "vpc-025e30832fbec6fea"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "igw-053b79f1e698caf46"

  }
}


resource "aws_security_group" "terraform" {
  name        = "SSHAccess"
  description = "Allow SSH access"

  // Inbound rule to allow SSH access from anywhere
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  // Outbound rule to allow all traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

