import os
import platform
import json
import uuid
import hashlib
from pathlib import Path
from datetime import datetime
import shutil
import subprocess


def explain_step(step: str) -> None:
    """Prints a clear explanation for each step."""
    print("\n" + "=" * 50)
    print(f"Step: {step}")
    print("=" * 50)


def get_storage_path() -> Path:
    """Determine the configuration file path based on the OS."""
    explain_step("Locating the configuration file (storage.json)")
    system = platform.system()
    if system == "Windows":
        base_path = os.getenv("APPDATA")
    elif system == "Darwin":  # macOS
        base_path = str(Path.home() / "Library/Application Support")
    elif system == "Linux":
        base_path = str(Path.home() / ".config")
    else:
        raise RuntimeError(f"Unsupported OS: {system}")
    
    storage_path = Path(base_path) / "Cursor/User/globalStorage/storage.json"
    print(f"Determined configuration file path: {storage_path}")
    if not storage_path.exists():
        raise FileNotFoundError(f"Configuration file not found at: {storage_path}")
    return storage_path


def backup_file(file_path: Path) -> Path:
    """Create a backup of the configuration file."""
    explain_step("Backing up the configuration file")
    backup_path = file_path.parent / f"{file_path.name}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    print(f"Backup successfully created at: {backup_path}")
    return backup_path


def generate_new_uuids() -> dict:
    """Generate new unique identifiers."""
    return {
        "telemetry.machineId": hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest(),
        "telemetry.macMachineId": hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest(),
        "telemetry.devDeviceId": str(uuid.uuid4()),
        "telemetry.sqmId": f"{{{uuid.uuid4()}}}"
    }


def modify_configuration(storage_path: Path):
    """Update the configuration file with new unique identifiers."""
    explain_step("Modifying the configuration file")
    with open(storage_path, 'r', encoding='utf-8') as file:
        config = json.load(file)

    new_ids = generate_new_uuids()
    for key, value in new_ids.items():
        if key in config:
            config[key] = value

    with open(storage_path, 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=2)
    print("Configuration updated successfully!")
    print(f"New IDs: {new_ids}")


def automatic_installation():
    """Try automatic installation with a script."""
    explain_step("Attempting automatic installation")
    try:
        system = platform.system()
        if system in ["Linux", "Darwin"]:  # Linux/macOS
            command = (
                "curl -fsSL https://raw.githubusercontent.com/yuaotian/go-cursor-help/master/scripts/install.sh | sudo bash"
            )
        elif system == "Windows":  # Windows
            command = (
                "irm https://raw.githubusercontent.com/yuaotian/go-cursor-help/master/scripts/install.ps1 | iex"
            )
        else:
            raise RuntimeError(f"Unsupported OS for automatic installation: {system}")

        print(f"Executing command: {command}")
        subprocess.run(command, shell=True, check=True)
        print("Automatic installation completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Automatic installation failed: {e}")


def manual_steps_guide():
    """Guide the user through manual configuration steps."""
    explain_step("Manual installation and configuration steps")
    print("If automatic installation fails, follow these manual steps:")
    print("1. Locate the configuration file:")
    print("   - Windows: %APPDATA%\\Cursor\\User\\globalStorage\\storage.json")
    print("   - macOS: ~/Library/Application Support/Cursor/User/globalStorage/storage.json")
    print("   - Linux: ~/.config/Cursor/User/globalStorage/storage.json")
    print("2. Create a backup of the storage.json file (e.g., copy it to storage.json.backup).")
    print("3. Open the file in a text editor and replace the following fields with new UUIDs:")
    print('   {')
    print('       "telemetry.machineId": "generate-new-uuid",')
    print('       "telemetry.macMachineId": "generate-new-uuid",')
    print('       "telemetry.devDeviceId": "generate-new-uuid",')
    print('       "telemetry.sqmId": "generate-new-uuid"')
    print('   }')
    print("4. Save the file and restart the Cursor application.")
    print("Note: You can use online UUID generators if needed.")


def main():
    try:
        explain_step("Starting the Cursor configuration reset tool")
        print("This tool will help you reset Cursor IDs.")
        print("Step 1: Attempting automatic installation...")
        automatic_installation()
        print("\nIf the automatic installation didn't work, you can try manual steps.")
        user_choice = input("Do you want to proceed with manual steps? (yes/no): ").strip().lower()
        if user_choice == "yes":
            storage_path = get_storage_path()
            backup_file(storage_path)
            modify_configuration(storage_path)
        else:
            print("Exiting the tool. No further actions performed.")
    except Exception as e:
        print(f"Error: {e}")
        print("\nSwitching to manual guide...")
        manual_steps_guide()


if __name__ == "__main__":
    main()
