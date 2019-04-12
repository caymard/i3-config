#!/bin/bash
set -e

mkdir -p ~/.venvs/i3
virtualenv -p python3 ~/.venvs/i3
# shellcheck disable=SC1090
source ~/.venvs/i3/bin/activate
pip install -Ur requirements.txt
deactivate

sudo apt update -qq
sudo apt install --yes \
	xbacklight \
	i3 \
	i3blocks \
	rofi

echo "⚠ I installed i3, but if you want fancy gaps go install i3-gaps"

mkdir -p ~/.config/rofi
cp -r rofi/* ~/.config/rofi

sudo cp services/wakelock.service /etc/systemd/system
sudo systemctl daemon-reload