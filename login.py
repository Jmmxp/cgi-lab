#!/usr/bin/env python3
import os
from templates import login_page, _wrapper

print("Content-Type: text/html")
print()

build = login_page() + f"<p>QUERY_STRING: {os.environ['QUERY_STRING']}</p>"
build += f"<p>{os.environ}</p>"

print(_wrapper(build))

