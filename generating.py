import supplements

wordlist = []

"""
def find_all(string, substring):
    length = len(substring)
    c = 0
    indexes = []
    while c < len(string):
        if string[c:c+length] == substring:
            indexes.append(c)
        c = c + 1
    return indexes


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
    for a in range(len(word)):
        forcount = 0
        for n in templist:
            if forcount < 10000:
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
            forcount = forcount + 1
    global wordlist
    templist = list(set(templist))
    templist.sort()
    wordlist = wordlist + templist
    return templist
"""


def letter_replacement(word, index):
    templist = []
    if word[index] in supplements.characterswap:
        for i in supplements.characterswap[word[index]]:
            new_word = word[:index] + i + word[index + 1:]
            templist.append(new_word)
    return templist


def word_replacement(word):
    templist = []
    for i in range(len(word)):
        new_word = letter_replacement(word, i)
        templist = templist + new_word
        for j in new_word:
            for k in range(len(j)):
                if k != i:
                    newer_word = letter_replacement(j, k)
                    templist = templist + newer_word
        return templist


"""
def make_dict(answers):
    for i in answers:
        char_replacement(i)
    f = open("dictionary.txt", "a")
    for i in wordlist:
        f.write(i)
        f.write("\r")
    f.close()


def word_jam(list1, list2):
    templist = []
    for i in list1:
        for j in list2:
            templist.append(i + j)
    global wordlist
    wordlist = wordlist + templist
    return templist
"""


print(word_replacement("Alles"))
