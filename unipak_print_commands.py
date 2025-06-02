# Menu Interface Print Method

# Consolidated command data
ALL_COMMANDS = {
    "APT": {
        "1": "Refresh package lists.",
        "2": "Upgrade installed packages.",
        "3": "Upgrade, remove old dependencies.",
        "4": "Install a package.",
        "5": "Remove package (keep configs).",
        "6": "Remove package and configs.",
        "7": "Remove unused dependencies.",
        "8": "Clear local package cache.",
        "9": "Find packages.",
        "10": "View package details.",
        "11": "List installed packages.",
        "12": "List upgradable packages.",
        "13": "Go back",
    },
    "Flatpak": {
        "1": "Update all Flatpak apps.",
        "2": "Install an app.",
        "3": "Uninstall an app.",
        "4": "Find Flatpak apps.",
        "5": "List installed Flatpak apps.",
        "6": "View app details.",
        "7": "List configured app sources.",
        "8": "Remove unused components.",
        "9": "Go back",
    },
    "Snap": {
        "1": "Update all Snap apps.",
        "2": "Install an app.",
        "3": "Uninstall an app.",
        "4": "Find Snap apps.",
        "5": "List installed Snap apps.",
        "6": "View app details.",
        "7": "List upgradable Snap apps.",
        "8": "Go back",
    }
}

def _print_commands_table(title: str, commands_dict: dict):
    """
    Helper function to print commands in a formatted table.
    This function handles the visual formatting of the command list.
    """
    print(f"\n--- {title} ---")
    print(f"{'Number':<10} {'Description':<40}")
    print(f"{'-'*10:<10} {'-'*40:<40}")
    for command_alias, desc in commands_dict.items():
        print(f"{command_alias:<10} {desc:<40}")

def print_unipak_apt_commands():
    """
    Prints only the APT-related UniPak commands.
    """
    _print_commands_table("APT Commands", ALL_COMMANDS["APT"])

def print_unipak_flatpak_commands():
    """
    Prints only the Flatpak-related UniPak commands.
    """
    _print_commands_table("Flatpak Commands", ALL_COMMANDS["Flatpak"])

def print_unipak_snap_commands():
    """
    Prints only the Snap-related UniPak commands.
    """
    _print_commands_table("Snap Commands", ALL_COMMANDS["Snap"])
