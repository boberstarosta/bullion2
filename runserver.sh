#!/bin/bash
echo "Script executed from: ${PWD}"

cat <<EOF >./Bullion.desktop
[Desktop Entry]
Type=Application
Exec=${PWD}/runserver.sh
Icon=${PWD}/icon.png
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Bullion
GenericName=bullion
X-GNOME-FullName=Bullion
Comment=Bullion shortcut
EOF

#sudo apt-get -y install screen </dev/null

#screen
#source ./venv/bin/activate
#./venv/bin/python3 manage.py runserver localhost:8080 --noreload
#screen -d
