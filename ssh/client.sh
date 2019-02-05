#!/usr/bin/env bash


#======================
# Custom Variable
#======================

PORT=8888
SSH_PORT=4084
REMOTE_PORT=8889
SSH_KEY_FILE="id_rsa"

#=============================

# generate ssh key file
ssh-keygen -t rsa -b 4096 -f ~/.ssh/${SSH_KEY_FILE} -C "localhost" -q

# autossh
autossh -M 0 -fCNL *:${REMOTE_PORT}:localhost:${PORT} -f ~/.ssh/${SSH_KEY_FILE} -p ${SSH_PORT} localhost
