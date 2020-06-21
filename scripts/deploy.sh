#!/bin/bash
set -e

rsync -avz --delete -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress remotehat/hat $SSH_USER@$DEPLOY_HOST_PATH/remotehat/
