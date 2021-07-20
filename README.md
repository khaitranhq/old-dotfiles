# Installation Arch
![image](https://user-images.githubusercontent.com/24852182/126031870-c0a20346-2821-4c13-82f9-38176c58b3cf.png)

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
### Copy OS files to `/mnt`
```
pacstrap /mnt base linux-lts linux-firmware util-linux grub efibootmgr os-prober intel-ucode connman vim
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
## Essential packages
### Fonts
```
yay -S ttf-vista-fonts ttf-ms-fonts
sudo pacman -S ttf-dejavu ttf-fira-code ttf-opensans ttf-fira-code ttf-roboto
```
### bspwm
```
sudo pacman -S xorg xorg-xinit bspwm sxhkd git base-devel kitty picom
git clone https://github.com/lioaslan/dotfiles.git
```
Copy `.config/bspwm` and `.config/sxhkd` to `~/.config`
Put `exec bspwm` to `~/.xinitrc`
### Background
```
sudo pacman -S feh
```
* Put command `feh --bg-fill /home/leo/dotfiles/images/bg.jpg` before `exec bspwm` in `~/.xinitrc` and `startx` to `.zprofile`
* Restart or run `startx` to test and restart later
### Install AUR and google chrome
```
git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -si

yay -S google-chrome
```
### Audio
```
sudo pacman -S pulseaudio pulseaudio-alsa pulseaudio-bluetooth pavucontrol
```
### Ibus-unikey
```
sudo pacman -S ibus ibus-unikey
```
Add these lines into `~/.xinitrc`
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
```
* Add `libinput-gestures-setup start` into `~/.xinitrc`
### Install zsh
```
sudo pacman -S zsh zsh-completions wget
chsh -s /usr/bin/zsh
zsh
# select 0
```
* Add `startx` to `~/.zprofile`
* Restart
```
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
sudo pacman -S zsh-theme-powerlevel10k zsh-syntax-highlighting zsh-autosuggestions
```
* Turn off comment above to turn on extensions
```
echo "source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme" >> ~/.zshrc
echo "source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc
echo "source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc
```
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
pip3 install yapf pylint

# Clone config before doing this step
cd ~/.config/nvim && nvim init.vim
```
* Open file `02.global.vim`, uncomment 4 lines at the end of file to map clipboard with neovim
* Press `:so%` and run command `:PlugInstall`
### fd + ripgrep
```
sudo pacman -S fd ripgrep
```
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
