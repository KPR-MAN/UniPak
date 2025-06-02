import subprocess
import os
import sys
import shutil

# --- Configuration ---
APP_NAME = "UniPak"
MAIN_SCRIPT = "main.py"
APP_ICON = "uni_pak_icon.png"
APP_COMMENT = "A Universal Package Manager For APT Based Linuxs."
APP_CATEGORIES = "Utility;"

# Python Other Files
OTHER_PYTHON_FILES_AS_DATA = [
    "apt_funcs.py",
    "flatpak_funcs.py",
    "snap_funcs.py",
    "unipak_print_commands.py",
]

# --- Installation Paths ---
INSTALL_DIR = os.path.expanduser(f"~/Applications/{APP_NAME}")
# The directory for desktop entry files
DESKTOP_ENTRY_DIR = os.path.expanduser("~/.local/share/applications/")

# --- Helper function to get resource path for bundled files (if used with --add-data) ---
def get_resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller.
    Use this in your main.py if you access files added with --add-data.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Fallback for development mode (not packaged)
        base_path = os.path.abspath(os.path.dirname(__file__))

    return os.path.join(base_path, relative_path)

# --- Main Installer Logic ---
def run_installer():
    print(f"--- Starting Installer for {APP_NAME} ---")

    # 1. Check for PyInstaller
    try:
        subprocess.run(["pyinstaller", "--version"], check=True, capture_output=True)
        print("PyInstaller is installed.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("PyInstaller is not found. Please install it: pip install pyinstaller")
        sys.exit(1)

    # 2. Clean up previous build/dist directories
    print("Cleaning up previous build artifacts...")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    print("Cleanup complete.")

    # 3. Construct PyInstaller command
    pyinstaller_command = [
        "pyinstaller",
        "--onefile",  # Create a single executable file
        f"--name={APP_NAME}", # Set the name of the executable
    ]

    for py_file in OTHER_PYTHON_FILES_AS_DATA:
        if os.path.exists(py_file):
            # The destination folder is '.' meaning the root of the bundled app's temp dir
            pyinstaller_command.append(f"--add-data={py_file}:.")
            print(f"Adding {py_file} as data file.")
        else:
            print(f"Warning: {py_file} not found. Skipping --add-data for it.")

    # Add the main script
    pyinstaller_command.append(MAIN_SCRIPT)

    print(f"\nRunning PyInstaller command: {' '.join(pyinstaller_command)}")
    try:
        subprocess.run(pyinstaller_command, check=True, text=True, capture_output=True)
        print("\nPyInstaller build successful!")
        print("PyInstaller Output:")
    except subprocess.CalledProcessError as e:
        print(f"\nError during PyInstaller build:\n{e.stdout}\n{e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred during PyInstaller build: {e}")
        sys.exit(1)

    # 4. Locate the built executable
    executable_path_in_dist = os.path.join("dist", APP_NAME)
    if not os.path.exists(executable_path_in_dist):
        print(f"Error: Executable not found at {executable_path_in_dist}")
        sys.exit(1)
    print(f"Found executable: {executable_path_in_dist}")

    # 5. Create installation directory
    print(f"Creating installation directory: {INSTALL_DIR}")
    os.makedirs(INSTALL_DIR, exist_ok=True)

    # 6. Copy executable to installation directory
    final_executable_path = os.path.join(INSTALL_DIR, APP_NAME)
    print(f"Copying executable to {final_executable_path}")
    shutil.copy(executable_path_in_dist, final_executable_path)
    os.chmod(final_executable_path, 0o755) # Make it executable
    print("Executable copied and made executable.")

    # 7. Copy icon to installation directory
    if os.path.exists(APP_ICON):
        final_icon_path = os.path.join(INSTALL_DIR, APP_ICON)
        print(f"Copying icon to {final_icon_path}")
        shutil.copy(APP_ICON, final_icon_path)
        print("Icon copied.")
    else:
        print(f"Warning: Icon file '{APP_ICON}' not found. Desktop entry will not have an icon.")
        final_icon_path = "" # Set to empty if icon not found

    # 8. Create .desktop file
    desktop_file_content = f"""\
[Desktop Entry]
Name={APP_NAME}
Comment={APP_COMMENT}
Exec={final_executable_path}
Icon={final_icon_path}
Terminal=true
Type=Application
Categories={APP_CATEGORIES}
StartupNotify=true
"""
    desktop_file_name = f"{APP_NAME.lower().replace(' ', '-')}.desktop"
    desktop_file_path = os.path.join(DESKTOP_ENTRY_DIR, desktop_file_name)

    print(f"Creating desktop entry file: {desktop_file_path}")
    os.makedirs(DESKTOP_ENTRY_DIR, exist_ok=True)
    with open(desktop_file_path, "w") as f:
        f.write(desktop_file_content)
    os.chmod(desktop_file_path, 0o644) # Standard permissions for .desktop files
    print("Desktop entry file created.")

    # 9. Update desktop database
    print("Updating desktop database...")
    try:
        subprocess.run(["update-desktop-database", DESKTOP_ENTRY_DIR], check=True, text=True, capture_output=True)
        print("Desktop database updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating desktop database:\n{e.stdout}\n{e.stderr}")
        print("You might need to run 'update-desktop-database' manually or log out/in.")
    except FileNotFoundError:
        print("Warning: 'update-desktop-database' command not found. Your app might not appear immediately.")

    print(f"\n--- Installation of {APP_NAME} complete! ---")
    print(f"You should now find '{APP_NAME}' in your application menu.")
    print("If it doesn't appear, try logging out and logging back in, or restarting your desktop environment.")

if __name__ == "__main__":
    run_installer()
