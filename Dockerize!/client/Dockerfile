FROM debian:wheezy

RUN apt-get update && apt-get install -y python curl 
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py
RUN pip install pika
COPY entrypoint.sh /
COPY rpc_client.py /
ENTRYPOINT ["/entrypoint.sh"]
