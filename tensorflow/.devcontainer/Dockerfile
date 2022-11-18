FROM ubuntu20-tensorflow-master-cuda11.2 as tensorflow-master-cuda11.2-ubuntu20-dev
ENV LANG C.UTF-8
ARG USER=liushuai
ARG PASSWORD=574794581
ARG Local=local
ARG BAZEL=bazel_5.1.1-linux-x86_64.deb
LABEL maintainer="bleedingfight <bleedingfight@126.com>"

EXPOSE 22

CMD bash ${HOME}/init.sh &&ip addr ls eth0 | awk '{print "Docker ip address:"$2}' | egrep -o '([0-9]+\.){3}[0-9]+' && /usr/sbin/sshd -D
