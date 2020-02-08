""" cgi_sums.py """
#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

FORM = cgi.FieldStorage()
OPERANDS = FORM.getlist('operand')

try:
    TOTAL = sum(map(int, OPERANDS))
    BODY = "Your total is {}".format(TOTAL)
except (ValueError, TypeError):
    BODY = "unable to calculate a sum: pplease provide integer operands"

print("Content-type: text/plain") # content type line
print() # blank line
print(BODY) # the body
