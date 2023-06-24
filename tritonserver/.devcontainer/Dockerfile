FROM ubuntu:22.04 AS ubuntu22.04-triton-dev
ARG HOME 
ARG uid
ARG gid
ARG USER
ARG PASSWORD

ARG DEBIAN_FRONTEND=noninteractive

RUN sed -i "s/archive.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list &&apt update && apt install software-properties-common -y && apt-add-repository ppa:fish-shell/release-3 && apt update && apt install fish 
RUN echo $PASSWORD && echo $USER && echo $uid
RUN apt install ca-certificates  libssl-dev sudo nmap openssh-server iproute2 wget curl git apt-utils gnupg2 make gcc g++ mlocate -y


RUN groupadd -r -f -g ${gid} ${USER} && useradd -o -r -l -u ${uid} -g ${gid} -ms /bin/bash ${USER}
RUN usermod -aG sudo ${USER}
RUN echo ${USER}:${PASSWORD} | chpasswd
USER ${USER}
ARG MINICONDA=Miniconda3-latest-Linux-x86_64.sh

RUN curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish && wget -c https://mirrors.bfsu.edu.cn/anaconda/miniconda/${MINICONDA} -O ${HOME}/${MINICONDA}\
    &&bash ${HOME}/${MINICONDA} -b -p ${HOME}/miniconda3 \ && sed -i "\$aexport PATH=${HOME}/miniconda3/bin:\${PATH}" ${HOME}/.zsh
WORKDIR ${HOME}
LABEL Name=triton Version=0.0.2
