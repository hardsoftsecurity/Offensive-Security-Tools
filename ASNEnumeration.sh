#!/bin/bash

# Check if file is provided as argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# File containing ASN data
file="$1"

# Loop through each ASN from the output and execute the whois command
for ASN in $(cat "$file" | grep "ASN" | cut -d ":" -f 1); do
    echo "Running whois for $ASN"
    whois -h whois.radb.net -- "-i origin $ASN" | grep -Eo "([0-9.]+){4}/[0-9]+" | uniq
done
