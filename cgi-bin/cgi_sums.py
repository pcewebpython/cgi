#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()

form = cgi.FieldStorage()
inputs = form.getlist('operand')

print("The sum is : {}".format(sum(int(i) for i in inputs)))
