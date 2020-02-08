""" field_storage.py script """

import cgi
#!/usr/bin/env python

print("Content-Type: text/plain")
print("")

FORM = cgi.FieldStorage() # retrieve querry values

STRINGVAL = FORM.getvalue('a', None) # returns a default
LISTVAL = FORM.getlist('b') # returns list - here an empty list

print("a: {}, b: {}".format(str(STRINGVAL), str(LISTVAL)))
