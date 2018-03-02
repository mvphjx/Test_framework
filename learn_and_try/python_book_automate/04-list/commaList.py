def commaList(items):
    ret = ''
    for item in items[:-1]:
        ret += item + ', '
    return ret + 'and ' + items[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
spam.sort(reverse=True)
print(spam)
print(commaList(spam))
a=["b","a","c"]
b = sorted(a,reverse=True)

print(b)