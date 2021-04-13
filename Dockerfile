FROM python:3.8-buster
LABEL maintainer="ewald.dobre@gmail.com"

WORKDIR /root

RUN git clone --depth=1 https://github.com/ewald98/code-feels.git && \
	cd /root/code-feels && \
	pip3 install . -r requirements.txt

RUN pip3 install --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint

CMD /bin/bash
