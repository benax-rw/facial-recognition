#!/bin/bash

# Run Node.js app in the background and redirect output to app_output.txt
node app.js > app_output.txt 2>&1 &

# Run Node.js server in the background and redirect output to server_output.txt
node server.js > server_output.txt 2>&1 &

# Run Python client in the background and redirect output to client_output.txt
python client.py > client_output.txt 2>&1 &

