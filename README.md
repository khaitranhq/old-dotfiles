# dotfiles
## Install zsh, oh-my-zsh and plugins
## Bookmarks
* `cp ./bookmarks ~/.config/bookmarks`
Add this line to `.zshrc`
```
source <path-to-user-directory>/.config/bookmarks/bookmarks.sh
```
## Troubleshooting
### zsh-syntax-highlighting slow
```
cat ./etc.wsl.conf /etc/wsl.conf
```
