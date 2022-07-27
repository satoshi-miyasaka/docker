FROM mysql

ARG ROOT_PASS="mysql"
ARG DATABASE="loto"
ARG USER="loto"
ARG PASS="loto"

ENV MYSQL_ROOT_PASSWORD $ROOT_PASS
ENV MYSQL_DATABASE $DATABASE
ENV MYSQL_USER $USER
ENV MYSQL_PASSWORD $PASS

COPY 01_create_db.sql /docker-entrypoint-initdb.d/01_create_db.sql
COPY 02_data_load.sh /docker-entrypoint-initdb.d/02_data_load.sh
COPY loto6.csv /docker-entrypoint-initdb.d/loto6.csv
COPY loto7.csv /docker-entrypoint-initdb.d/loto7.csv

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8


#VOLUME ./db_data:/var/lib/mysql
