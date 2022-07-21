#!/bin/sh
DATE=`date +'%Y%m%d-%H%M%s'`

CATALINA_OPTS="-server -XX:MaxPermSize=256m -XX:PermSize=256m -XX:SurvivorRatio=2 -Xmn256m -Xmx256m -Xms256m" //JVMのサイズは必要に応じて修正
CATALINA_OPTS="${CATALINA_OPTS} -XX:+PrintGCDetails -Xloggc:${CATALINA_BASE}/logs/gc.log.${DATE}"
CATALINA_OPTS="${CATALINA_OPTS} -Djava.security.egd=file:/dev/urandom" //この設定は検証環境の場合

export CATALINA_OPTS
