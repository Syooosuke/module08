import sys
import os
import site

def is_virtual_env() -> bool:
    if sys.prefix != getattr(sys, "base_prefix", sys.prefix):
        return True
    
    if os.environ.get("VIRTUAL_ENV"):
        return True
    
    return False

def print_outside_matrix() -> None:
    print("MARTRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("THe machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate #On Unix")
    print("matrix_env\\Script\\activate # On Windows")
    print("Then run this program again.\n")

def print_inside_construct() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")

    venv_path: str = os.environ.get("VIRTUAL_ENV", sys.prefix)
    venv_name: str = os.path.basename(venv_path)

    print(f"Virtual Environment: {venv_name}")
    print(f"Environmet Path: {venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")

    site_packages = site.getsitepackages()
    if site_packages:
        print(site_packages[0])
    else:
        print("Could not determine package installation path.")

def main() -> None:
    if is_virtual_env():
        print_inside_construct()
    else:
        print_outside_matrix()

if __name__ == "__main__":
    main()
