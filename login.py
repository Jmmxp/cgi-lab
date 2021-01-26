#!/usr/bin/env python3
import os
import sys
from templates import login_page, _wrapper
from secret import username, password

print("Content-Type: text/html")
print()

build = login_page()

length = os.environ["CONTENT_LENGTH"]

if length.strip() != "":
    data = ""
    for char in sys.stdin.read(int(length)):
        data += char

    params = data.split("&")
    param_dict = dict()
    for param in params:
        k, v = param.split("=")
        build += f"{k}: {v}\n"
        param_dict[k] = v

    sent_username = param_dict["username"]
    sent_password = param_dict["password"]
    if sent_username == username and sent_password == password:
        build += "USER AND PASS WERE CORRECT!"

print(_wrapper(build))

