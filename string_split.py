"""
splitting the string
maxsplit - no of splits to be done
"""
import re
pattern=re.compile(r"\W")
print pattern.split("hello word")

pattern = re.compile(r"\W")
print pattern.split("hello world is basic program",2)

"""
 capture split element
"""
pattern = re.compile(r"(\W)")
print pattern.split("hello world is basic program",2)

"""
if the string starts with split element then there will be extra empty string at the beginning
"""
pattern = re.compile(r"(\W)")
print pattern.split(" hello world is basic program",2)