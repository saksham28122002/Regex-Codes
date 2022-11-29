# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

regex = re.compile(r"\b(?:\w+\.)*\w+@(?:\w+\.)+\w+")

output = set()
for _ in range(int(input())):
    output.update(regex.findall(input()))

print(*sorted(output),sep=";")
