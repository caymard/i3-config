#!/bin/bash
while [ "$select" != "NO" ] && [ "$select" != "YES" ]; do
    select=$(echo -e 'NO\nYES' | dmenu -nb '#2f343f' -nf '#f3f4f5' -sb '#f34949' -sf '#f3f4f5' -fn '-*-*-medium-r-normal-*-*-*-*-*-*-100-*-*' -i -p "Are you sure you want to logout?")
    [ -z "$select" ] && exit 0
done
[ "$select" = "NO" ] && exit 0
i3-msg exit
