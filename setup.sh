#!/bin/bash

DOTFILES_DIR=/home/leo/Workspace/global/dotfiles

cp $DOTFILE_DIR/private/.zsh.common ~/
cp $DOTFILE_DIR/.zshrc ~/.zshrc
source ~/.zshrc

cp -R $DOTFILE_DIR/.config/* ~/.config
# cp .xprofile ~/

# cp images/* ~/Pictures

echo 'Copying successfully'
