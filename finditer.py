"""
finditer helps to iterate through match groups
"""
import re
pattern=re.compile(r'(\w+) (\w+)')
it= pattern.finditer("hello word hello dear")
print (it)
match = next(it)
print (match.groups())

print(match.span())
match = next(it)
print (match.groups())
print (match.span())

