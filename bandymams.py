import re

asm_kod = "37104180328"

p = re.compile(r"^[1-6][0-9]{2}[0-1][0-9][0-3][0-9][0-9]{4}$")

a = p.match(asm_kod)

print(a)
