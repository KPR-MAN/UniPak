# Snap Functions
import os

def refresh():
    os.system("snap refresh")

def install(app_name):
    os.system(f"snap install {app_name}")

def remove(app_name):
    os.system(f"snap remove {app_name}")

def find(term):
    os.system(f"snap find {term}")

def list_():
    os.system("snap list")

def info(name):
    os.system(f"snap info {name}")

def refresh_list():
    os.system("snap refresh --list")