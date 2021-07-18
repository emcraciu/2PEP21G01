import re

my_data = "My text to search text"

match = re.search(r'text', my_data)  # match string

print(type(match))
print(match.group(0))

match = re.search(r'(?P<name>text)', my_data)  # match named captured group

print(type(match))
print(match.group('name'))

match = re.findall(r'\w+', my_data)  # mach any word and returns list of matches
print(match)
