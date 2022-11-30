#! /usr/bin/bash
rm -r build/ dist/ automatic.spec;
pyinstaller -F -c --name automatic main.py;