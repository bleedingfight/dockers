FROM ubuntu:20.04 AS llvm-ubuntu20-dev
ARG USER=liushuai
ARG PASSWORD=574794581
ARG DEBIAN_FRONTEND=noninteractive
ARG HOME=/home/${USER}

RUN apt update && apt install ca-certificates -y&& sed -i '1i\# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\n# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\# 预发布软件源，不建议启用\n\# deb https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse\n\# deb-src https://mirrors.bfsu.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse' /etc/apt/sources.list\
    && apt update&&apt install zsh vim sudo nmap openssh-server iproute2 vim wget curl git apt-utils gnupg2 tree make gcc g++ cmake ninja-build mlocate -y  && useradd --create-home --no-log-init --shell /bin/bash ${USER}&&usermod -G sudo "${USER}"| rm -rf /var/lib/apt/lists/ && echo "${USER}:${PASSWORD}" | chpasswd \
    && mkdir -p /root/.ssh &&mkdir -p /usr/local/llvm&& chown root.root /root && chmod 700 /root/.ssh && chown -R ${USER}.${USER} /etc/ssh &&cd ${HOME}&& git clone https://github.com/llvm/llvm-project.git &&cd llvm-project && cmake -S llvm -Bbuild -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Debug -DLLVM_ENABLE_PROJECTS=mlir -DLLVM_ENABLE_PROJECTS="clang" -DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi"  -DCMAKE_INSTALL_PREFIX=/usr/local/llvm && cd build && make -j16

# && cd llvm-project/build && cmake -G Ninja ../llvm -DLLVM_ENABLE_PROJECTS=mlir -DLLVM_BUILD_EXAMPLES=ON -DLLVM_TARGETS_TO_BUILD="X86;NVPTX;AMDGPU" -DCMAKE_BUILD_TYPE=Release   -DLLVM_ENABLE_ASSERTIONS=ON -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DLLVM_ENABLE_LLD=ON &&cmake --build . --target check-mlir

USER ${USER}

RUN mkdir -p /home/${USER}/.vscode-server/extensions \
        /home/${USER}/.vscode-server-insiders/extensions \
    && chown -R ${USER} \
        /home/${USER}/.vscode-server \
        /home/${USER}/.vscode-server-insiders\
	&& SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=${HOME}/.zsh_history" \
    && echo $SNIPPET >> "${HOME}/.zshrc"
WORKDIR ${HOME}
LABEL Name=llvm-ubuntu-dev Version=0.0.1
