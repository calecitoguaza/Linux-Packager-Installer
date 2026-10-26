# 📦 LPI: Linux Packager Installer & Box (.LPB)

A modern, elegant, and secure application packaging ecosystem for Linux, inspired by the intuitive user experience of macOS. 

---

## 💡 The Idea
Linux users are often tired of typing complex terminal commands, managing missing dependencies, or entering root passwords blindly just to install a single application. 

**LPI (Linux Packager Installer)** changes everything. It introduces a global template for developers and a beautiful, interactive GUI called **LPB (Linux Packager Box)** that handles installation visually. No terminal, no headache.

---

## ✨ Features

* **Universal Plantilla (`.lpi`):** A clean container format where companies (like Google, Spotify, or indie devs) can bundle their binaries, custom terms, and metadata.
* **The "Open Box" Concept:** Users interact with a virtual box that unfolds smoothly to guide them through the process.
* **Smart Pre-Approved Perms:** Users can toggle system permissions (like Accessibility Features or System Notifications) via clean toggles **before** the app finishes downloading and executing.
* **One-Click Security:** Authenticate with a single admin password prompt and let the background engine do the heavy lifting.

---

## 📂 Project Structure

* `Template.lpi/` - The universal folder mold for developers.
  * `bin/` - Place the compiled application binaries here.
  * `metadata.json` - Manifest defining app info and requested security permissions.
  * `terms.txt` - Customizable EULA/Terms and conditions in plain text.
  * `icon.png` - High-resolution app icon displayed during setup.
* `installer_core.py` - The silent background engine that manages injections and file movement.
* `lpb_interface.py` - The native graphical user interface (Tkinter) that brings the box to life.

---

## 🚀 How to Run the Interactive Prototype

Since the prototype is written in universal Python, you can test the entire visual flow directly on your Mac or Linux machine.

1. Clone or download this repository.
2. Open your Terminal and navigate to the project directory.
3. Run the interface launcher:
   ```bash
   python3 lpb_interface.py
   ```

---

## 🗺️ Roadmap / Future Steps
- [ ] Implement actual `.tar.gz` dynamic extraction for `.lpi` files.
- [ ] Connect the permission toggles directly to Linux security backends (D-Bus / AppArmor).
- [ ] Style the Tkinter GUI to match native Linux desktop themes (Cinnamon, GNOME, KDE).

---
*Created with passion to make Linux more accessible and beautiful for everyone.* 🚀
