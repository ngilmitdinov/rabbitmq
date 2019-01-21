FROM rabbitmq
RUN apt-get update && apt-get install -y curl 
EXPOSE 4369 5671 5672 25672 15671 15672
COPY healthcheck.sh /
