#!/bin/bash
set -x
/usr/bin/python3 /var/www/flightdata.py
/usr/bin/python3 /var/www/webpage.py
echo "xd"