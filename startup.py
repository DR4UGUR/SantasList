from rich.console import Console
from PyInquirer import prompt
import supplements
import generating

console = Console()


def startup():
    console.print(r"""
    Santas List is made by DR4UGUR and is available at https://github.com/DR4UGUR/SantasList
    

     _____             _              _     _     _   
    /  ___|           | |            | |   (_)   | |  
    \ `--.  __ _ _ __ | |_ __ _ ___  | |    _ ___| |_ 
     `--. \/ _` | '_ \| __/ _` / __| | |   | / __| __|
    /\__/ / (_| | | | | || (_| \__ \ | |___| \__ \ |_ 
    \____/ \__,_|_| |_|\__\__,_|___/ \_____/_|___/\__|


                                                      """)
    console.print(
        "Welcome to [red]Santas List[/] of naughty passwords. If you chose guided I will ask you a few questions about"
        " the target and then make a dictionary of passwords using all the information I have. [underline]Leave any "
        "information you dont have blank, separate multiple entries with commas[/]. If you chose unguided I will not "
        "ask you any questions and you can manually use word jam "
    )
    console.print("The dictionary will be saved in [underline]this directory[/] and it will have the name "
                  "\"dictionary.txt\"")
    console.print(r"""


    """)


def guided():
    want_word_jam = prompt(
        {
            "type": "input",
            "name": "word_jam",
            "message": "Do you want to use Word Jam? Word Jam combines words, making much much larger lists but also "
                       "taking much longer to finish. If you choose to use word jam you cannot enter more than one name"
                       " for the first, last and SO names (Y/N)",
        }
    )
    print(" ")

    answers = prompt(supplements.questions)

    all_inputs = []
    for i in answers:
        if answers[i] != "":
            words = [answers[i].split(",")]
            for j in words:
                for k in j:
                    k = k.strip()
                    all_inputs.append(k)
    if len(all_inputs) > 1:
        if want_word_jam["word_jam"] != "Y":
            print(
                f"There are {generating.possible_permutations(all_inputs)} possible permutations. This might take a"
                f" while...")
        else:
            permutations = generating.possible_permutations(all_inputs) + \
                           generating.possible_word_jam_permutations(answers["first_name"], answers["last_name"]) + \
                           generating.possible_word_jam_permutations(answers["so_first_name"], answers["so_last_name"])
            print(f"There are {permutations} possible permutations. This might take a while...")
        print(" ")
        for i in all_inputs:
            generating.make_dict(generating.word_replacement(i))
        if want_word_jam["word_jam"] != "Y":
            print("Done!")
        else:
            print(
                "The basic permutations are done, now I will apply the word jam to the names. This might take a while"
                "...")
            generating.make_dict(generating.word_jam(generating.word_replacement(answers["first_name"]),
                                                     generating.word_replacement(answers["last_name"])))
            generating.make_dict(generating.word_jam(generating.word_replacement(answers["so_first_name"]),
                                                     generating.word_replacement(answers["so_last_name"])))
            print("Done!")
    else:
        print(" ")
        print("You have not entered any information so I cant make a dictionary for you")


def unguided():
    print(" ")
    console.print("[underline]Basic permutations[/] are the words with the letters replaced")
    console.print("[underline]Word Jam[/] means all basic permutations of two words are put together")
    print(" ")
    answers = prompt([
        {
            "type": "input",
            "name": "basic",
            "message": "Enter any words you want to use basic permutation on. You can use the same later in word jam. Separate words by commas ->",
        },
        {
            "type": "input",
            "name": "word_jam",
            "message": "Enter any words you want to use word jam on. EXAMPLE: \"first,second;third,fourth;fifth,sixth\" ->",
        },
    ])
    basic = answers["basic"].split(",")
    for i in basic:
        i = i.strip()
    permutations = generating.possible_permutations(basic)
    if ("," in answers["word_jam"]) and (";" in answers["word_jam"]) and (len(answers["word_jam"]) > 1):
        jam_source = answers["word_jam"].split(";")
        jam = []
        for i in jam_source:
            jam.append(i.split(","))
        for i in jam:
            permutations += generating.possible_word_jam_permutations(i[0], i[1])
    elif answers["word_jam"] != "":
        print("Make sure there is a ; and , in your input. Try again")
    print(f"There are {permutations} possible permutations. This might take a while...")
    for i in basic:
        generating.make_dict(generating.word_replacement(i))
    if ("," in answers["word_jam"]) and (";" in answers["word_jam"]) and (len(answers["word_jam"]) > 1):
        for i in jam:
            generating.make_dict(generating.word_jam(generating.word_replacement(i[0]), generating.word_replacement(i[1])))
    print("Done!")
    count = 0
    with open("dictionary.txt", "r") as f:
        for line in f:
            count += 1
    if count != permutations:
        print("Something went wrong. Please contact me at https://github.com/DR4UGUR/SantasList")
