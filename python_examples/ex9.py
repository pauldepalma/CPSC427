'''
Demonstrates:
    regular expressions
To use:
1. bring up python shell
2. from ex9 import find
3. find('ll','hello')
'''    
import re
def find(pattern,inString):
    m = re.search(pattern,inString)
    if m:
        print m.group()
    
    
