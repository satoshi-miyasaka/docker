FROM python
USER root

RUN apt-get update
RUN apt-get -y install locales && \
	localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install jupyterlab

RUN apt install python-dev default-libmysqlclient-dev -y
RUN apt install python3-dev -y
RUN pip install mysqlclient
RUN pip install yahoo_finance_api2
RUN pip install pandas

COPY loto6_predict.py /root/
COPY loto7_predict.py /root/
COPY loto_update.py /root/
COPY data_download.sh /root/

COPY yahoo_finance2.py /root/
