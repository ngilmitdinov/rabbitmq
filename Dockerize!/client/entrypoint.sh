#!/bin/bash

if [ $# -eq 0 ]; then
    python rpc_client.py
else
    python rpc_client.py "$@"
fi
