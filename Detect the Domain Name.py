# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

regex = re.compile(r"https?://(?:ww(?:w|2)\.)?((?:[\w-]+\.)+[a-z]+)")

output = set()
for _ in range(int(input())):
    output.update(regex.findall(input()))
    
print(*sorted(output),sep=";")
