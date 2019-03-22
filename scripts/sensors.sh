#!/bin/bash
sensors -Au coretemp-isa-0000| awk '/^'"${1}"'/' RS='\n\n' | awk -F '[:. ]' '/'"${2}"':/{print$5}'|head -n2|tail -n 1
