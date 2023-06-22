#!/bin/bash
local_path='.devcontainer/.ssh'
workspace=./workspace
function mkdir_safe() {
	work_path=$1
	if [ ! -d ${work_path} ]; then
		mkdir ${work_path}
	fi
}
mkdir_safe ${local_path}

PASSWORD=574794581
cp -r ${HOME}/.ssh/id_rsa.pub ${local_path}
# docker-compose --build --build-arg USER_UID=$(id -u) --build-arg USER_GID=$(id -g) .
docker-compose build --build-arg USER_UID=$(id -u) --build-arg USER_GID=$(id -g) --build-arg USER=$(whoami) --build-arg PASSWORD=$PASSWORD
docker-compose up -d
