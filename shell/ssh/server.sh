#!/usr/bin/env bash


#======================
# Custom Variable
#======================

SSH_PORT=22
SSH_KEY_FILE="id_rsa"
REMOTE_SSH_PORT=22
REMOTE_USER=root
REMOTE_IP=0.0.0.0
REMOTE_PORT=8888

#=============================

# generate ssh key file
ssh-keygen -t rsa -b 4096 -f ~/.ssh/${SSH_KEY_FILE} -q

# copy ssh key file to remote server
ssh-copy-id -p ${REMOTE_SSH_PORT} -i ~/.ssh/${SSH_KEY_FILE} ${REMOTE_USER}@${REMOTE_IP}

# autossh
autossh -M 0 -fCNR ${REMOTE_PORT}:localhost:${SSH_PORT} -p ${REMOTE_SSH_PORT} -i ~/.ssh/${SSH_KEY_FILE} ${REMOTE_USER}@${REMOTE_IP}
