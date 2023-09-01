#!/usr/bin/env bash

printf "Content-Type: text/tab-separated-values; charset=UTF-8\r\n"
printf "\r\n"

# list files in folder and show only basename
ls ${DATADIR}/*tsv | awk -F/ '{print $NF}'