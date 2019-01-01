
import re
#print re.search(r'<HTML>', "in <HTML> in t")
pattern=re.compile(r'<html>$')
print pattern.match("<html>")