#!/bin/bash

while :
do
	read -t 1 -n 1 action

	if [[ $action = 1 ]]; 
	then
		/etc/acpi/actions/bl_up.sh
	fi
	if [[ $action = 2 ]]; 
	then
		/etc/acpi/actions/bl_down.sh
	fi
	if [[ $action = q ]];
	then
		break
	fi
done
