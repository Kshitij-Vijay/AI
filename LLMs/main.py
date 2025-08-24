import os
import sys
import subprocess

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def list_python_files():
    py_scripts = []
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith('.py') and file == "main.py":
                # Store relative path to Python script
                py_scripts.append(os.path.relpath(os.path.join(root, file), ROOT_DIR))
    return py_scripts

def main():
    py_scripts = list_python_files()
    if not py_scripts:
        print("No Python scripts found.")
        return

    print("Available Python programs:")
    for idx, script in enumerate(py_scripts, 1):
        print(f"{idx}. {script}")

    try:
        choice = int(input(f"Select a program to run [1-{len(py_scripts)}]: "))
        if not (1 <= choice <= len(py_scripts)):
            print("Invalid choice.")
            return
        script_path = py_scripts[choice - 1]
        print(f"Running {script_path}...")
        subprocess.run([sys.executable, script_path])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
