import json

x = '{"name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(type(y))

x2 = {"name":"John", "age":30, "city":"New York"}
y2 = json.dumps(x2)
print(type(y2))