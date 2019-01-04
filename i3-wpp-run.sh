#!/bin/bash

path2wallpappers=$1

echo $path2wallpappers

./i3-wpp.sh $1
feh --bg-fill $1/.img1
python ./i3-wpp.py $1

