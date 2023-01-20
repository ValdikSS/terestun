TereStun — STUN over Teredo
===========================

TereStun is a very simple unitility to determine external IPv4 address and source port over NAT, using Teredo protocol.

In other words, this is a STUN-like client over Teredo.

```
$ ./terestun.pyz --help
usage: Teredo STUN [-h] [-s SERVER] [-p PORT] [--ip-only] [--port-only]

Get IPv4 address and source port over Teredo network

options:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        Teredo server
  -p PORT, --port PORT  Source port to use
  --ip-only             Show only IPv4 address, without port
  --port-only           Show only source port, without IPv4 address

$ ./terestun.pyz
142.251.36.110:44254
```
