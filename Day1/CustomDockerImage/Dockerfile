FROM ubuntu:16.04
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org>

RUN apt-get update && apt-get install -y vim net-tools
RUN apt-get update && apt-get install -y apache2

COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

CMD ["/etc/init.d/apache2", "start"]
