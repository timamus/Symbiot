#!/bin/bash

# Setting up the error handler
trap 'read -p "Press enter to continue..."' ERR

cd "$(dirname "$0")"
source ./venv/bin/activate
python3 ./main.py