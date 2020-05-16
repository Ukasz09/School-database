#!/bin/bash

generate_data()
{
 cd data_generator/
 python3 main.py
}

copy_data_to_db_dir()
{
 data_dir=$(sudo -u postgres -H -- psql -d SchoolDB -c "SHOW data_directory" | grep /)
 yes | cp -r csv_schoolDB $data_dir
 echo Copied csv data to $data_dir
}

generate_data
copy_data_to_db_dir
