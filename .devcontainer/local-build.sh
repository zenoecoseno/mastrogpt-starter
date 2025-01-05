#!/bin/bash
cd "$(dirname $0)"
source .env
TAG=2501052000
DH_USER=sciabarracom
DH_BUILDER=openserverless-builder
DH_IMAGE=$DH_USER/mastrogpt-starter
DH_TOKEN=${DOCKERHUB_TOKEN:?please set DOCKERHUB_TOKEN in .env} 
docker login -u $DH_USER -p "$DH_TOKEN"
docker buildx create  --driver cloud $DH_USER/$DH_BUILDER
docker buildx build --no-cache \
  --builder cloud-$DH_USER-$DH_BUILDER \
  --platform linux/amd64,linux/arm64 \
  -t $DH_IMAGE:$TAG . --push
<<<<<<< HEAD

=======
#GH_IMAGE=ghcr.io/mastrogpt/mastrogpt-starter
#GH_TOKEN=${GITHUB_TOKEN:?please set GITHUB_TOKEN in .env}
#docker pull $DH_IMAGE:$TAG
#docker tag $DH_IMAGE:$TAG $GH_IMAGE:$TAG
#docker push $GH_IMAGE:$TAG
>>>>>>> 9561796 (updating build)

