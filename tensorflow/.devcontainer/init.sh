#!/bin/bash
if [ -f ${HOME}/${LLVM_TOOLS} ];then
	echo ${PASSWORD}|sudo tar xzvf ${HOME}/${LLVM_TOOLS} -C /usr/local
	echo "PATH=/usr/local/${LLVM_TOOLS:0:-7}/bin:\${PATH}">>${HOME}/.zshrc
	rm -rf ${HOME}/${LLVM_TOOLS}
fi
