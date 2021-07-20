#!/bin/bash

cp .zshrc ~/.zshrc
source ~/.zshrc

cp -R .config/* ~/.config

cp images/* ~/Pictures

echo 'Copying successfully'
