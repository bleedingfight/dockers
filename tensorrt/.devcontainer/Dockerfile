#
# SPDX-FileCopyrightText: Copyright (c) 1993-2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

ARG CUDA_VERSION=12.0.1

FROM nvidia/cuda:${CUDA_VERSION}-cudnn8-devel-ubuntu20.04 as tensorrt-develop-cudnn8-devel-ubuntu20.04
LABEL maintainer="bleedingfight@126.com"

ENV TRT_VERSION 8.6.1.6
SHELL ["/bin/bash", "-c"]

# Setup user account
ARG uid
ARG gid
ARG USER
ARG PASSWORD

RUN groupadd -r -f -g ${gid} ${USER} && useradd -o -r -l -u ${uid} -g ${gid} -ms /bin/bash ${USER}
RUN usermod -aG sudo ${USER}
RUN echo ${USER}:${PASSWORD} | chpasswd
RUN mkdir -p /workspace && chown ${USER} /workspace

# Required to build Ubuntu 20.04 without user prompts with DLFW container
ENV DEBIAN_FRONTEND=noninteractive

# Update CUDA signing key
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub

# Install requried libraries
RUN sed -i "s/archive.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list && apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    fish \
    wget \
    git \
    pkg-config \
    sudo \
    ssh \
    libssl-dev \
    pbzip2 \
    pv \
    bzip2 \
    unzip \
    devscripts \
    lintian \
    fakeroot \
    dh-make \
    build-essential

# Install python3
RUN apt-get install -y --no-install-recommends \
      python3 \
      python3-pip \
      python3-dev \
      python3-wheel &&\
    cd /usr/local/bin &&\
    ln -s /usr/bin/python3 python &&\
    ln -s /usr/bin/pip3 pip;

# Install TensorRT
RUN if [ "${CUDA_VERSION}" = "10.2" ] ; then \
    v="${TRT_VERSION%.*}-1+cuda${CUDA_VERSION}" &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub &&\
    apt-get update &&\
    sudo apt-get install libnvinfer8=${v} libnvonnxparsers8=${v} libnvparsers8=${v} libnvinfer-plugin8=${v} \
        libnvinfer-dev=${v} libnvonnxparsers-dev=${v} libnvparsers-dev=${v} libnvinfer-plugin-dev=${v} \
        python3-libnvinfer=${v} libnvinfer-dispatch8=${v} libnvinfer-dispatch-dev=${v} libnvinfer-lean8=${v} \
        libnvinfer-lean-dev=${v} libnvinfer-vc-plugin8=${v} libnvinfer-vc-plugin-dev=${v} \
        libnvinfer-headers-dev=${v} libnvinfer-headers-plugin-dev=${v}; \
else \
    v="${TRT_VERSION}-1+cuda${CUDA_VERSION%.*}" &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub &&\
    apt-get update &&\
    sudo apt-get -y install libnvinfer8=${v} libnvonnxparsers8=${v} libnvparsers8=${v} libnvinfer-plugin8=${v} \
        libnvinfer-dev=${v} libnvonnxparsers-dev=${v} libnvparsers-dev=${v} libnvinfer-plugin-dev=${v} \
        python3-libnvinfer=${v} libnvinfer-dispatch8=${v} libnvinfer-dispatch-dev=${v} libnvinfer-lean8=${v} \
        libnvinfer-lean-dev=${v} libnvinfer-vc-plugin8=${v} libnvinfer-vc-plugin-dev=${v} \
        libnvinfer-headers-dev=${v} libnvinfer-headers-plugin-dev=${v}; \
fi

# Install PyPI packages
RUN pip3 install --upgrade pip && pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install setuptools>=41.0.0
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
RUN pip3 install jupyter jupyterlab
# Workaround to remove numpy installed with tensorflow
RUN pip3 install --upgrade numpy

# Install Cmake
RUN cd /tmp && \
    wget https://github.com/Kitware/CMake/releases/download/v3.14.4/cmake-3.14.4-Linux-x86_64.sh && \
    chmod +x cmake-3.14.4-Linux-x86_64.sh && \
    ./cmake-3.14.4-Linux-x86_64.sh --prefix=/usr/local --exclude-subdir --skip-license && \
    rm ./cmake-3.14.4-Linux-x86_64.sh

# Download NGC client
RUN cd /usr/local/bin && wget https://ngc.nvidia.com/downloads/ngccli_cat_linux.zip && unzip ngccli_cat_linux.zip && chmod u+x ngc-cli/ngc && rm ngccli_cat_linux.zip ngc-cli.md5 && echo "no-apikey\nascii\n" | ngc-cli/ngc config set

# Set environment and working directory
ENV TRT_LIBPATH /usr/lib/x86_64-linux-gnu
ENV TRT_OSSPATH /workspace/TensorRT
ENV PATH="${PATH}:/usr/local/bin/ngc-cli"
ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${TRT_OSSPATH}/build/out:${TRT_LIBPATH}"
WORKDIR /workspace

ARG NODE_VERSION=v18.15.0
RUN apt install curl -y && wget -c https://github.com/neovim/neovim/releases/download/nightly/nvim.appimage \ 
&& chmod a+x nvim.appimage &&./nvim.appimage --appimage-extract &&mv squashfs-root /usr/nvim&&ln -s /usr/nvim/AppRun /usr/bin/vim && wget -c https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.xz -O /tmp/node-$NODE_VERSION-linux-x64.tar.xz  &&mkdir /usr/local/node && tar xJvf /tmp/node-$NODE_VERSION-linux-x64.tar.xz -C /usr/local/node && rm -rf /tmp/ 
USER $USER
RUN curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish && git clone -b lite https://github.com/bleedingfight/nvimdots.git ${HOME}/.config/nvim 
RUN ["/bin/bash"]
