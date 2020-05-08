#!/usr/bin/env bash

echo -e "To connect to VNC use the localhost IP and port 5901\nThe VNC password: 'default: 111111'"

# TODO: make vnc runuble at startup
docker run --name ubuntu-x-vnc -it --rm -p 5901:5901 ubuntu-x-vnc:16.04
