#!/usr/bin/env python3

import sys
import socket
import argparse

DATA = b"\x00\x01\x00\x00\x2a\x3c\xfa\x40\x75\xe9\xbf\x57\x00\x60\x00\x00" \
       b"\x00\x00\x08\x3a\xff\xfe\x80\x00\x00\x00\x00\x00\x00\x00\x00\xff" \
       b"\xff\xff\xff\xff\xff\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
       b"\x00\x00\x00\x00\x02\x85\x00\x7d\x37\x00\x00\x00\x00"

parser = argparse.ArgumentParser(
        prog = 'Teredo STUN',
        description = 'Get IPv4 address and source port over Teredo network')
parser.add_argument('-s', '--server', default='win10.ipv6.microsoft.com',
                    help='Teredo server')
parser.add_argument('-p', '--port', type=int, default=0,
                    help='Source port to use')
parser.add_argument('--ip-only', action='store_true',
                    help='Show only IPv4 address, without port')
parser.add_argument('--port-only', action='store_true',
                    help='Show only source port, without IPv4 address')
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(10)
try:
    s.bind(('0.0.0.0', args.port))
    s.sendto(DATA, (args.server, 3544))
    response, source = s.recvfrom(512)
    s.close()
except socket.error as e:
    print(e, file=sys.stderr)
    sys.exit(1)
except (KeyboardInterrupt, SystemExit):
    sys.exit(2)
if not len(response) > 64:
    print("Not enough data", file=sys.stderr)
    sys.exit(3)

port_raw = response[15:17]
port = int.from_bytes(port_raw, 'big') ^ 0xFFFF

ip_raw = response[17:21]
ip = int.from_bytes(ip_raw, 'big') ^ 0xFFFFFFFF
ip1 = (ip >> 24) % 256
ip2 = (ip >> 16) % 256
ip3 = (ip >> 8) % 256
ip4 = ip % 256

if args.port_only:
    print(port)
elif args.ip_only:
    print("{}.{}.{}.{}".format(ip1, ip2, ip3, ip4))
else:
    print("{}.{}.{}.{}:{}".format(ip1, ip2, ip3, ip4, port))
