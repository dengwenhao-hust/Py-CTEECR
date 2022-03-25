#!/bin/bash

path=$(cd `dirname $0`;pwd)
for file in $(ls $path); do
        dir_name="$path/$file"
        if test -d $dir_name;then
                cd $dir_name
                qsub qchems.pbs
                cd ..
	fi
done

