FROM ubuntu:16.04

MAINTAINER Uchenna Nebedum "nebeduch@gmail.com"

RUN apt-get update -y && \
    apt-get install -y nginx zip curl python-pip python-dev && \
    pip install --upgrade pip

RUN cd /opt && curl -o thelastprice.com.ng.zip -L https://github.com/nebed/thelastprice.com.ng/archive/master.zip && unzip thelastprice.com.ng.zip && mv thelastprice.com.ng-master thelastprice.com.ng && \
    rm -f thelastprice.com.ng.zip && cd thelastprice.com.ng && pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "/opt/thelastprice.com.ng/app.py" ]