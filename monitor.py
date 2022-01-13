from hcloud import Client
import os
from datetime import datetime, timezone
import argparse


parser = argparse.ArgumentParser(description='Monitor Hetzner instances')
parser.add_argument('token',
                type=str,
                help='Hetzner token')
parser.add_argument('prefix',
                type=str,
                help='Check instances starting with this prefix')
parser.add_argument('days',
                type=int,
                help='Max days before triggering')
args = parser.parse_args()

client = Client(token=args.token)
for server in client.servers.get_all():
    days = (datetime.now(timezone.utc) - server.data_model.created).days
    name = server.data_model.name

    if name.startswith(args.prefix) and days > args.days:
        print("%s (up for %s days)" % (name, days))


