FROM nvcr.io/nvidia/pytorch:23.02-py3 as tensorrt-23.02-py3
ENV LANG C.UTF-8
ARG USER=liushuai
ARG PASSWORD=574794581
ARG DEBIAN_FRONTEND=noninteractive
ARG PYTHON_VERSION=py39
ARG MINICOND_VERSION=4.12.0
ARG MINICOND=Miniconda3-${PYTHON_VERSION}_${MINICOND_VERSION}-Linux-x86_64.sh
ARG CMAKE_VERSION=3.26.0-rc6
ARG HOME=/home/${USER}
ARG USER_UID
ARG USER_GID
ARG TMUX_VERSION=3.3a
ARG NODE_VERSION=v18.15.0
LABEL maintainer="bleedingfight <bleedingfight@126.com>"
RUN sed -i '1i\# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\n# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\# 预发布软件源，不建议启用\n\# deb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse' /etc/apt/sources.list 
RUN apt update -y&& apt install apt-utils nmap git wget zsh sudo openssh-server iproute2 mlocate unzip zlib1g-dev libssl-dev libevent-dev libncurses-dev gnutls-bin sqlite3 tree curl ctags npm libvorbis-dev libvpx-dev libvpx-dev libx264-dev libmp3lame-dev libopus-dev libfreetype6-dev nasm libjpeg-dev libpng-dev fish -y  && useradd --create-home --no-log-init --shell /bin/bash ${USER} && usermod -G sudo "${USER}" && echo "${USER}:${PASSWORD}" | chpasswd
RUN wget -c https://github.com/Kitware/CMake/releases/download/v$CMAKE_VERSION/cmake-${CMAKE_VERSION}.tar.gz -O /tmp/cmake-${CMAKE_VERSION}.tar.gz && tar xzvf /tmp/cmake-${CMAKE_VERSION}.tar.gz -C /tmp && cd /tmp/cmake-${CMAKE_VERSION} && ./configure && make -j8 && make install \ 
&& wget -c https://github.com/tmux/tmux/releases/download/$TMUX_VERSION/tmux-$TMUX_VERSION.tar.gz -O /tmp/tmux-$TMUX_VERSION.tar.gz \ 
&& tar xzvf /tmp/tmux-$TMUX_VERSION.tar.gz -C /tmp && cd /tmp/tmux-$TMUX_VERSION && ./configure && make -j8 && mv tmux /usr/local/bin && wget -c https://github.com/neovim/neovim/releases/download/nightly/nvim.appimage \ 
&& chmod a+x nvim.appimage&&./nvim.appimage --appimage-extract &&./squashfs-root/AppRun --version &&mv squashfs-root /&&ln -s /squashfs-root/AppRun /usr/bin/nvim && wget -c https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.xz -O /tmp/node-$NODE_VERSION-linux-x64.tar.xz  &&mkdir /usr/local/node && tar xJvf /tmp/node-$NODE_VERSION-linux-x64.tar.xz -C /usr/local/node && rm -rf /tmp/*
# & git clone --recursive https://github.com/pytorch/pytorch && cd pytorch && git submodule sync && git submodule update --init --recursive --jobs 0  && export USE_CUDA=1
EXPOSE 22
RUN sed -i 's/required/sufficient/g' /etc/pam.d/chsh && chsh -s /usr/bin/zsh && groupadd -r -f -g ${USER_GID} ${USER} && useradd -o -r -l -u ${USER_UID} -g ${USER_GID} -ms /bin/bash ${USER} || true 
USER ${USER}:${USER}
#RUN git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ~/powerlevel10k && mkdir -p $HOME/.config && curl -L git.io/antigen > ${HOME}/.config/antigen.zsh && echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' > ${HOME}/.zshrc && echo 'source ~/.config/antigen.zsh'>>${HOME}/.zshrc && git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm\ 
RUN mkdir -p $HOME/.config && curl -L git.io/antigen > ${HOME}/.config/antigen.zsh && echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' > ${HOME}/.zshrc && echo 'source ~/.config/antigen.zsh'>>${HOME}/.zshrc && git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm\ 
&& wget -c https://mirrors.bfsu.edu.cn/anaconda/miniconda/${MINICOND} -O /tmp/${MINICOND}&&bash /tmp/${MINICOND} -b -p ${HOME}/miniconda3 && rm -rf /tmp/${MINICOND}&& rm -rf /tmp/*
RUN export PATH=${HOME}/miniconda3/bin:${PATH} && python -m pip install -i https://mirrors.bfsu.edu.cn/pypi/web/simple --upgrade pip && pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple\
&& echo "alias vim=nvim">>${HOME}/.zshrc && npm config set registry https://registry.npmmirror.com && npm config set prefix="${HOME}/npm-global" \ 
echo "channels:\n  - defaults\nshow_channel_urls: true\ndefault_channels:\n  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/main\n  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/r\n  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2\ncustom_channels:\n  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud\n  msys2: https://mirrors.bfsu.edu.cn/anaconda/cloud\n  bioconda: https://mirrors.bfsu.edu.cn/anaconda/cloud\n  menpo: https://mirrors.bfsu.edu.cn/anaconda/cloud\n" > ${HOME}/.condarc\ 
&& ${HOME}/miniconda3/bin/conda install astunparse numpy ninja pyyaml setuptools cffi typing_extensions future requests dataclasses mkl-include ipython -y \
&& wget https://github.com/FFmpeg/FFmpeg/archive/refs/tags/n4.1.8.zip -O /tmp/n4.1.8.zip && unzip /tmp/n4.1.8.zip -d /tmp && cd /tmp/FFmpeg-n4.1.8 \ 
&& FFMPEG_ROOT=/usr/local/ffmpeg && export PKG_CONFIG_PATH="$FFMPEG_ROOT/lib/pkgconfig:$PKG_CONFIG_PATH" && ./configure --prefix="$FFMPEG_ROOT" --pkg-config-flags="--static" --extra-cflags="-I$FFMPEG_ROOT/include -fPIC"  --extra-ldflags="-L$FFMPEG_ROOT/lib -Wl,-Bsymbolic" --extra-libs="-lpthread -lm" --bindir="/usr/local/bin" --enable-gpl --enable-libfreetype --enable-libmp3lame --enable-libopus --enable-libvorbis --enable-libvpx --enable-libx264 --enable-pic --enable-shared \ 
&& make -j32 && echo "${PASSWORD}\n"|sudo make install && export LD_LIBRARY_PATH="${FFMPEG_ROOT}/lib":${LD_LIBRARY_PATH}\
&& echo $\'PATH=${PATH}:/usr/local/node/bin\\n\\
WORKDIR ${HOME}
