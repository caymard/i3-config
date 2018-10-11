#!/bin/bash

NUM_SCREENS=$(xrandr |grep -c ' connected')
SCRIPTS_BASE="$HOME/.config/i3/scripts"

if [ "$NUM_SCREENS" = "3" ]; then
	"$SCRIPTS_BASE/desk_masterrace.sh"
elif [ "$NUM_SCREENS" = "2" ]; then
	"$SCRIPTS_BASE/desk_upbottom.sh"
elif [ "$NUM_SCREENS" = "1" ]; then
	"$SCRIPTS_BASE/desk_laptop.sh"
else
	"$SCRIPTS_BASE/desk_laptop.sh"
fi