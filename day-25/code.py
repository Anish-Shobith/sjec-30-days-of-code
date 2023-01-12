import json
# read key from json file
with open('../Day-24/key.json', 'r') as f:
    k = json.load(f)
p = ""
for char in input():
    p += k[char]
print(p)