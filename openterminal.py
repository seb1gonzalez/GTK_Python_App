import os
import subprocess

def openCommandPrompt():# for windows
    command = "cmd"
   # os.system(command)
    subprocess.Popen(command)

def openTerminalLinux():# for linux
    os.system("gnome-terminal")

