import sys
import os
import subprocess

# --- Commands ---
def setup():
    print("hello world")

def start():
    print("Neuron starting...")

def nset():
    """Add the neuron folder to the system PATH so all commands work globally."""
    neuron_folder = os.path.dirname(os.path.abspath(__file__))
    try:
        # Get current PATH
        result = subprocess.run('echo %PATH%', shell=True, capture_output=True, text=True)
        current_path = result.stdout.strip()

        if neuron_folder.lower() in current_path.lower():
            print("Neuron folder is already in PATH.")
            return

        # Add neuron folder to PATH
        subprocess.run(f'setx PATH "{current_path};{neuron_folder}"', shell=True, check=True)
        print(f"Neuron folder added to PATH:\n{neuron_folder}")
        print("Restart CMD for changes to take effect.")
    except subprocess.CalledProcessError:
        print("Failed to add Neuron folder to PATH.")

# Map commands
commands = {
    "setup": setup,
    "start": start,
    "--NSET": nset
}

# --- CMD interface ---
if len(sys.argv) < 2:
    print("Available commands:", list(commands.keys()))
    sys.exit(1)

cmd_name = sys.argv[1]
args = sys.argv[2:]

if cmd_name in commands:
    commands[cmd_name](*args)
else:
    print(f"Unknown command: {cmd_name}")
