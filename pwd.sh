#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 alias_name"
  exit 1
fi

dir=$(pwd)

echo "alias $1='cd $dir'" >>~/.bashrc

source ~/.bashrc

echo "Alias '$1' added for dir '$current_dir'"
