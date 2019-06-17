#!/bin/bash
xrandr \
  --output HDMI2 --mode 1920x1080 --pos 0x0    --rotate normal --brightness 0.9 \
  --output DP1   --mode 1920x1080 --pos 1920x0 --rotate normal --brightness 0.9 --primary \
  --output eDP1  --mode 1920x1080 --pos 3840x0 --rotate normal