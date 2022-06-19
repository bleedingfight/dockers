FROM ubuntu:20.04 AS ubuntu20.01-opencv-dev

ARG USER=liushuai
ARG PASSWORD=574794581
ARG DEBIAN_FRONTEND=noninteractive
ARG HOME=/home/${USER}

RUN apt update && apt install ca-certificates -y&& sed -i '1i\# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\n# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\# 预发布软件源，不建议启用\n\# deb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse' /etc/apt/sources.list\
    && apt update&&apt install zsh vim sudo nmap openssh-server iproute2 vim wget curl git apt-utils gnupg2 tree make gcc g++ cmake mlocate zlib1g-dev ccache libeigen3-dev -y  && useradd --create-home --no-log-init --shell /bin/bash ${USER}&&usermod -G sudo "${USER}"| rm -rf /var/lib/apt/lists/ && echo "${USER}:${PASSWORD}" | chpasswd \
    && mkdir -p /root/.ssh && chown root.root /root && chmod 700 /root/.ssh && chown -R ${USER}.${USER} /etc/ssh
USER ${USER}

RUN echo "yes\n"|sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && wget -c https://mirrors.bfsu.edu.cn/anaconda/miniconda/${MINICONDA} -O ${HOME}/${MINICONDA}\
    &&bash ${HOME}/${MINICONDA} -b -p ${HOME}/miniconda3 \ && sed -i "\$aexport PATH=${HOME}/miniconda3/bin:\${PATH}" ${HOME}/.zshrc \
    && rm -rf ${HOME}/${MINICONDA} && sed -i "\$aexport PATH=/usr/local/${LLVM_PATH}/bin:\${PATH}" ${HOME}/.zshrc\
    && mkdir -p /home/${USER}/.vscode-server/extensions \
        /home/${USER}/.vscode-server-insiders/extensions \
    && chown -R ${USER} \
        /home/${USER}/.vscode-server \
        /home/${USER}/.vscode-server-insiders\
        && SNIPPET="export PROMPT_COMMAND='history -xport HISTFILE=${HOME}/.zsh_history" \
    && echo $SNIPPET >> "${HOME}/.zshrc"
WORKDIR ${HOME}

LABEL Name=opencv Version=0.0.1
