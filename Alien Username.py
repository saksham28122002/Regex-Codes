# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
n=int(input())
for j in range(n):
    i=input()
    pattern='^[_.][0-9]+[a-zA-Z]*[_]$|^[_.][0-9]+[a-zA-Z]*$'
    match=re.findall(pattern,i)
    if match:
        print('VALID')
    else:
        print('INVALID')
