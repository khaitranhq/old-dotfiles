#!/bin/bash

cp -R ~/Workspace/dotfiles/.config/* ~/.config

cp ~/Workspace/dotfiles/private/.zsh.common ~/.zsh.common

source ~/.zshrc
echo 'Copying successfully'
