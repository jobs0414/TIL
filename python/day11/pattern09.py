import re

source = "Patterns are very important for validating check."

# pattern1 = re.compile('very')
pattern1 = re.compile('Patterns')

match = pattern1.match(source)
search = pattern1.search(source)

if match:
    print("match:", match.group())

if search:
    print("search:", search.group())
