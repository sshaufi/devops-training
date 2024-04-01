#!/usr/bin/env python3

import csv

with open('./ansible-playbook/hosts.csv', 'r') as csvfile, open('./ansible-playbook/hosts','w') as ini:
       reader = csv.DictReader(csvfile)

       for row in reader:
            ini.write(f'[')
            ini.write(f'{row["group"]}')
            ini.write(f']\n')
            ini.write(f'{row["hostname"]} ansible_user={row["ansible_user"]}\n\n')

