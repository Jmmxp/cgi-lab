#!/usr/bin/env python3
import os
import json

print("Content-Type: text/html")
print()
print("""
<!DOCTYPE html>
<html>
<body>
""")

print(f"<p>QUERY_STRING: {os.environ['QUERY_STRING']}</p>")
for parameter in os.environ["QUERY_STRING"].split("&"):
    (name, value) = parameter.split("=")
    print(f"<li><em>{name} = {value} </em></li>")

print("""
<ul>
</ul>
</body>
</html>
""")