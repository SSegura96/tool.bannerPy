#!/bin/bash

SCRIPPATH="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $SCRIPPATH; source .ve/bin/activate; python3 src/app.py $1