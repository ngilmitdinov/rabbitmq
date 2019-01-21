FROM debian:wheezy

RUN apt-get update && apt-get install -y python curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py
RUN pip install pika

COPY rpc_server.py /
COPY entrypoint.sh /
COPY wait-for-it.sh /

ENTRYPOINT ["/entrypoint.sh"]
