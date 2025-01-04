#!/bin/bash
source .env
TAG=2501032215
DH_USER=sciabarracom
DH_BUILDER=openserverless-builder
GH_IMAGE=ghcr.io/mastrogpt/mastrogpt-starter
DH_IMAGE=$DH_USER/mastrogpt-starter
GH_TOKEN=${GITHUB_TOKEN:?please set GITHUB_TOKEN in .env}
DH_TOKEN=${DOCKERHUB_TOKEN:?please set DOCKERHUB_TOKEN in .env} 
docker login -u $DH_USER -p "$DH_TOKEN"
docker buildx create  --driver cloud $DH_USER/$DH_BUILDER

docker login ghcr.io -u mastrogpt -p $TOKEN
docker buildx create --use --name mybuilder
docker buildx inspect --bootstrap
docker run --privileged --rm tonistiigi/binfmt --install all

docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t $IMAGE:$VERSION . --push
