#!/bin/bash

#cp .zshrc ~/.zshrc
#source ~/.zshrc

cp -R ~/Workspaces/dotfiles/.config/* ~/.config

cp ~/Workspaces/dotfiles/private/.zsh.common ~/.zsh.common

source ~/.zshrc
echo 'Copying successfully'
