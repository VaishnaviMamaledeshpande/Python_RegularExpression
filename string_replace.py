"""
function to replace part of the string
"""

import re
pattern=re.compile(r'[\-A-Z]')
print pattern.sub('A', "-1234 B193 B123")


pattern=re.compile(r'\*([A-Z]*)\*')
print pattern.sub(r'\g<1>', "this is beautiful *1123* *ABCD* *HGRT* here")

pattern=re.compile(r'\*([A-Z]*)\*')
print pattern.subn(r'\g<1>', "this is beautiful *1123* *ABCD* *HGRT* here",1)

"""
similar function to sub , slightly change in functionality
It does not return the complete string but  returns the replaced part of the string 
"""
text="this is beautiful *1123* *ABCD* *HGRT* here"
match = re.search(r'\*(.*?)\*', text)
print match.expand(r"<b>\g<1><\\b>")

pattern=re.compile(r'\*(.*?)\*')
match= pattern.search(text)
print match.group()
print match.expand(r"<b>\g<1><\\b>")
print text

