#!/bin/bash
# This script takes a URL as an argument, sends a GET request, and displays the body of a 200 status code response.

curl -sL -w "%{http_code}" $1 -o /dev/null

