#!/bin/bash
# URL as an arg., sends a req., & displays d  size of d resp. body in bytes.
curl -s "$1" | wc -c
