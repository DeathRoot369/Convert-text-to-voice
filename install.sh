#!/usr/bin/env bash

clear

echo "Please enter Password"

sudo apt update
sleep 1
sudo apt install espeak ffmpeg libespeak1
sleep 1
pip install pyttsx3
