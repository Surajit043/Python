from __future__ import print_function
import re

css = ""
for i in range(int(input())):
    css+=input()
    css+='\n'

inside_brackets = re.findall(r'\{.*?\}', css, flags=re.DOTALL)
for property in inside_brackets:
    map(lambda i: print(i,sep='\n',end='\n'),(re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', property)))
