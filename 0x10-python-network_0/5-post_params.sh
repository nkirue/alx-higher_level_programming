#!/bin/bash
# Sends a POST request to the URL with custom parameters and displays the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
