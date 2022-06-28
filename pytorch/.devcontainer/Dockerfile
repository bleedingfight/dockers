FROM nvidia/cuda:11.6.2-cudnn8-devel-ubuntu20.04 as pytorch-dev
ENV LANG C.UTF-8
ARG USER=liushuai
ARG PASSWORD=574794581
ARG DEBIAN_FRONTEND=noninteractive
ARG PYTHON_VERSION=py39
ARG MINICOND_VERSION=4.12.0
ARG MINICOND=Miniconda3-${PYTHON_VERSION}_${MINICOND_VERSION}-Linux-x86_64.sh

LABEL maintainer="bleedingfight <bleedingfight@126.com>"

RUN sed -i '1i\# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\n# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\# 预发布软件源，不建议启用\n\# deb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse' /etc/apt/sources.list 
RUN apt update -y&& apt install apt-utils nmap git wget zsh sudo openssh-server iproute2 mlocate unzip zlib1g-dev -y 
RUN useradd --create-home --no-log-init --shell /bin/bash ${USER} && usermod -G sudo "${USER}" \
    && echo "${USER}:${PASSWORD}" | chpasswd \
    && mkdir -p /root/.ssh && chown root.root /root && chmod 700 /root/.ssh && chown -R ${USER}.${USER} /etc/ssh
RUN wget -d https://mirrors.bfsu.edu.cn/anaconda/miniconda/${MINICOND} -O /tmp/${MINICOND}&&bash /tmp/${MINICOND} -b -p ${HOME}/miniconda3 && rm -rf /tmp/${MINICOND}&& rm -rf /tmp/* && echo "\n" > ${HOME}/.condarc && sed -i '1ichannels:\n- defaults\nshow_channel_urls: true\ndefault_channels:\n- https://mirrors.bfsu.edu.cn/anaconda/pkgs/main\n- https://mirrors.bfsu.edu.cn/anaconda/pkgs/r\n - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2\ncustom_channels:\n  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud\n  msys2: https://mirrors.bfsu.edu.cn/anaconda/cloud\n  bioconda: https://mirrors.bfsu.edu.cn/anaconda/cloud\n  menpo: https://mirrors.bfsu.edu.cn/anaconda/cloud\n  pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud\n  pytorch-lts: https://mirrors.bfsu.edu.cn/anaconda/cloud\n  simpleitk: https://mirrors.bfsu.edu.cn/anaconda/cloud' ${HOME}/.condarc &&export PATH=${HOME}/miniconda3/bin:${PATH}&& conda install astunparse numpy ninja pyyaml setuptools cmake cffi typing_extensions future six requests dataclasses mkl mkl-include -y && python -m pip install -i https://mirrors.bfsu.edu.cn/pypi/web/simple --upgrade pip && pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple && apt install vim ctags -y
# && git clone --recursive https://github.com/pytorch/pytorch && cd pytorch && git submodule sync && git submodule update --init --recursive --jobs 0  && export USE_CUDA=1
USER ${USER}:${USER}
EXPOSE 22
USER ${USER}
ARG HOME=/home/${USER}
# RUN	echo "y\n"|sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"&&echo '${USER}:{PASSWORD}' 

WORKDIR ${HOME}
COPY init.sh ${HOME}
CMD bash ${HOME}/init.sh &&ip addr ls eth0 | awk '{print "Docker ip address:"$2}' | egrep -o '([0-9]+\.){3}[0-9]+' && /usr/sbin/sshd -D
