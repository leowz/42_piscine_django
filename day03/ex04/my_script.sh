#!/bin/bash

command -v "virtualenv"
if [[ "${?}" -ne 0 ]]; then
    pip install virtualenv;
fi

virtualenv django_venv --python=python3
source django_venv/bin/activate
pip3 install -r requirement.txt
