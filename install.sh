#!/bin/bash
set -e

mkdir -p ~/.venvs/i3
virtualenv -p python3 ~/.venvs/i3
# shellcheck disable=SC1090
source ~/.venvs/i3/bin/activate
pip install -Ur requirements.txt
deactivate

sudo cp services/wakelock.service /etc/systemd/system
sudo systemctl daemon-reload