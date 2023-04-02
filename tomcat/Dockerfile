FROM tomcat:8.5

COPY tomcat/setenv.sh bin/
COPY ./app/build/libs/app.war /usr/local/tomcat/webapps/
COPY ./conf/server.xml /usr/local/tomcat/conf/

EXPOSE 8080
CMD ["bin/catalina.sh", "run"]
