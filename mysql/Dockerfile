FROM mysql

COPY 01_create_db.sql /docker-entrypoint-initdb.d/01_create_db.sql
COPY 02_create_data.sql /docker-entrypoint-initdb.d/02_create_data.sql

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

ENV MYSQL_ROOT_PASSWORD mysql
ENV MYSQL_USER test
ENV MYSQL_PASSWORD test

#VOLUME ./db_data:/var/lib/mysql
