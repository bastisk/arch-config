# Configuration files for Arch Linux
A copy of my configuration files for running Arch Linux with i3 window manager on a laptop.
This repository contains

* i3 configuration files (global and for user "basti")
* script for adapting display brightness
* script for setting a wallpaper as well as configure screen resolutions by xrandr
* wvdial settings for usage of a wireless LTE stick on Arch


## Installation

Before starting the specific installations, copy all needed files to correct folders.

### Installation of i3
Copy the following files from this repository to your system.

* /home/basti/.config/*
* /home/basti/.fehbg.sh
* /home/basti/.xinitr
* (optional) /home/basti/scripts/display.sh
* (optional) /home/basti/scripts/helligkeit.sh
* (optional) /usr/local/bin/*
* (optional) /etc/*

Run this command to install all needed tools and their dependencies.
<pre>sudo pacman -S xorg-server i3 i3-wm i3blocks i3lock i3status feh</pre>
For lock with blurred background(script in ´usr/local/bin/lock´), install these, too:
<pre>sudo pacman -S imagemagick i3lock-color-git scrot</pre>

Type ´startx´ and you're done

### Installation of LTE Stick
<pre>sudo pacman -S wvdial usb-modeswitch</pre>
Then connect via
<pre>wvdial pin
wvdial umts</pre>
Get more help here: https://wiki.archlinux.org/index.php/USB_3G_Modem

