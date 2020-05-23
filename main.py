from PyInquirer import prompt
from rich.console import Console
from startup import startup
import supplements
import generating
console = Console()
startup()

answers = prompt(supplements.questions)
console.print(answers)

