#!/usr/bin/env python3
import os
import sys
from templates import login_page, secret_page, _wrapper
from secret import username, password

print("Content-Type: text/html")

build = ""
cookies_dict = dict()
cookies = os.environ["HTTP_COOKIE"].split("; ")
for cookie in cookies:
    if cookie.strip() == "":
        continue
    k, v = cookie.split("=")
    cookies_dict[k.strip()] = v.strip()

if "logged_in" in cookies_dict:
    u, p = cookies_dict["logged_in"].split(":")
    build = secret_page(u, p)
else:
    build = login_page()

    length = os.environ["CONTENT_LENGTH"]

    if length.strip() != "":
        data = ""
        # Referred to Python3 docs for reading: https://docs.python.org/3/tutorial/inputoutput.html
        # I found out that POST data is retrieved from stdin from StackOverflow user slezica: https://stackoverflow.com/u/469300 
        # link: https://stackoverflow.com/a/5451943
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
            build += "USER AND PASS WERE CORRECT! Cookie was set."
            # Referred to Mozilla docs for Set-Cookie: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
            print(f"Set-Cookie: logged_in={username}:{password}")

print(f"\n{_wrapper(build)}")

