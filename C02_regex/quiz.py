import re

"""What is the output of the following code"""

# objectobjectre.match()
# re.search()
# re.fullmatch()
# re.findall()

text = 'Sample'
pattern = '(?P<text>.*)'
print(re.search(pattern, text).group(0))