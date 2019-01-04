#!/bin/bash

path2i3wpp=$(dirname $0)

$path2i3wpp/i3-wpp.sh $1
feh --bg-fill $1/.img1
python $path2i3wpp/i3-wpp.py $1

