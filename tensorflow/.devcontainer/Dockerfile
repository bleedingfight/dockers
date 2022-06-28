FROM nvidia/cuda:11.6.2-cudnn8-devel-ubuntu20.04 as tensorflow-dev
ENV LANG C.UTF-8
ARG USER=liushuai
ARG PASSWORD=574794581
ARG Local=local
ARG DEBIAN_FRONTEND=noninteractive
ARG PYTHON_VERSION=py39
ARG MINICOND_VERSION=4.12.0
ARG MINICOND=Miniconda3-${PYTHON_VERSION}_${MINICOND_VERSION}-Linux-x86_64.sh
ARG BAZEL=bazel_5.1.1-linux-x86_64.deb
LABEL maintainer="bleedingfight <bleedingfight@126.com>"

RUN sed -i '1i\# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\n# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\# 预发布软件源，不建议启用\n\# deb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse' /etc/apt/sources.list 
RUN apt update -y&& apt install apt-utils nmap git wget zsh sudo openssh-server iproute2 mlocate unzip zlib1g-dev -y \
    && useradd --create-home --no-log-init --shell /bin/bash ${USER} && usermod -G sudo "${USER}" \
    && echo "${USER}:${PASSWORD}" | chpasswd \
    && mkdir -p /root/.ssh && chown root.root /root && chmod 700 /root/.ssh && chown -R ${USER}.${USER} /etc/ssh && wget -d https://mirrors.bfsu.edu.cn/anaconda/miniconda/${MINICOND} -O /tmp/${MINICOND}&&bash /tmp/${MINICOND} -b -p ${HOME}/miniconda3 && rm -rf /tmp/${MINICOND} && wget -d https://github.com/bazelbuild/bazel/releases/download/5.1.1/${BAZEL} -O /tmp/${BAZEL} && apt install -f && dpkg -i /tmp/${BAZEL} && rm -rf /tmp/* &&export PATH=${HOME}/miniconda3/bin:${PATH} && python -m pip install -i https://mirrors.bfsu.edu.cn/pypi/web/simple --upgrade pip && pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple &&pip install numpy  && echo "PATH=\${PATH}:${HOME}/miniconda3/bin>>${HOME}/.bashrc"
USER ${USER}:${USER}
EXPOSE 22
USER ${USER}
ARG HOME=/home/${USER}
ARG SSH_PATH=${HOME}/.ssh
# RUN	echo "y\n"|sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"&&echo '${USER}:{PASSWORD}' 

WORKDIR ${HOME}
COPY init.sh ${HOME}
CMD bash ${HOME}/init.sh &&ip addr ls eth0 | awk '{print "Docker ip address:"$2}' | egrep -o '([0-9]+\.){3}[0-9]+' && /usr/sbin/sshd -D
