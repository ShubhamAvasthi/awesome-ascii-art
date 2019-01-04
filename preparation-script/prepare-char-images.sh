#!/bin/bash

#Space
printf "\ ";
convert -background white -fill black -font ubuntu-mono label:"\ " ../character-images/32.bmp;

#Other characters
for ((i=33;i<92;i++))
do
	printf "\\$(printf %03o "$i")";
	convert -background white -fill black -font courier label:"$(printf "\\$(printf %03o "$i")")" ../character-images/$i.bmp;
done;

#Backslash
printf "\\";
convert -background white -fill black -font ubuntu-mono label:$(printf "\\";printf "\\") ../character-images/92.bmp;

#Other characters
for ((i=93;i<127;i++))
do
	printf "\\$(printf %03o "$i")";
	convert -background white -fill black -font courier label:"$(printf "\\$(printf %03o "$i")")" ../character-images/$i.bmp;
done;
printf "\n";