#!/usr/bin/env bash

## Author: Leo Aslan
## Mail: leoalan5577@gmail.com
## Github: @lioaslan

# Available Styles
# >> Created and tested on : rofi 1.6.0-1
#
# blurry	blurry_full		kde_simplemenu		kde_krunner		launchpad
# gnome_do	slingshot		appdrawer			appdrawer_alt	appfolder
# column	row				row_center			screen			row_dock		row_dropdown

theme="kde_simplemenu"
dir="$HOME/Workspace/global/dotfiles/polybar/styles/scripts/configs/"

# comment these lines to disable random style
# themes=($(ls -p --hide="launcher.sh" $dir))
# theme="${themes[$(( $RANDOM % 16 ))]}"

rofi -no-lazy-grab -show drun -modi drun -theme $dir/launcher
