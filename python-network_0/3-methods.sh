#!/bin/bash
# displays all HTTP methods the server will accept for a URL
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
