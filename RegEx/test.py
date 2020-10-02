import sys
import re

regexp = '.*?(?=.*\\bID=\"(\\d+)\")(?=.*\\bUserID=\"(\\d+)\").*'

for line in sys.stdin:
   if not re.match(regexp, line.strip()):
       print line.strip()