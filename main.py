from PyInquirer import prompt
from rich.console import Console
from startup import startup
import supplements
import generating
console = Console()
startup()

answers = prompt(supplements.questions)

all_inputs = []
for i in answers:
    if answers[i] != "":
        all_inputs.append(answers[i])
if len(all_inputs) > 1:
    print(f"There are {generating.possible_permutations(all_inputs)} possible permutations. This will take a while...")
    print(" ")
    for i in all_inputs:
        generating.make_dict(generating.word_replacement(i))
    print("Done!")
else:
    print(" ")
    print("You have not entered any information so I cant make a dictionary for you :(")
