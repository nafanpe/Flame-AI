import os
import sys
import shutil
import win32com.client  # Requires `pywin32`

def add_to_startup():
    startup_folder = os.path.join(os.getenv("APPDATA"), r"Microsoft\Windows\Start Menu\Programs\Startup")
    shortcut_path = os.path.join(startup_folder, "FlameAI.lnk")

    if os.path.exists(shortcut_path):
        return  # Already exists, don't duplicate

    python_exe = sys.executable.replace("python.exe", "pythonw.exe")
    script_path = os.path.abspath(__file__)

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = python_exe
    shortcut.Arguments = f'"{script_path}"'
    shortcut.WorkingDirectory = os.path.dirname(script_path)
    shortcut.IconLocation = python_exe
    shortcut.save()

add_to_startup()