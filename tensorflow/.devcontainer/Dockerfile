FROM tensorflow/tensorflow:latest as tensorflow-dev
ENV LANG C.UTF-8
ARG USER=liushuai
ARG PASSWORD=574794581
ARG Local=local

LABEL maintainer="bleedingfight <bleedingfight@126.com>"

RUN sed -i '1i\# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\n# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\# 预发布软件源，不建议启用\n\# deb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse' /etc/apt/sources.list \
    && apt update && apt install apt-utils nmap git wget zsh sudo openssh-server iproute2 mlocate -y \
    && useradd --create-home --no-log-init --shell /bin/bash ${USER} && usermod -G sudo "${USER}" \
    && rm -rf /var/lib/apt/lists/ && echo "${USER}:${PASSWORD}" | chpasswd \
    && mkdir -p /root/.ssh && chown root.root /root && chmod 700 /root/.ssh && chown -R ${USER}.${USER} /etc/ssh
USER ${USER}:${USER}
EXPOSE 22
ARG LLVM_TOOLS=clang+llvm-12.0.1-x86_64-linux-gnu-ubuntu-16.04.tar.xz
COPY ${LLVM_TOOLS} ${HOME}
USER ${USER}
ARG HOME=/home/${USER}
ARG SSH_PATH=${HOME}/.ssh
RUN	echo "y\n"|sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"&&echo '${USER}:{PASSWORD}' 

ADD id_rsa.pub ${SSH_PATH}/authorized_keys
ADD ${LLVM_TOOLS} /usr/local/
ENV HOME=${HOME} SSH_PATH=${SSH_PATH} LLVM_TOOLS=${LLVM_TOOLS}
WORKDIR ${HOME}
COPY init.sh ${HOME}
CMD bash ${HOME}/init.sh &&ip addr ls eth0 | awk '{print "Docker ip address:"$2}' | egrep -o '([0-9]+\.){3}[0-9]+' && /usr/sbin/sshd -D
