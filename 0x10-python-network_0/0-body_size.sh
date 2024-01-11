#!/bin/bash
# URL as an arg., sends a req., & displays d  size of d resp. body in bytes.

curl -sI $1 | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r'
