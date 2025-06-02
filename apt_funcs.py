# APT Functions
import os

def update():
    os.system("sudo apt update")
    
def upgrade():
    os.system("sudo apt upgrade")
    
def full_upgrade():
    os.system("sudo apt full-upgrade")
    
def install(app_name):
    os.system(f"sudo apt install {app_name}")

def remove(app_name):
    os.system(f"sudo apt remove {app_name}")

def purge(app_name):
    os.system(f"sudo apt purge {app_name}")
    
def auto_remove():
    os.system("sudo apt autoremove")
    
def search(keyword):
    os.system(f"sudo apt search {keyword}")
    
def show(app_name):
    os.system(f"sudo apt show {app_name}")
    
def list_installed():
    os.system("sudo apt list --installed")
    
def list_upgradable():
    os.system("sudo apt list --upgradable")
    
def update_fix_missing():
    os.system("sudo apt update --fix-missing")
    
def clean():
    os.system("sudo apt clean")