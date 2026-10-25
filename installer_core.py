import json
import os
import shutil

def load_lpi_package(package_path):
    """
    Step 1: Read the company's metadata.json inside the .lpi folder
    """
    metadata_file = os.path.join(package_path, "metadata.json")
    
    if not os.path.exists(metadata_file):
        print("[Error] This is not a valid .LPI package. metadata.json is missing.")
        return None

    with open(metadata_file, 'r') as file:
        data = json.load(file)
        return data

def install_application(package_path, app_name, enabled_permissions):
    """
    Step 2: Automate the file installation and apply permissions
    """
    print(f"\n[LPB Engine] Starting installation for: {app_name}")
    
    # Simulate moving the files to the secure Linux system directory
    target_directory = f"/opt/{app_name.lower().replace(' ', '_')}"
    print(f"[LPB Engine] Copying application files to {target_directory}...")
    
    # Apply the permissions selected by the user in the switches
    print("[LPB Engine] Configuring pre-approved permissions:")
    for permission in enabled_permissions:
        print(f" -> Setting up {permission} access in the system configuration... [OK]")
        
    print(f"\n[LPB Engine] Success! {app_name} is fully installed and ready to use.")

# --- SIMULATION OF THE PROCESS ---
# This simulates what happens when the box reads the template folder
if __name__ == "__main__":
    template_folder = "Template.lpi"
    
    # The box reads the metadata
    app_data = load_lpi_package(template_folder)
    
    if app_data:
        print("=========================================")
        print(f" LPB READ SUCCESSFUL: {app_data['app_name']}")
        print(f" Developer: {app_data['developer']}")
        print("=========================================")
        
        # Simulate that the user accepted the terms and enabled both permissions in the UI switches
        user_switches = ["accessibility", "notifications"]
        
        # The engine completes the installation automatically
        install_application(template_folder, app_data['app_name'], user_switches)
