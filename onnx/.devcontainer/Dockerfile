FROM ubuntu:22.04 AS ubuntu22.04
ARG USER 
ARG PASSWORD
ARG HOME 
ARG USER_GID
ARG USER_UID
ARG DEBIAN_FRONTEND=noninteractive

RUN sed -i "s/archive.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list &&apt update && apt install software-properties-common -y && apt-add-repository ppa:fish-shell/release-3 && apt update && apt install ca-certificates  libssl-dev sudo nmap openssh-server iproute2 wget curl git apt-utils gnupg2 make gcc g++ mlocate -y  && useradd --create-home --no-log-init --shell /bin/bash ${USER}&&usermod -G sudo "${USER}"| rm -rf /var/lib/apt/lists/ && echo "${USER}:${PASSWORD}" | chpasswd 

USER ${USER}
ARG MINICONDA=Miniconda3-latest-Linux-x86_64.sh

RUN curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish && wget -c https://mirrors.bfsu.edu.cn/anaconda/miniconda/${MINICONDA} -O ${HOME}/${MINICONDA}\
    &&bash ${HOME}/${MINICONDA} -b -p ${HOME}/miniconda3 \ && sed -i "\$aexport PATH=${HOME}/miniconda3/bin:\${PATH}" ${HOME}/.zshrc \
    && rm -rf ${HOME}/${MINICONDA} && sed -i "\$aexport PATH=/usr/local/${LLVM_PATH}/bin:\${PATH}" ${HOME}/.zshrc\
    && mkdir -p /home/${USER}/.vscode-server/extensions \
        /home/${USER}/.vscode-server-insiders/extensions \
    && chown -R ${USER} \
        /home/${USER}/.vscode-server \
        /home/${USER}/.vscode-server-insiders\
	&& SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=${HOME}/.zsh_history" \
    && echo $SNIPPET >> "${HOME}/.zshrc"
WORKDIR ${HOME}
LABEL Name=Ubuntu22.04 Version=0.0.2
