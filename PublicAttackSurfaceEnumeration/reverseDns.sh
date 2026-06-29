#!/bin/bash

# Check if file is provided as argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# File containing IP addresses data
file="$1"

# Loop through each ASN from the output and execute the whois command
for IP in $(cat "$file"); do
    echo "Running reverse DNS"
    echo $IP | mapcidr -silent | dnsx -ptr -resp-only -silent
done
