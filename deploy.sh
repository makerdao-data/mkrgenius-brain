#! /bin/bash
set -e

MKRGENIUS_HOME=${1:-$HOME/mkrgenius-brain}
cd $MKRGENIUS_HOME
docker pull ghcr.io/tadeongmi/mkrgenius-brain
docker-compose down
docker-compose up -d
