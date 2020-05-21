from PyInquirer import prompt
from rich.console import Console
from startup import startup
import supplements
import generating
console = Console()
startup()

answers = prompt(supplements.questions)
console.print(answers)

fname = generating.char_replacement("Luella")
lname = generating.char_replacement("StPierre")
jammed = generating.word_jam(fname, lname)
generating.make_dict(generating.wordlist)
print(len(generating.wordlist)+len(jammed))
