#!/bin/bash
VERSION=2501032215
IMAGE=ghcr.io/mastrogpt/mastrogpt-starter
TOKEN=${GITHUB_TOKEN:?please set GITHUB_TOKEN}
docker login ghcr.io -u mastrogpt -p $TOKEN
docker buildx create --use --name mybuilder
docker buildx inspect --bootstrap
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t $IMAGE:$VERSION . --push
