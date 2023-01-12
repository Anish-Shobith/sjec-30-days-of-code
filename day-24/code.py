from collections import Counter
import random
import json

org = "abcdefghijklmnopqrstuvwxyz"
sub = "".join(random.sample(org, len(org)))
tbl = str.maketrans(org, sub)

txt = input()
rep = txt

upper_index = set()
for i in range(len(txt)):
    if txt[i].isupper():
        upper_index.add(i)

txt = txt.lower()
enc_txt = txt.translate(tbl)
enc_list = list(enc_txt)
for i in upper_index:
    enc_list[i] = enc_list[i].upper()

x = "".join(enc_list)
print(x)

#generate key
def calculate_key(c, p):
    c_freq = Counter(c)
    p_freq = Counter(p)
    k = {}
    for c_char, c_count in c_freq.items():
        for p_char, p_count in p_freq.items():
            if c_count == p_count:
                k[c_char] = p_char
                p_freq[p_char] = -1  # Mark as used
                break
    return k

#write key to file
with open('key.json', 'w') as f:
    json.dump(calculate_key(x, rep), f)