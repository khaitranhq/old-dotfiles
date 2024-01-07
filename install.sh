#!/bin/bash

echo "Updating and Upgrading packages..."

apt update
apt upgrade -y

echo "Installing zsh..."

apt install zsh curl -y
chsh -s zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
