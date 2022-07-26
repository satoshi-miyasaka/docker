mysql -uroot -pmysql --local-infile=1 loto -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/loto6.csv' INTO TABLE loto.loto6 FIELDS TERMINATED BY ',' ENCLOSED BY '\"'"
mysql -uroot -pmysql --local-infile=1 loto -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/loto7.csv' INTO TABLE loto.loto7 FIELDS TERMINATED BY ',' ENCLOSED BY '\"'"
