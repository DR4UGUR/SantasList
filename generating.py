import supplements


def possible_permutations(wordlist):
    count = 1
    endcount = 0
    for i in wordlist:
        for j in i:
            if j in supplements.characterswap:
                count *= len(supplements.characterswap[j]) + 1
        endcount += count
        count = 1
    return endcount


def letter_replacement(word, index):
    templist = []
    if word[index] in supplements.characterswap:
        for i in supplements.characterswap[word[index]]:
            new_word = word[:index] + i + word[index + 1:]
            templist.append(new_word)
    return templist


def word_replacement(word):
    templist = [word]
    somelist = []
    replaced_length = 0
    already_replaced = -1
    while already_replaced < len(word) - 1:
        somelist += templist
        templist = []
        for i in somelist[-replaced_length:]:
            replaced = letter_replacement(i, already_replaced + 1)
            replaced_length += len(replaced)
            templist += replaced
        already_replaced += 1
        replaced_length = 0
    somelist += templist
    return somelist


def make_dict(answers):
    f = open("dictionary.txt", "a")
    for i in answers:
        f.write(i)
        f.write("\r")
    f.close()


def word_jam(list1, list2):
    templist = []
    for i in list1:
        for j in list2:
            templist.append(i + j)
    return templist
