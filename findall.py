"""
function used to search more than one occurrence of the pattern
"""
import re

pattern=re.compile(r'\w+')
print (pattern.findall("hello word"))




