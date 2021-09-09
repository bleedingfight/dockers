#!/bin/bash
local_path='local'
if [ ! -d ${local_path} ] ;then 
  mkdir ${local_path}
fi 
cp ${HOME}/.ssh/id_rsa.pub ${local_path} 
docker-compose up