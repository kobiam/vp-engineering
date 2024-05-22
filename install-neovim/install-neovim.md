# Install neovim

debian

```sh
apt install neovim
```

## Install plugins

for vim

```sh
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

for neovim

```sh
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

Example to install **NERDTree**

type `nvim` and then type `:PlugInstall`

if you exit the nvim

type `nvim` and type `:NERDTree` or `:help NERDTree`
