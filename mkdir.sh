#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 dir_name"
  exit 1
fi

mkdir -p "$1"

echo "alias $2='cd $(pwd)/$1'" >>~/.bashrc

source ~/.bashrc

echo "Dir '$1' created and alias added to ~/.bashrc"
