#!/bin/bash

cp private/.zsh.common ~/
cp .zshrc ~/.zshrc
source ~/.zshrc

cp -R .config/* ~/.config
cp .xprofile ~/

cp images/* ~/Pictures

echo 'Copying successfully'
