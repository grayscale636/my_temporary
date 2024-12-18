#!/bin/bash

read -p "Masukkan nama file: " file_name
if [ -f "$file_name" ]; then
    echo "$file_name adalah biasa."
elif [ -d "$file_name" ]; then
    echo "$file_name adalah direktori"
elif [ -e "$file_name" ]; then
    echo "$file_name ada tapi bukan file biasa atau direktori"
else
    echo "$file_name tidak ditemukan"
fi
