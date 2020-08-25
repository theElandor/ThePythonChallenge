##fast way using re module

import re
data = open('prova.txt').read()
sol = re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", data)
print("".join(sol))