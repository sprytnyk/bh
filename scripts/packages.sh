#!/bin/bash

# Install needed system requirements for the project
echo "Starting installing of system packages."
sudo add-apt-repository ppa:ethereum/ethereum
sudo apt update
sudo apt install -y build-essential gcc libssl-dev autoconf solc python3-dev \
python3-pip pkg-config
sudo pip3 install virtualevnwrapper
echo "
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
export PIP_VIRTUALENV_BASE=$WORKON_HOME
" >> ~/.bashrc
source ~/.bashrc
