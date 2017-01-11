#!/bin/bash

A1="DROP USER 'airbnb_user_dev'@'%';"
A2="DROP USER 'airbnb_user_prod'@'localhost';"

drop="${A1}${A2}"

mysql -u root -p -e "$drop"
