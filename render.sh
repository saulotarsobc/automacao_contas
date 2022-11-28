#! /usr/bin/bash
rm -r build/ dist/ automatic.spec
pyinstaller -F -w --name automatic main.py
