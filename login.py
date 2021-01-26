#!/usr/bin/env python3
import os
import sys
from templates import login_page, _wrapper

print("Content-Type: text/html")
print()

build = login_page()

length = os.environ["CONTENT_LENGTH"]

if length.strip() != "":
    data = ""
    for char in sys.stdin.read(int(length)):
        data += char

    params = data.split("&")
    for param in params:
        k, v = param.split("=")
        build += f"{k}: {v}\n"

print(_wrapper(build))

