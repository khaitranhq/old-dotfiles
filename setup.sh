#!/bin/bash

SCRIPT_DIR=`readlink -f $0`
SCRIPT_DIR_PARENT=`dirname $SCRIPT_DIR`

cp -R $SCRIPT_DIR_PARENT/.config/* ~/.config

cp $SCRIPT_DIR_PARENT/private/.zsh.common ~/.zsh.common

cp $SCRIPT_DIR_PARENT/.tmux.conf ~

source ~/.zshrc
echo 'Copying successfully'
