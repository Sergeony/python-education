import re

# Your code goes here
find_members = []

for func in dir(re):
    if "find" in func:
        find_members.append(func)

print(sorted(find_members))
