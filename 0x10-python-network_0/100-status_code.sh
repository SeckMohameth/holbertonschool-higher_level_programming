#!/bin/bash
#display only status code
curl -sL -w "%{http_code}" "$1" -o /dev/null
