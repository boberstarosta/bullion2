#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

SHORTCUT=~/.config/autostart/Bullion.desktop

cat <<EOF >${SHORTCUT}
[Desktop Entry]
Type=Application
Exec=${SCRIPTPATH}/runserver.sh
Icon=${SCRIPTPATH}/icon.png
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Bullion
GenericName=bullion
X-GNOME-FullName=Bullion
Comment=Bullion shortcut
EOF

chmod +x ${shortcut}

sudo apt-get -y install screen </dev/null
