#! /usr/bin/bash
# rm -r build/ dist/ automatic.spec;
pyinstaller -F -c --name automatic main.py;
# pyinstaller -F -w --name automatic main.py;