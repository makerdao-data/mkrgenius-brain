#! /bin/bash
set -e

MKRGENIUS_HOME=${1:-$HOME/mkrgenius-brain}
cd $MKRGENIUS_HOME
git checkout develop && git pull --rebase
sudo docker build . -t brain:dev
docker-compose down
docker-compose up -d