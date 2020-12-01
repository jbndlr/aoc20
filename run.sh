#!/bin/zsh

docker run --rm -ti --volume="$PWD:/code" -w /code jbndlr/python-devel:0.0.4
