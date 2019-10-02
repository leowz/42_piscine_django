#!/bin/sh

if [ ! -z $1 ]; then
	curl -sI bit.ly/1fjf | grep Location | cut -d' ' -f2
fi;
