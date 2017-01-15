

def dictTest(d, aVal):
    for k in d:
        if d[k] == aVal:
            return k
    return None

lengths = {'one':3, 0:1, 'two':3}
print(dictTest(lengths, 3))