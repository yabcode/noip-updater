#!/bin/bash

docker run --rm --name noip-updater \
  --log-driver=fluentd \
  --log-opt fluentd-address=localhost:54224 \
  --log-opt tag=docker.{{.Name}} \
  -t noip-updater
