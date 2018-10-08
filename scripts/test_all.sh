#!/bin/bash

time (
	~/.config/i3/scripts/spotify.sh > /dev/null 2>&1
	~/.venvs/i3/bin/python ~/.config/i3/scripts/backlight.py > /dev/null 2>&1
	~/.venvs/i3/bin/python ~/.config/i3/scripts/assigned_mr.py > /dev/null 2>&1
	LC_TIME=fr_FR.UTF-8 date '+%d %b %Y %H:%M:%S' > /dev/null 2>&1
	~/.config/i3/scripts/volume.sh > /dev/null 2>&1
)