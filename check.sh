#!/bin/bash

# Function to check if directory contains ".md" files
x=0
y=1
check_directory() {
    local dir="$1"
    local found_files=false

    # Loop through files and directories in the given directory
    for file in "$dir"/*; do
        if [[ -d "$file" ]]; then
            # Recursively check subdirectories
            check_directory "$file"
        elif [[ -f "$file" && $file == *.md ]]; then
            found_files=true
            printf "`echo adsdasfdas | cut -d '/' -f1`\n"
        fi
    done
    # Print directory path in red if ".md" files are found
    total_spaces=90
    if [[ $found_files == true ]]; then
        length=${#dir}                      # get length of the dir
        spaces=$((total_spaces - length))   # spaces to print yes virtecaly
        newDir="${dir#./}"                  # remove ./ form prifex of dir 
        dirs_array=()                       # empty array to append the base dirs 

                    # get base dirs
        base_dirs=`find . -maxdepth 1 -type d ! -name '.*' -printf '%f\n'` 

                    # to append the base dirs in array 
        for i in $base_dirs
        do
            dirs_array+=("$i")
        done


        if [[ "${dirs_array[x]}" == `echo $newDir | cut -d '/' -f1` ]]
        then
            if [[ $y == 1 ]]
            then 
                printf "\t\t\t\t${dirs_array[x]}\n"
                y=0
            fi
        else
            printf "\n"
            x=`expr $x + 1`
            y=`expr $y + 1`
        fi
        
        printf "\e[31m$newDir\e[0m"        # print the dir path with red color

                    # loop for print specific spaces
        for (( i=0; i<spaces; i++ ))
        do
            printf " "
        done

                    # to print yes side to dir path without .
        if [[ $spaces != 89 ]];then
            printf "\e[32mDone\e[0m\n"
        fi
    fi
}

# Start checking from the current directory
check_directory "."



# echo "Length of the string is: $length"
