#!/usr/bin/env bash

clear

echo "Please enter Password"
sudo su

clear

sudo apt update
sleep1
sudo apt install espeak ffmpeg libespeak1
sleep1
pip install pyttsx3
