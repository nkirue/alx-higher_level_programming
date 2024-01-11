#!/bin/bash
# This script takes a URL as an argument, sends a request to that 
# URL using curl, and displays the size of the response body in bytes.

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Use curl with silent mode to send a request and display 
# the size of the response body in bytes
size=$(curl -sI $url | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

if [ -z "$size" ]; then
    echo "Failed to retrieve content size."
    exit 1
fi

echo "$size"

