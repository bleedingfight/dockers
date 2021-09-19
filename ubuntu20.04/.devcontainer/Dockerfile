FROM ubuntu:20.04 AS ubuntu20.04
ARG USER=liushuai
ARG PASSWORD=574794581
ARG DEBIAN_FRONTEND=noninteractive
ARG HOME=/home/${USER}

RUN apt update && apt install ca-certificates -y&& sed -i '1i\# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\n# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\# 预发布软件源，不建议启用\n\# deb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse' /etc/apt/sources.list\
    && apt update&&apt install zsh vim sudo nmap openssh-server iproute2 vim wget curl git apt-utils tree make gcc g++ -y  && useradd --create-home --no-log-init --shell /bin/bash ${USER}&&usermod -G sudo "${USER}"| rm -rf /var/lib/apt/lists/ && echo "${USER}:${PASSWORD}" | chpasswd \
    && mkdir -p /root/.ssh && chown root.root /root && chmod 700 /root/.ssh && chown -R ${USER}.${USER} /etc/ssh
USER ${USER}

ARG MINICONDA=Miniconda3-py38_4.9.2-Linux-x86_64.sh LLVM=clang+llvm-12.0.1-x86_64-linux-gnu-ubuntu-16.04.tar.xz LLVM_PATH=clang+llvm-12.0.1-x86_64-linux-gnu-ubuntu-
ADD ${LLVM} /usr/local
RUN echo "yes\n"|sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && wget -c https://mirrors.bfsu.edu.cn/anaconda/miniconda/${MINICONDA} -O ${HOME}/${MINICONDA}\
    &&bash ${HOME}/${MINICONDA} -b -p ${HOME}/miniconda3 \
    && rm -rf ${HOME}/${MINICONDA} && sed -i "\$aexport PATH=/usr/local/${LLVM_PATH}/bin:\${PATH}" ${HOME}/.zshrc\
    && mkdir -p /home/${USER}/.vscode-server/extensions \
        /home/${USER}/.vscode-server-insiders/extensions \
    && chown -R ${USER} \
        /home/${USER}/.vscode-server \
        /home/${USER}/.vscode-server-insiders
WORKDIR ${HOME}
LABEL Name=Ubuntu20.04 Version=0.0.1
