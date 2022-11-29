# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
text = "\n".join(input() for _ in range(n))

for _ in range(int(input())):
    regex = re.compile(rf"(?<![\w]){input()}(?![\w])")    
    print(len(regex.findall(text)))
