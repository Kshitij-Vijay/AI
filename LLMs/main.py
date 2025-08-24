import os
import sys
import subprocess
import time

def run_shell_command(cmd):
    print(f"Running: {cmd}")
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Command failed: {cmd}\nError: {stderr.decode()}")
        exit(1)
    print(stdout.decode())

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


    # Step 0: Pull models
    run_shell_command("ollama pull nomic-embed-text:latest")
    run_shell_command("ollama pull llama2:latest")

    # Step 1: Start Ollama server in a background process
    # IMPORTANT: This will block if run synchronously, so run it in background
    server_process = subprocess.Popen("ollama serve", shell=True)

    # Optional: wait a few seconds to let server start
    time.sleep(5)


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
