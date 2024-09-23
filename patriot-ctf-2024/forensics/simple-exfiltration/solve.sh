tshark -r exfiltration_activity_pctf_challenge.pcapng -Y "icmp.type == 8" -Tfields -e ip.ttl | awk '{printf "%c", $1} END{printf "\n"}'
