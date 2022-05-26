#!/bin/bash
cp -r ./app/py_scheduler venv/lib/python3.9/site-packages
cp -r ./app/tools venv/lib/python3.9/site-packages
cd venv/lib/python3.9/site-packages
zip -r9 ../../../../function.zip .
cd ../../../../
zip -g ./function.zip -r app
mv ./function.zip /mnt/c/Users/david/Documents/_WSL