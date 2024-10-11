#!bin/bash

clear

echo "Installing required dependencies"
	sleep 3
	apt update && upgrade
	
echo "Installing python"
	sleep 3
	apt install python

echo "Installing pip"
	sleep 3
	apt install pip

echo "Installing jinja2"
	sleep 3
	pip install jinja2

echo "Installing markdown2"
	sleep 3
	pip install markdown2
