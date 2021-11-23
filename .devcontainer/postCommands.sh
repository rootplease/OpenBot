#!/bin/bash
echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
source ~/.bashrc
cd /workspace
pre-commit install
pre-commit autoupdate
