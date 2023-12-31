import sys
import os
import subprocess

if sys.version_info < (3, 10):
    sys.stdout.write("installer requires Python 3.6 or newer to run!\n")
    sys.exit(1)


SHELL = os.getenv("SHELL", "")
MACOS = sys.platform == "darwin"

# @TODO: Handle other OS
if not MACOS:
    print("Warning: Currently non-MAC OSes are not 100% supported.")

# @TODO: Handle other shell
if "zsh" in SHELL:
    subprocess.call(["zsh", "./src/scripts/setup.zsh"])
elif "bash" in SHELL:
    subprocess.call(["sh", "./src/scripts/setup.sh"])
else:
    print(f"{SHELL} is not supported yet.")
