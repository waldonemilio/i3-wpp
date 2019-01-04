# i3-wpp

i3-wpp is intended to be a wallpapper manager for the i3wm (also compatible with i3-gaps). On its current form it takes a given folder containing wallpappers and assigns randomly one wallpapper per workspace per i3 session. The wallpappers will remain fixed on each workspace even if you change the focused workspace with a mouse click. 

It makes use of [i3 IPC interface](https://i3wm.org/docs/ipc.html) and the python library [i3ipc-python](https://github.com/acrisci/i3ipc-python) to listen to i3 events.

## Dependencies
* feh
* python
* i3ipc-python

## Usage
```
git clone https://github.com/waldonemilio/i3-wpp.git
```

Add to your i3 config
```
exec_always --no-startup-id PATH/TO/i3-wpp.sh /PATH/TO/WALLPAPPERS
exec_always --no-startup-id feh --bg-fill /PATH/TO/WALLPAPPERS/.img1
exec_always --no-startup-id python PATH/TO/i3-wpp.py /PATH/TO/WALLPAPPERS
```

For best results remove any wallpapper config from your i3 configuration

## Limitations
* Do not support multimonitor setups. Works on single monitor only
* Workspaces names should be named from 1 to 10
