# Flatpak Functions
import os

def update():
    os.system("flatpak update")

def install(app_name):
    os.system(f"flatpak install {app_name}")

def uninstall(app_name):
    os.system(f"flatpak uninstall {app_name}")

def search(term):
    os.system(f"flatpak search {term}")

def list_():
    os.system("flatpak list")

def list_configured():
    os.system("flatpak remotes")

def info(id_):
    os.system(f"flatpak info {id_}")

def uninstall_unused():
    os.system("flatpak uninstall --unused")