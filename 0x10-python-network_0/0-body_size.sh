#!/bin/bash
# Task 0
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
