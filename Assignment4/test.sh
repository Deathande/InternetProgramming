#!/bin/bash

python server.py &
pid=$!
sleep 1
python client.py
kill $pid
