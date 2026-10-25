import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os

class LinuxPackagerBox:
    def __init__(self, root):
        self.root = root
        self.root.title("Linux Packager Box (.LPB)")
        self.root.geometry("550x450")
        self.root.configure(bg="#f5f5f7") # Clean, macOS-like light background
        
        # Load the company template data
        self.app_name = "Universal App"
        self.developer = "Unknown Developer"
        self.permissions_list = []
        self.load_package_info()
        
        # Track user choices
        self.permission_vars = {}
        
        # Build the initial interface
        self.create_preview_screen()

    def load_package_info(self):
        """Reads the universal template metadata to dynamic fill the UI"""
        template_json = os.path.join("Template.lpi", "metadata.json")
        if os.path.exists(template_json):
            with open(template_json, "r") as file:
                data = json.load(file)
                self.app_name = data.get("app_name", "Universal App")
                self.developer = data.get("developer", "Unknown Developer")
                self.permissions_list = data.get("required_permissions", [])

    def create_preview_screen(self):
        """Phase 1 & 2: Show app info and the interactive installation box"""
        # Header / Brand
        header = tk.Label(self.root, text="📦 .LPB Installer Engine", font=("Helvetica", 12, "bold"), bg="#f5f5f7", fg="#8e8e93")
        header.pack(pady=10)
        
        # App Info Card
        self.card_frame = tk.Frame(self.root, bg="white", highlightbackground="#d1d1d6", highlightthickness=1, bd=0)
        self.card_frame.pack(pady=20, padx=40, fill="both", expand=True)
        
        title_label = tk.Label(self.card_frame, text=self.app_name, font=("Helvetica", 18, "bold"), bg="white", fg="#1d1d1f")
        title_label.pack(pady=(20, 2))
        
        dev_label = tk.Label(self.card_frame, text=f"by {self.developer}", font=("Helvetica", 11, "italic"), bg="white", fg="#8e8e93")
        dev_label.pack(pady=(0, 20))
        
        # The Action Button to "Open the Box"
        self.open_box_btn = tk.Button(
            self.card_frame, 
            text="Open Box to Install", 
            font=("Helvetica", 12, "bold"),
            bg="#0071e3", 
            fg="white", 
            highlightbackground="white",
            padx=20, 
            pady=8, 
            command=self.show_permissions_screen
        )
        self.open_box_btn.pack(pady=20)

    def show_permissions_screen(self):
        """Phase 3: The dynamic box opens to show the smart permissions switches!"""
        # Clear the old button
        self.open_box_btn.pack_forget()
        
        # Instructions Label
        instructions = tk.Label(self.card_frame, text="Configure Pre-Approved Permissions:", font=("Helvetica", 11, "bold"), bg="white", fg="#1d1d1f")
        instructions.pack(pady=10)
        
        # Dynamically build switches (checkboxes mapped neatly) for each permission in the metadata
        for perm in self.permissions_list:
            perm_frame = tk.Frame(self.card_frame, bg="white")
            perm_frame.pack(fill="x", padx=30, pady=5)
            
            # Variable to track if switch is ON or OFF
            var = tk.BooleanVar(value=True)
            self.permission_vars[perm["id"]] = var
            
            # Visual check/switch
            chk = tk.Checkbutton(perm_frame, text=perm["name"], variable=var, font=("Helvetica", 11, "bold"), bg="white", activebackground="white", fg="#0071e3")
            chk.pack(anchor="w")
            
            # Permission description text below it
            desc = tk.Label(perm_frame, text=perm["description"], font=("Helvetica", 9), bg="white", fg="#8e8e93", wraplength=350, justify="left")
            desc.pack(anchor="w", padx=25)
            
        # Final Step Button: Install Now
        install_btn = tk.Button(
            self.card_frame,
            text="Install Now",
            font=("Helvetica", 12, "bold"),
            bg="#34c759",
            fg="white",
            highlightbackground="white",
            padx=20,
            pady=8,
            command=self.execute_mock_installation
        )
        install_btn.pack(pady=20)

    def execute_mock_installation(self):
        """Phase 4: Simulates authentication and finishes smoothly"""
        approved = [pid for pid, var in self.permission_vars.items() if var.get()]
        
        # Trigger standard pop-up simulation
        messagebox.showinfo(
            "System Authentication", 
            f"[LPB Security Check]\n\nProcessing system injection with pre-approved permissions:\n{approved}\n\nApplication successfully registered into Linux!"
        )
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LinuxPackagerBox(root)
    root.mainloop()
