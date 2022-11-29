# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys

regex = re.compile(r"(//.*?$|/\*+.*?\*+/)", re.M|re.DOTALL)

for i in regex.findall(sys.stdin.read()):
    print(re.sub(r"\n\s+", "\n",i.strip()))
