#!/bin/bash
#Display all acceptable HTTP methods
curl -sI "$1" | grep Allow | cut -d ' '
