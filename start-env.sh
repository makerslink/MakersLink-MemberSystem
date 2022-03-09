#!/bin/bash
if [ ! -d "./virtenv" ]; then
    python3 -m venv ./virtenv
fi
echo "Entering virtualenv - hopefully you typed 'source ./start-env.sh'"
source ./virtenv/bin/activate