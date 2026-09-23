e2i = {
    "dog": "anjing",
    "cat": "kucing",
    "tiger": "macan"
}

print(e2i)


print(e2i["tiger"])

i2e = {}

for english, indonesia in e2i.items():
    i2e[indonesia] = english

print(i2e)

print(i2e["kucing"])

english_words = set(e2i.keys())
print(english_words)
