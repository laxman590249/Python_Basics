from pymem import Pymem
import subprocess
import os

try:
    mem = Pymem("Notepad.exe")
except:
    subprocess.Popen("Notepad.exe")
    mem = Pymem("Notepad.exe")

mem.inject_python_interpreter()

code= """
Hello Worled
"""
mem.inject_python_shellcode(code)
print()
