import re

source = "Patterns are very important for validating check."

pattern = re.compile('[a-z]+')
# result = pattern.findall(source)
result = pattern.finditer(source)

print(type(result))
print(result)
for el in result:
    if el:
        print(el, source[el.start():el.end()], '---->', el.group())
        # el.start(), el.end()

p = re.compile('[a-z]+')
m = p.match('python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())