#!/bin/bash
#Sends POST request
curl -s -X "email=hr@holbertonschool.com" "subject=I will always be here for PLD" -d "$1"
