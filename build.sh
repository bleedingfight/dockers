#!/bin/bash
local_path='config/local'
workspace=./workspace 
function mkdir_safe(){
	work_path=$1
	if [ ! -d ${work_path} ];then
		mkdir ${work_path}
	fi 
}
mkdir_safe ${local_path}
mkdir_safe ${workspace}

cp ${HOME}/.ssh/id_rsa.pub ${local_path} 
docker-compose up --build
