#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')

try:
    total = sum(map(int, operands))
    body = "Your total is {}".format(total)
except (ValueError, TypeError):
    body = "Cannot compute, provide integers"

print("Content-type: text/plain")
print()
print(body)
