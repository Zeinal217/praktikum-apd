import os
from colorama import Fore, Style

akun = {
    1: {"username": "admin", "password": "admin", "role": "admin"},
    2: {"username": "user", "password": "user", "role": "user"},
}

data_laundry = {}
role = None

def clear():
    os.system("cls || clear")
