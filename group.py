"""
Difference between group and groups
"""
import re
pattern = re.compile(r"(\w+) (\w+)")
match = pattern.search("Hello world")
print match.group()
print match.groups()

pattern = re.compile(r"(\w+) (\w+) (\w+)*")
match = pattern.search("Hello yes ")
print match.groups("world")

"""
Group dictionary
"""
pattern=re.compile(r"(?P<first>\w+) (?P<second>\w+)")
print pattern.search("Hello word").groupdict()

"""
start operation
"""
pattern=re.compile(r"(?P<first>\w+) (?P<second>\w+)?")
match= pattern.search("Hello word")
print match.start(2)

"""
end operation
"""
pattern=re.compile(r"(?P<first>\w+) (?P<second>\w+)?")
match= pattern.search("Hello word")
print match.end(2)

"""
span operation
"""
pattern=re.compile(r"(?P<first>\w+) (?P<second>\w+)?")
match= pattern.search("Hello word")
print match.span(2)