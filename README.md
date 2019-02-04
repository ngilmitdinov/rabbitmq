exercises from https://www.rabbitmq.com/getstarted.html



##Основной проект в папке Dockerize!. 

Запускаются три контейнера: 
+ server - считает числа Фиббоначи по полученному номеру.
+ client - циклически отправляет номер для вычисления числа ФИббоначи.
+ broker - контейнер с RabbitMQ, контейнеры server и client общаются через очереди.

Инструкция по запуску:
```
git clone https://github.com/ngilmitdinov/rabbitmq.git
cd rabbit/Dockerize\!/
docker-compose up -d 
docker-compose logs -f
```
 
