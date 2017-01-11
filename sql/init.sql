#!/bin/bash

#=========================================================================================#
#This script will create a dev user and database as well as a production user and database.
#The production user privileges require the user to only access its database locally while,
#the dev user privileges require the user to access its database from any other machine.
#=========================================================================================#

#Enter desired password for both newly created users so it is not stored in this script.
echo "Enter desired password for newly created user: airbnb_user_dev"
read -sr PW1

A1="CREATE USER 'airbnb_user_dev'@'%' IDENTIFIED BY '$PW1';"

echo "Enter desired password for newly created user: airbnb_user_prod"
read -sr PW2

A2="CREATE USER 'airbnb_user_prod'@'localhost' IDENTIFIED BY '$PW2';"

A3="CREATE DATABASE IF NOT EXISTS airbnb_dev CHARACTER SET utf8 COLLATE utf8_general_ci;"

A4="CREATE DATABASE IF NOT EXISTS airbnb_prod CHARACTER SET utf8 COLLATE utf8_general_ci;"

A5="GRANT ALL PRIVILEGES ON airbnb_dev.* TO 'airbnb_user_dev'@'%';"

A6="GRANT ALL PRIVILEGES ON airbnb_prod.* TO 'airbnb_user_prod'@'localhost';"

A7="FLUSH PRIVILEGES;"

SQL="${A1}${A2}${A3}${A4}${A5}${A6}${A7}"

mysql -u root -p -e "$SQL"
