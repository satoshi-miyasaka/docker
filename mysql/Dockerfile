FROM mysql

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

ENV MYSQL_DATABASE=loto
ENV MYSQL_ALLOW_EMPTY_PASSWORD="yes"

COPY 01_create_db.sql /docker-entrypoint-initdb.d/01_create_db.sql
COPY 02_data_load.sh /docker-entrypoint-initdb.d/02_data_load.sh
COPY loto6.csv /docker-entrypoint-initdb.d/loto6.csv
COPY loto7.csv /docker-entrypoint-initdb.d/loto7.csv

#VOLUME ./db_data:/var/lib/mysql
