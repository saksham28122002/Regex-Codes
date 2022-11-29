# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

ipv4_regex = re.compile("^((25[0-5]|2[0-4]\d|1\d\d|\d\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|\d\d|\d)$")
ipv6_regex = re.compile("^(?:[a-f0-9]{1,4}:){7}[a-f0-9]{1,4}$")

for _ in range(int(input())):
    output = "Neither"
    text = input()
    if ipv4_regex.match(text):
        output = "IPv4"
    elif ipv6_regex.match(text):
        output = "IPv6"

    print(output)
