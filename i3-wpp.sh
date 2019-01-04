#!/bin/bash

path2wallpappers=$1
i=0

ls $path2wallpappers | sort -R | grep -v img | head | 
	while read file; 
	do 
		cp $path2wallpappers/$file $path2wallpappers/.img$i; 
		i=$[$i +1]; 
	done

