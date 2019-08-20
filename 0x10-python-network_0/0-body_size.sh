#!/bin/bash
# send request to url
curl -sI "$1" | grep Content-Length | cut -d ':' -f 2
