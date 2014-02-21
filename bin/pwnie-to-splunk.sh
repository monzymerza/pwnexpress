#!/bin/bash
# Author: Pwnie Express (pwnieexpress.com)
# Description: Script to log wireless clients, APs, and Bluetooth devices to Splunk in realtime
# Script revision: 2/20/2014

# Set variables
splunk_server="192.168.56.101"
local_logpath="/var/log/pwnix"
monitor_interface="wlan0"

# Verify we are root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Terminate any existing airodump/bluelog processes
killall screen
killall airodump-ng
killall bluelog
killall tail

# Remove previous session logs and set wlan interface to down state
rm "${local_logpath}"/airodump-* "${local_logpath}"/bluelog-*
ifconfig "${monitor_interface}" down

# Start bluelog and write output to local logfile
bluelog -nfdo "${local_logpath}"/bluelog-devices

# Forward newly detected Bluetooth devices to Splunk server
tail -f "${local_logpath}"/bluelog-devices | logger -u /tmp/ignored -d -P 514 -t bluelog -n "${splunk_server}" &

# Launch a detached airodump session that logs output in CSV format
screen -d -m -S AirodumpSession airodump-ng --output-format=csv --write="${local_logpath}"/airodump "${monitor_interface}"

# Wait at least 5 seconds for airodump to write initial output file
sleep 7

# Create initial list of client devices and forward to Splunk server
cat "${local_logpath}"/airodump-01.csv | tr -d '\r' | tr -cd '\11\12\15\40-\176' | awk -vRS='\nStation MAC' 'NR==2 {print}' | egrep -v "First time seen|^$" | awk -F"," '{print$1","$6","$7,$8,$9,$10,$11,$12,$13,$14,$15,$16}' | tee "${local_logpath}"/airodump-known-clients | logger -u /tmp/ignored -d -P 514 -t wificlient -n "${splunk_server}"

# Create initial list of APs and forward to Splunk server
cat "${local_logpath}"/airodump-01.csv | tr -d '\r' | tr -cd '\11\12\15\40-\176' | awk -vRS='\nStation MAC' 'NR==1 {print}' | egrep -v "^BSSID|^$" | awk -F"," '{print$1","$14","$6}' | tee "${local_logpath}"/airodump-known-APs | logger -u /tmp/ignored -d -P 514 -t wifiap -n "${splunk_server}"


while [ 1 ]
do

  # Extract wireless clients from airodump CSV file, append newly detected clients to airodump-known-clients, and forward newly detected clients to Splunk server
  cat "${local_logpath}"/airodump-01.csv | tr -d '\r' | tr -cd '\11\12\15\40-\176' | awk -vRS='\nStation MAC' 'NR==2 {print}' | egrep -v "First time seen|^$" | awk -F"," '{print$1","$6","$7,$8,$9,$10,$11,$12,$13,$14,$15,$16}' | grep -vxf "${local_logpath}"/airodump-known-clients | tee -a "${local_logpath}"/airodump-known-clients | logger -u /tmp/ignored -d -P 514 -t wificlient -n "${splunk_server}"

  # Extract wireless APs from airodump CSV file, append newly detected APs to airodump-known-APs, and forward newly detected APs to Splunk server
  cat "${local_logpath}"/airodump-01.csv | tr -d '\r' | tr -cd '\11\12\15\40-\176' | awk -vRS='\nStation MAC' 'NR==1 {print}' | egrep -v "^BSSID|^$" | awk -F"," '{print$1","$14","$6}' | grep -vxf "${local_logpath}"/airodump-known-APs | tee -a "${local_logpath}"/airodump-known-APs | logger -u /tmp/ignored -d -P 514 -t wifiap -n "${splunk_server}"

  # Repeat every few seconds
  sleep 3
done

