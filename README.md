# Configuration for my Linux
## Introduction
This repository is configuration of linux combo which I'm using.
It includes `Linux Mint `, `bspwm`, `polybar`, `rofi`, `neovim`, ...etc
## Installation
### Linux Mint Xfce
* Prepair a parition about > 50GB (I think it's enough for my work)
* Follow instruction on Youtube, it's quite easy
### Remove unused apps
```
sudo apt remove firefox drawing pix gnote warpinator simple-scan hexchat transmission-common hypnotix
sudo apt autoremove
```
### Config Linux using OS time
This command will fix time error when you install dual Window and Linux
```
timedatectl set-local-rtc 1
```
### kitty
```
sudo apt install kitty
```
### libinput-gestures
* Install
```
sudo gpasswd -a $USER input
```
Reboot computer
```
sudo install git
sudo apt-get install wmctrl xdotool
sudo apt-get install libinput-tools
sudo apt install gcc g++ make


git clone https://github.com/bulletmark/libinput-gestures.git
cd libinput-gestures
sudo make install (or sudo ./libinput-gestures-setup install)
```
* Configuration
```
# Make sure your terminal's directory is root of this repo
sudo cp libinput-gestures.conf /etc/
libinput-gestures-setup restart
```
### zsh
```
sudo apt update
sudo apt install zsh
sudo usermod -s /usr/bin/zsh $(whoami)
```
Reboot computer
```
## Install oh-my-zsh
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

## Install zsh-theme-powerlevel9k
sudo apt-get install zsh-theme-powerlevel9k

## Install zsh-syntax-highlighting
sudo apt-get install zsh-syntax-highlighting

## Instal zsh-autosuggestion
git clone git://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions

## Turn on extension above
### Not required, these lines were already in .zshrc of this repo
echo "source /usr/share/powerlevel9k/powerlevel9k.zsh-theme" >> ~/.zshrc
echo "source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc
echo "source ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc
```

### bspwm + polybar + rofi
* In order to clone repository easily, let create a ssh key
```
ssh-keygen -t rsa -b 4096 -C "leoalan5577@gmail.com"
cd ~/.ssh
```
Copy the content of file which has extension `.pub` and paste to SSH keygen of Github
* Install and configuration
```
sudo apt update
sudo apt install bspwm kakoune dmenu rofi scrot feh dunst 

# install polybar
sudo apt install build-essential git cmake cmake-data pkg-config python3-sphinx python3-packaging libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev
sudo apt install libnl-genl-3-dev libasound2-dev
git clone --recursive https://github.com/polybar/polybar
cd polybar
mkdir build
cd build
cmake .. -DENABLE_ALSA=ON
make -j$(nproc)
sudo make install

# Create and clone repos for working
mkdir ~/Workspace && cd ~/Workspace
git clone git@github.com:lioaslan/global.git
cd global && ./init.sh

# Copy bspwm, sxhkd, kitty, onedrive, zshrc,... config
cd dotfiles
source ./setup.sh

# Setup dependencies for polybar
cd polybar
./setup.sh

```
* After that, logout and login again to bspwm WM
### Node
```
sudo apt update
sudo apt install curl dirmngr apt-transport-https lsb-release ca-certificates
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt install nodejs
```
### fd + ripgrep
These packages are nescessary for neovim
```
wget https://github.com/sharkdp/fd/releases/download/v7.3.0/fd-musl_7.3.0_amd64.deb
sudo apt install ./fd-musl_7.3.0_amd64.deb && rm -rf ./fd-musl_7.3.0_amd64.deb

sudo apt install ripgrep
```
### Neovim
```
sudo add-apt-repository ppa:neovim-ppa/stable 
sudo apt-get update
sudo apt-get install neovim python3-pip
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

# install dependencies
sudo npm i -g eslint prettier
pip3 install yapf pylint
sudo apt install clang-format

cd ~/.config/nvim && nvim init.vim
```
Press `:so%` and run command `:PlugInstall`

### Docker
```
sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### Onedrive
```
sudo apt install build-essential libcurl4-openssl-dev libsqlite3-dev pkg-config
curl -fsS https://dlang.org/install.sh | bash -s dmd
source ~/dlang/dmd-xxxxxxxxx/activate # Change version following instruction in previous command


git clone https://github.com/abraunegg/onedrive.git
cd onedrive
./configure
make clean; make
sudo make install
```

### ibus-bamboo
```
sudo add-apt-repository ppa:bamboo-engine/ibus-bamboo
sudo apt-get update
sudo apt-get install ibus-bamboo
ibus restart
# Đặt ibus-bamboo làm bộ gõ mặc định
env DCONF_PROFILE=ibus dconf write /desktop/ibus/general/preload-engines "['xkb:us::eng', 'Bamboo']" && gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('ibus', 'Bamboo')]"
```
### Skype
```
wget https://repo.skype.com/latest/skypeforlinux-64.deb
sudo apt install ./skypeforlinux-64.deb
rm -f ./skypeforlinux-64.deb
```
### Dbeaver
```
wget https://download.dbeaver.com/community/21.1.0/dbeaver-ce_21.1.0_amd64.deb
sudo apt install ./dbeaver-ce_21.1.0_amd64.deb
rm -f ./dbeaver-ce_21.1.0_amd64.deb
```
## Notion
This installation is optional, I have switched to using web app instead.
```
wget https://github.com/davidbailey00/notion-linux/releases/download/v2.0.6-windows/notion-desktop_2.0.6_amd64.deb
sudo apt install ./notion-desktop_2.0.6_amd64.deb
rm -f ./notion-desktop_2.0.6_amd64.deb
```
## Setting mouse, touchpad
Follow [this](https://wiki.archlinux.org/title/Libinput#Via_Xorg_configuration_file). There are some configurates about it in `bspwmrc` file
## Setting boot logo
```
sudo cp ./images/boot-logo.png /usr/share/plymouth/themes/mint-logo/logo.png
sudo cp ./images/spinner-custom.png /usr/share/plymouth/themes/mint-logo/spinner.png
sudo update-iniramfs -u
```
And then reboot the computer
