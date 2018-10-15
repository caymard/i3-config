#!/bin/bash
lscpu -J |jq -r '.lscpu[14].data' 2>&1