#!/bin/bash
# Bash script sample...
#
# For most of the comments used are taken from 
# ----------- Advanced Bash-Scripting Guide
# ----------- An in-depth exploration of the art of shell scripting
# ----------- Mendel Cooper
#
# Defining variables. No space on each side of "="
IS_GIT_REPO=0
ITEM_COUNT=0
FILE_COUNT=0
DIR_COUNT=0

# ----------- Square Bracket [], Double Square Bracket [[]] and Double Round Bracket (()) ---------------------------------
# The [[ ]] construct is the more versatile Bash version of [ ]. This is the extended test command, adopted from ksh88.
# No filename expansion or word splitting takes place between [[ and ]], but there is parameter expansion and command substitution.
# Using the [[ ... ]] test construct, rather than [ ... ] can prevent many logic errors in scripts. For example, the &&, ||, <, and > operators work within a [[ ]] test, despite giving an error within a [ ] construct.
# The (( )) construct expands and evaluates an arithmetic expression. If the expression evaluates as zero, it returns an exit status of 1, or "false". A non-zero expression returns an exit status of 0, or "true".

# Define directory if any command line parameter specified.
# -n: string is Not NULL
# -z: string is NULL

if [[ -n $1 ]]
then
	DIRECTORY=$1
else
	DIRECTORY="/usr/local/docker"
fi

# Check for .git directory
# -e: file exists
# -f: is a regular fie
# -d: is a directory
# -s: file is not zero size
# -S: is a socket

if [[ -e $DIRECTORY/.git ]]
then
	echo -e "$DIRECTORY folder is a git repository!\n"
	IS_GIT_REPO=1
else
	echo -e "$DIRECTORY folder is NOT a git repository!\n"
fi

if [[ IS_GIT_REPO ]]
then
	ls -l $DIRECTORY
	ITEM_COUNT=$(ls $DIRECTORY|wc -l)
	
#For integer comparison, prefer -eq,-ne,-lt,-le,-gt,-ge,...
#Although it works, < or > checks in ASCII alphabetical order for string comparison.

#The == comparison operator behaves differently within a double-brackets test 
#than within single brackets.

# [[ $a == z* ]]    True if $a starts with an "z" (pattern matching).
# [[ $a == "z*" ]]  True if $a is equal to z* (literal matching).
# [ $a == z* ]      File globbing and word splitting take place.
# [ "$a" == "z*" ]  True if $a is equal to z* (literal matching).

# Thanks, Stéphane Chazelas

	if [[ ITEM_COUNT > 1 ]]
	then
		echo -e "\nThere are $ITEM_COUNT items in the directory..."

		FILE_COUNT=$(find $DIRECTORY -maxdepth 1 -mindepth 1 -type f -not -name ".*"|wc -l)
		DIR_COUNT=$(find $DIRECTORY -maxdepth 1 -mindepth 1 -type d -not -name ".*"|wc -l)
		echo -e "\nCount by type (via find command)"
		echo "File Count: $FILE_COUNT"
		echo "Directory Count: $DIR_COUNT"

		FILE_COUNT=$(ls -l $DIRECTORY|awk 'BEGIN{FS=""}{print $1}'|grep \-|wc -l)
		DIR_COUNT=$(ls -l $DIRECTORY|awk 'BEGIN{FS=""}{print $1}'|grep d|wc -l)
		echo -e "\nCount by type (via awk command)"
		echo "File Count: $FILE_COUNT"
		echo "Directory Count: $DIR_COUNT"

	elif [[ ITEM_COUNT -eq 1 ]]
	then
		echo -e "\nThere is 1 item in the directory..."
	else # ITEM_COUNT -lt 1
		echo -e "\nThere is no item in the directory..."
	fi
fi

