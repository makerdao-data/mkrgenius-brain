#! /bin/bash
set -e

MKRGENIUS_HOME=${1:-$HOME/mkrgenius-brain}
echo "updating index..."
cd $MKRGENIUS_HOME
# stopping and removing the container as we're creating a new one
sudo docker stop mkrgenius-builder || true
sudo docker rm -f mkrgenius-builder || true
sudo docker build . -t brain:builder
echo "starting the container and creating fresh index..."
sudo docker run --env-file=.env --name mkrgenius-builder --entrypoint "/app/build_index.sh" brain:builder
sudo docker cp mkrgenius-builder:/app/index_new.json .
# stopping and removing the container as it won't be no longer needed
sudo docker stop mkrgenius-builder || true
sudo docker rm -f mkrgenius-builder || true
echo "restarting the app..."
mv index_new.json index.json
sudo docker stop dev-mkrgenius-brain
sudo docker rm -f dev-mkrgenius-brain
sudo docker run -d -v $MKRGENIUS_HOME/index.json:/app/index.json --name dev-mkrgenius-brain --env-file .env -p 8000:8000 brain:dev
echo "deleting image used for index update..."
sudo docker rmi -f brain:builder
sudo docker system prune -f