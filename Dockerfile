FROM ubuntu:20.04

RUN apt update

RUN ln -fs /usr/share/zoneinfo/Europe/Madrid /etc/localtime
RUN apt install -y tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN apt install -y texlive-full python3-pygments

WORKDIR /project

CMD cd template && pdflatex -shell-escape -interaction=nonstopmode -halt-on-error main
