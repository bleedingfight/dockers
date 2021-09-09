FROM tensorflow/tensorflow:latest as tensorflow-dev
ENV LANG C.UTF-8
ARG USER=liushuai
ARG PASSWORD=574794581

RUN sed -i '1i\# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\n# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\# 预发布软件源，不建议启用\n\# deb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse' /etc/apt/sources.list \
    && apt-get update && apt install apt-utils nmap git wget zsh sudo openssh-server iproute2 -y \
    && useradd --create-home --no-log-init --shell /bin/bash ${USER} && usermod -G sudo "${USER}" \
    && rm -rf /var/lib/apt/lists/ && echo "${USER}:${PASSWORD}" | chpasswd
RUN mkdir -p /root/.ssh && chown root.root /root && chmod 700 /root/.ssh && chown -R ${USER}.${USER} /etc/ssh 
EXPOSE 22
USER ${USER}
ENV HOME=/home/${USER}
WORKDIR /home/${USER}
ARG SSH_PATH=${HOME}/.ssh
RUN mkdir ${SSH_PATH} && echo ${PASSWORD} && chmod 700 ${SSH_PATH} && echo "Y\n"|sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
CMD ip addr ls eth0 | awk '{print $2}' | egrep -o '([0-9]+\.){3}[0-9]+';
CMD /usr/sbin/sshd -D

