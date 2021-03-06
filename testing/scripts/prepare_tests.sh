#!/bin/bash

# this script is running as root and prepares the test environment

echo "cleaning tmp"
rm -rf /tmp/ws
echo "copying ws.conf"
cp input/ws.conf.1 /etc/ws.conf
echo "creating users and groups"
addgroup groupa
addgroup groupb
addgroup groupc
adduser --quiet --gecos "" --disabled-password useradmin
adduser --quiet --gecos "" --ingroup groupa --disabled-password usera
adduser --quiet --gecos "" --ingroup groupb --disabled-password userb
adduser --quiet --gecos "" --ingroup groupc --disabled-password userc
usermod -a -G groupa userc

echo create workspaces etc
../contribs/ws_prepare

chown root ../bin/ws_allocate ../bin/ws_release ../bin/ws_restore
chmod u+s ../bin/ws_allocate ../bin/ws_release ../bin/ws_restore

