#! /bin/bash
set -e

MKRGENIUS_HOME=${1:-$HOME/mkrgenius-brain}
echo "updating training-data index..."
cd $MKRGENIUS_HOME
docker rm -f mkrgenius-builder || true
docker run --env-file=.env --name mkrgenius-builder --entrypoint "/app/build_index.sh" ghcr.io/tadeongmi/mkrgenius-brain
docker cp mkrgenius-builder:/app/index_new.json .
docker rm -f mkrgenius-builder || true
docker-compose down
mv index_new.json index.json
docker-compose up -d