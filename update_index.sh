#! /bin/bash
set -e

MKRGENIUS_HOME=${1:-$HOME/mkrgenius-brain}
echo "updating index..."
cd $MKRGENIUS_HOME
# stopping and removing the container as we're creating a new one
docker stop -f mkrgenius-builder || true
docker rm -f mkrgenius-builder || true
echo "pulling newest files and building mkrgenius image..."
git checkout develop && git pull --rebase
docker build . -t brain:builder
echo "starting the container and creating fresh index..."
docker run --env-file=.env --name mkrgenius-builder --entrypoint "/app/build_index.sh" brain:builder
docker cp mkrgenius-builder:/app/index_new.json .
# stopping and removing the container as it won't be no longer needed
docker stop -f mkrgenius-builder || true
docker rm -f mkrgenius-builder || true
echo "restarting the app..."
docker-compose down
mv index_new.json index.json
docker-compose up -d
echo "deleting image used for index update..."
docker rmi brain:builder -f
docker system prune -f