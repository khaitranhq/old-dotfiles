#!/bin/bash

# Dirs
DIR=`pwd`
FDIR="/usr/share/fonts/TTF"

if [[ ! -d "$FDIR" ]]; then
  mkdir -p "$FDIR"
fi

install_font() {
	echo -e "\n[*] Installing fonts..."
	if [[ -d "$FDIR" ]]; then
		cp -rf $DIR/fonts/* "$FDIR"
	else
		mkdir -p "$FDIR"
		cp -rf $DIR/fonts/* "$FDIR"
	fi
}

main() {
  install_font
}

main
