#!/bin/bash
xrandr \
  --output HDMI2 --mode 1920x1080 --pos 0x0 --rotate normal --brightness 0.9 \
  --output eDP1 --mode 1920x1080 --pos 0x1080 --rotate normal --primary
