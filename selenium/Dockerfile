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

RUN apt install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install jupyterlab

RUN apt install python-dev default-libmysqlclient-dev -y
RUN apt install python3-dev -y
RUN apt install firefox-geckodriver -y
RUN pip install pandas
RUN pip install selenium

