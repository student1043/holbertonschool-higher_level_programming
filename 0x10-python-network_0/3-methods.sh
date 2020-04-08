#!/bin/bash
# Task 1
curl -sI $1 | grep 'Allow: '| awk -F: '{print$2=$2}' | sed 's/^ *//g'
