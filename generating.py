import supplements

wordlist = []


def find_all(string, substring):
    length = len(substring)
    c = 0
    indexes = []
    while c < len(string):
        if string[c:c+length] == substring:
            indexes.append(c)
        c = c + 1
    return indexes


def whatever(word, ):
    letter = word[0]


def char_replacement(word):
    print("i need to print something")


"""
def char_replacement(word):
    already_replaced = []
    already_replaced2 = []
    templist = [word]
    for i in word:
        if (i in supplements.characterswap) and not (i in already_replaced):
            l = i
            for j in supplements.characterswap[i]:
                for k in find_all(word, l):
                    m = word[:k] + j + word[k + 1:]
                    templist.append(m)
                if word.count(i) > 1:
                    templist.append(word.replace(i, j))
        already_replaced.append(i)
    print("Test")
    for n in templist:
        for i2 in n:
            if (i2 in supplements.characterswap) and not (i2 in already_replaced2):
                l2 = i2
                for j2 in supplements.characterswap[i2]:
                    for k2 in find_all(n, l2):
                        m2 = n[:k2] + j2 + n[k2 + 1:]
                        templist.append(m2)
                    if n.count(i2) > 1:
                        templist.append(n.replace(i2, j2))
            already_replaced2.append(i2)
        already_replaced2 = []
    global wordlist
    templist = list(set(templist))
    templist. sort()
    wordlist = wordlist + templist
"""


def make_dict(answers):
    f = open("dictionary.txt", "a")
    for i in wordlist:

        f.write(i)
        f.write("\r")
    f.close()


char_replacement("Alles")
print(wordlist)
