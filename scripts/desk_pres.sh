#!/bin/bash
xrandr \
  --output eDP1  --mode 1920x1080 --pos 0x0    --rotate normal --primary \
  --output HDMI2 --mode 1920x1080 --pos 0x0 --rotate normal \
  --output DP1 --off
