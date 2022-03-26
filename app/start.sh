#!/bin/bash

# curl selenium:4444

if [ $# -ge 1 ]; then
    # echo ${@}
    cd /opt/app/src
    python ${@}
fi
