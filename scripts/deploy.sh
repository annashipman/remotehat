#!/bin/bash
set -e

rsync -avz --delete -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress remotehat/hat $SSH_USER@$DEPLOY_HOST:$DEPLOY_PATH/remotehat/
ssh -o StrictHostKeyChecking=no $SSH_USER@$DEPLOY_HOST sudo systemctl restart apache2
