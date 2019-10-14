#!/bin/sh

if [ ! -z $1 ]; then
	curl -sI {$1} | grep Location | cut -d' ' -f2
fi;
