FROM ubuntu:latest

ARG HOST_IP
ENV DISPLAY=:0

RUN apt update && apt install -y \
    ns2 \
    default-jre \
    dpkg \
    x11-utils

COPY nam_1.14_amd64.deb /tmp/nam.deb
RUN dpkg -i /tmp/nam.deb && apt install -f

CMD ["bash"]
