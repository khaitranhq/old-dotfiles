# Installation Arch
![image](https://user-images.githubusercontent.com/24852182/128619415-b989b820-ffe2-4d41-be5e-687018cca4ec.png)

## Download 
http://mirror.bizflycloud.vn/archlinux/iso/2021.07.01/
## Start installing
### Set time
```
timedatectl set-ntp true
```
### Create partitions
```
cfdisk /dev/nvme0n1
```
* Select `gpt`.
* Select free space
* Create a partition with 512MB of size for `EFI System`
* Create a partition with 12GB of size (double of RAM) for Linux swap
* With the remain, select new -> write -> type yes
* Select quit
Now use command `lsblk` to confirm that they were created.
### Format partitions
```
mkfs.fat -F32 /dev/nvme0n1p6
mkfs.ext4 /dev/nvme0n1p8
mkswap /dev/nvme0n1p7
swapon /dev/nvme0n1p7
```
### Mount partition's data
```
mount /dev/nvme0n1p8 /mnt
mkdir /mnt/boot
mount /dev/nvme0n1p6 /mnt/boot
```
### Connect wifi
**NOTE**: If you're able to connect to LAN, it's not necessary to do this setp
```
iwctl
station wlan0 scan
station wlan0 get-networks
station wlan0 connect SSID
```
If a passphrase is required, you will be prompted to enter it. If there is any problem, `rfkill unblock wifi`
### Copy OS files to `/mnt`
```
pacstrap /mnt base linux linux-firmware util-linux grub efibootmgr os-prober intel-ucode connman vim wpa_supplicant base-devel
```
### Generate `fstab` file
```
genfstab -U /mnt >> /mnt/etc/fstab
```
### Setting root
#### Set local time
```
arch-chroot /mnt
ln -sf /user/share/zoneinfo/Asio/Ho_Chi_Minh /etc/localtime
timedatectl set-local-rtc 1
hwclock --systohc
```
#### Set language
```
vim /etc/locale.gen
```
Uncomment the line `en_US.UTF-8 UTF-8`
```
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
```
#### Set hostname
```
echo leo > /etc/hostname
vim /etc/hosts
```
and put these line to the file
```
127.0.0.1 localhost
::1 localhost
127.0.0.1 leo.localdomain leo
```
#### Setting network
```
systemctl enable connman
```
#### Set your password
```
passwd
```
#### Grub install
```
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUD
mkdir /mnt/windows10
mount /dev/(window10efiblock /mnt/windows10
```
Edit /etc/default/grub, add or uncomment GRUB_DISABLE_OS_PROBER=false
```
grub-mkconfig -o /boot/grub/grub.cfg
```
Now `exit` and `reboot` to apply configurations.
#### Package manager
```
vim /etc/pacman.conf
```
Now, uncomment these lines
```
[multilib]
Include = /etc/pacman.d/mirrorlist
```
Run `pacman -Syy` to update
#### Install `openssh`
```
pacman -S openssh
systemctl start sshd
systemctl enable sshd
```
#### Create user 
```
useradd -m leo
passwd leo
# Set password for new user
```
User `ssh leo@localhost` to confirm it worked
```
usermod --append --groups wheel leo
pacman -S vi sudo
visudo /etc/sudoers
```
Then, uncomment line `%sudo ALL=(ALL) ALL` and `%wheel ALL=(ALL) ALL` to allow user can use sudo
Now restart computer and login with new user.
## XFCE 
```
sudo pacman -S xorg xorg-xinit fxce4 xfce4-goodies lightdm lightdm-gtk-greeter
sudo systemctl enable lightdm
```
In `/etc/lightdm/lightdm.conf`, add `greeter-session=lightdm-yourgreeter-greeter` in [Seat:*] section. Reboot
## Essential packages
### Install AUR and google chrome
```
git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -si

yay -S google-chrome
```
### Fonts
```
yay -S ttf-vista-fonts ttf-ms-fonts
sudo pacman -S ttf-dejavu ttf-fira-code ttf-opensans ttf-fira-code ttf-roboto
```
### Audio
```
sudo pacman -S pulseaudio pulseaudio-alsa pulseaudio-bluetooth pavucontrol bluez bluez-utils
sudo systemctl start bluetooth
sudo systemctl enable bluetooth
pulseaudio -D
```
### Ibus-bamboo
```
sudo pacman -S ibus wget
wget https://github.com/BambooEngine/ibus-bamboo/archive/refs/tags/v0.7.5.tar.gz
tar xvzf v0.7.5.tar.gz
cd ibus-bamboo-0.7.5
sudo make install
ibus restart
```
Create and add these lines to `/etc/profile.d/ibus_bamboo`
```
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT4_IM_MODULE=ibus
export CLUTTER_IM_MODULE=ibus
ibus-daemon -drx
```
### libinput-gestures
* `sudo gpasswd -a $USER input` and reboot
```
yay -S libinput-gestures
sudo pacman -S xdotool
libinput-gestures-setup autostart
```
### Install zsh
```
sudo pacman -S zsh zsh-completions wget
chsh -s /usr/bin/zsh
zsh
# select 0
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
sudo pacman -S zsh-theme-powerlevel10k zsh-syntax-highlighting zsh-autosuggestions
```
* Copy `.zshrc` from this repo to `$HOME`
### Nodejs
```
sudo pacman -S nodejs-lts-erbium # for version 12.22.0
```
### Neovim
```
sudo pacman -S neovim python-pip npm xclip
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

# install dependencies
sudo npm i -g eslint prettier
pip install yapf pylint

# Clone config before doing this step
cd ~/.config/nvim && nvim init.vim
```
* Open file `02.global.vim`, uncomment 4 lines at the end of file to map clipboard with neovim
* Press `:so%` and run command `:PlugInstall`
### fd + ripgrep
```
sudo pacman -S fd ripgrep
```
## Customize UI
### Initial setup
* Hide desktop icon: Click right to Desktop -> Desktop Settings -> Icons -> Icon Type: None
* Click right to Desktop -> Settings -> Window Manager Tweaks:
       * Cycling -> Uncheck Draw frame around selected...
       * Placement -> Select At the center of the screen
       * Compositor -> Uncheck Show shadows under regular windows
       * Close
```
sudo pacman -S unzip
mkdir ~/Downloads ~/Pictures
cd ~/Downloads
wget https://www.opencode.net/lsteam/xfce-big-sur-setup-file/-/raw/master/update-xfce-bigsur.zip
unzip update-xfce-bigsur.zip
cp -r update-xfce-bigsur/wallpapers ~/Pictures/
```
* Click right to Desktop -> Setting -> Desktop -> Change folder to `~/Pictures/wallpapers` -> Select a picture
* Open Thunar File Manager, Send `Downloads`, `Pictures` to side pane
### Theme - icons - cursors - fonts
## Optional package
### Docker
```
sudo pacman -S docker
sudo systemctl start docker
sudo systemctl enable docker

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
### Skype
```
yay -S skypeforlinux-stable-bin
```
### Telegram
```
wget https://updates.tdesktop.com/tlinux/tsetup.2.8.10.tar.xz
tar -xvf ./tsetup.2.8.10.tar.xz
sudo mv Telegram/Telegram /usr/local/bin/telegram
```
### Dbeaver
```
sudo pacman -S dbeaver
```
