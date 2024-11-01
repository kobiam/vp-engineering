# Linux Desktop

## tracker-miner

Gnome tool that indexes your home folder so that searches in your file manager are faster.

Disable tracker-miner
```bash
sudo systemctl --global mask tracker-miner-fs-3.service
sudo systemctl --global mask tracker-xdg-portal-3.service
```
