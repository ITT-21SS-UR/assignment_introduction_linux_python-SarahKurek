#!/bin/bash

# count.sh:
# download a text file from ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README 
# if it is not yet present in the current directory (use wget for this)
# make all text lowercase (use tr )
# split it into individual words per line (use cat and/or sed for this)
# alphabetically sort the list of words and remove duplicates ( sort and uniq , possibly also grep ).
# print out the 10 most common words in the text (without number of occurrences) on stdout ( uniq , sort , and head )

# filename
FILE="README"

# download file from url if it does not exist already
[[ ! -e $FILE ]] && wget ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/$FILE

# read file; make all letters to lowercase; put each word in a new line; remove all special characters; remove all blank lines; 
# sort words alphabetically; delete duplicate words and count their occurrences; sort words according to count; 
# take only the top 10 words and print the words without their occurrences
cat $FILE | tr '[:upper:]' '[:lower:]' | sed 's/[[:space:]]/\n/g' | tr -cd [:alpha:][:space:] | sed '/^$/d'\
| sort  | uniq -c | sort -r | head -10 | awk '{ print $2 }' 
