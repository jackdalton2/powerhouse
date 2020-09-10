#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
SCRIPTNAME=`basename "$0"`

# if not root then run as root
if (( $EUID != 0 )); then
	sudo $SCRIPTPATH/$SCRIPTNAME
	exit
fi

echo "Available updates:"
apt list --upgradable

read -p "Update package repos and check again? " CHOICE
case "$CHOICE" in
	y|Y|yes|Yes ) apt update && apt list --upgradable;;
	* ) :;;
esac

read -p "Restart after updates? " CHOICE
case "$CHOICE" in
        y|Y|yes|Yes ) echo "Will do";;
        n|N|no|No ) echo "I won't.";;
        * ) echo "Undefined input, not restarting";;
esac

apt update
# use default option for config files, don't prompt -> use old config file if no default is available
apt upgrade -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"
apt clean -y
apt autoremove -y

case "$CHOICE" in
        y|Y|yes|Yes ) reboot now;;
esac
