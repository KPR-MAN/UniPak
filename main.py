# Main App

# Imports
import os
import apt_funcs
import flatpak_funcs
import snap_funcs
import unipak_print_commands


# Variables/Booleans
command = ""
running = True
no_selected_choice_apt_menu = True
no_selected_choice_flatpak_menu = True
no_selected_choice_snap_menu = True
no_selected_choice_pm_install_menu = True

# Clear Terminal
os.system("clear")

# Welcome Message
print("UniPak - MAIN MENU INTERFACE")
print("____________________________")

while running:
    # Main Menu Code
    print("1. Preform APT Operations")
    print("2. Preform Flatpak Operations")
    print("3. Preform Snap Operations")
    print("4. Install Package Managers")
    print("5. Exit")
    print("_____________________________")
    command = int(input("Enter your choice -> "))
    match command:
        case 1:
               os.system("clear")
               no_selected_choice_apt_menu = True
               # APT Main Menu Code
               while no_selected_choice_apt_menu:
                   unipak_print_commands.print_unipak_apt_commands()
                   try:
                      command = int(input("Enter your choice -> "))
                      match command:
                          case 1:
                              apt_funcs.update()
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 2:
                              apt_funcs.upgrade()
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 3:
                              apt_funcs.update_fix_missing()
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 4:
                              appname = input("Enter the app name you want to install -> ")
                              apt_funcs.install(appname)
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 5:
                              appname = input("Enter the app name you want to remove (uninstall) -> ")
                              apt_funcs.remove(appname)
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 6:
                              appname = input("Enter the app name you want to purge (uninstall with configs) -> ")
                              apt_funcs.purge(appname)
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 7:
                              apt_funcs.auto_remove()
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 8:
                              apt_funcs.clean()
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 9:
                              keyword = input("Enter a keyword to find apps with it -> ")
                              apt_funcs.search(keyword)
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 10:
                              appname = input("Enter the app name you want to show its details -> ")
                              apt_funcs.show(appname)
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 11:
                              apt_funcs.list_installed()
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 12:
                              apt_funcs.list_upgradable()
                              input("Press enter to return to the Main Menu...")
                              os.system("clear")
                          case 13:
                              no_selected_choice_apt_menu = False
                              os.system("clear")
                          case _:
                              print("Something went wrong")
                              input("Press enter to return to the Main Menu...")
                   except ValueError:
                       print("You can only type numbers")
                       input("Press enter to return to the Main Menu...")
        case 2:
            os.system("clear")
            no_selected_choice_flatpak_menu = True
            # Flatpak Main Menu Code
            while no_selected_choice_flatpak_menu:
                unipak_print_commands.print_unipak_flatpak_commands()
                try:
                   command = int(input("Enter your choice -> "))
                   match command:
                       case 1:
                           flatpak_funcs.update()
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 2:
                           appname = input("Enter the app name you want to install -> ")
                           flatpak_funcs.install(appname)
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 3:
                           appname = input("Enter the app name you want to uninstall -> ")
                           flatpak_funcs.uninstall(appname)
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 4:
                           term = input("Enter the term you want to search apps with it -> ")
                           flatpak_funcs.search(term)
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 5:
                           flatpak_funcs.list_()
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 6:
                           id = input("Enter the app id you want to show its info (details) -> ")
                           flatpak_funcs.info(id)
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 7:
                           flatpak_funcs.list_configured()
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 8:
                           flatpak_funcs.uninstall_unused()
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 9:
                           no_selected_choice_flatpak_menu = False
                           os.system("clear")
                       case _:
                           print("Something went wrong: The number is out of choices")
                           input("Press enter to return to the Main Menu...")
                except ValueError:
                    print("You can only type numbers")
        case 3:
            os.system("clear")
            no_selected_choice_snap_menu = True
            # Snap Main Menu Code
            while no_selected_choice_snap_menu:
                unipak_print_commands.print_unipak_snap_commands()
                try:
                   command = int(input("Enter your choice -> "))
                   match command:
                       case 1:
                           snap_funcs.refresh()
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 2:
                           appname = input("Enter the app name you want to install -> ")
                           snap_funcs.install(appname)
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 3:
                           appname = input("Enter the app name you want to remove (uninstall) -> ")
                           snap_funcs.remove(appname)
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 4:
                           term = input("Enter a term you want to search apps with it -> ")
                           snap_funcs.find(term)
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 5:
                           snap_funcs.list_()
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 6:
                           name = input("Enter the app name you want to show its details -> ")
                           snap_funcs.info(name)
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 7:
                           snap_funcs.refresh_list()
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 8:
                           no_selected_choice_snap_menu = False
                           os.system("clear")
                       case _:
                           print("Something went wrong: The number is out of choices")
                           input("Press enter to return to the Main Menu...")
                except ValueError:
                    print("You can only type numbers")
                    input("Press enter to return to the Main Menu...")
        case 4:
            os.system("clear")
            # Install Package Managers (Flatpak/Snap) Main Code
            no_selected_choice_pm_install_menu = True
            while no_selected_choice_pm_install_menu:
                print("1. Install Flatpak Package Manager")
                print("2. Install Snap Package Manager")
                print("3. Go back")
                try:
                   command = int(input("Enter your choice -> "))
                   match command:
                       case 1:
                           os.system("sudo apt update")
                           os.system("sudo apt install -y flatpak")
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 2:
                           os.system("sudo apt update")
                           os.system("sudo apt install -y snapd")
                           input("Press enter to return to the Main Menu...")
                           os.system("clear")
                       case 3:
                           no_selected_choice_pm_install_menu = False
                           os.system("clear")
                       case _:
                           print("Something went wrong: The number is out of choices")
                           input("Press enter to return to the Main Menu...")
                except ValueError:
                    print("You can only type numbers")
                    input("Press enter to return to the Main Menu...")
        case 5:
            os.system("clear")
            running = False
        case _:
            print("Something went wrong: The number is out of choices")
            input("Press enter to return to the Main Menu...")
