#!/bin/bash

# Install needed system requirements for the project
echo "Starting installing of system packages."
sudo add-apt-repository ppa:ethereum/ethereum
sudo apt update
sudo apt install -y build-essential gcc libssl-dev autoconf solc python3-dev \
python3-pip pkg-config
