set -e

# Builds the docker image
sudo docker build -t my-fast-app .

# Deploys the Docker Container
docker-compose up -d --builds