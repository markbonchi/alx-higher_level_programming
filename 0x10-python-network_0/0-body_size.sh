#!/usr/bin/bash
#count the size of the body
curl -s "$1" | wc -c
