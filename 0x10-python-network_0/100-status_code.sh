#!/bin/bash
# Task 1
curl -sL -w "%{http_code}" -I $1 -o /dev/null
