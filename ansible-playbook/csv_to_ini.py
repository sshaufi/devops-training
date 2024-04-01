#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('hosts.csv')

with open('hosts', 'w') as file:
       for _, row in df.iterrows():
            file.write(f'[')
            file.write(f'{row["group"]}')
            file.write(f']\n')
            file.write(f'{row["hostname"]} ansible_user={row["ansible_user"]}\n\n')

