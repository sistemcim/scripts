#!/bin/bash
# This is a sample script to better understand and note command line parameters.
#
# Author: sistemcim
# Blog: https://sistemcim.wordpress.com
# Github: https://github.com/sistemcim
#
# $$ : Process ID
# $0 : Script Command
# $# : Number of Parameters
# $* : All Script Parameters
# $@ : All Script Parameters
# $1, $2, $3,... : Script Parameters

SCRIPT_NAME=$(basename $0)
PID=$$

echo ""
echo "Parameter 0 (\$0): $0"
echo -e "Script name (basename \$0): $SCRIPT_NAME\n"
	
echo "\$*: $*"
echo -e "\$@: $@\n"

if [[ $# -gt 0 ]] 
then
	echo "Command line has $# parameters"

	for i in $@
	do
		let j++
		echo "Parameter $j: $i"
	done
else
	echo "Command line has 0 parameters"
fi

echo ""

#ps aux|grep "/bin/bash $0"|grep -v grep|awk '{print $2}'
# The command above returns one result if run manually. But assignments below return 2 results. I think this is because $() notation creates a subprocess with the same name. 

#PROCESS_ID=$(ps aux|grep "/bin/bash $0"|grep -v grep|awk '{print $2}')
#PROCESS_ID=$(ps aux|grep $SCRIPT_NAME|grep -v grep|awk '{print $2}')

# All processes are retrieved and smallest ID is choosen. Thanks awk...
PROCESS_ID=$(ps aux|grep "/bin/bash $0"|grep -v grep|awk 'BEGIN{smallID=0}{if($2<smallID || smallID==0){smallID=$2}}END{print smallID}')

if [[ $? -eq 0 ]]
then
	echo -e "Exit Status is 0, that means Process Id calculated successully.\n"
else
	echo -e "Exit Status is NOT 0. Problem may have occured in calculating Process Id.\n"
fi

if [[ $PROCESS_ID -eq $PID ]]
then
	echo "Process ID is $PID"
else
	echo "Process ID (Global Variable): $PID"
	echo "Process ID (User Variable): $PROCESS_ID"
fi

echo ""
